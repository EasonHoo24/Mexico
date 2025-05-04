
import streamlit as st
import pandas as pd

st.set_page_config(page_title="美墨关税与SME政策追踪工具", layout="wide")
st.title("📊 美墨关税与中小企业（SME）政策追踪助手 v1")
st.markdown("本工具将每日追踪中美墨主流媒体中的出口关税、SME支持等政策内容，并进行中西双语摘要与分类分析。")

@st.cache_data
def load_data():
    return pd.read_csv("美墨关税与SME政策追踪_DEMO.csv")

df = load_data()

# 筛选器
with st.sidebar:
    st.header("🔍 筛选条件")
    selected_type = st.multiselect("政策类型", df["政策类型"].unique(), default=list(df["政策类型"].unique()))
    selected_sentiment = st.multiselect("情绪倾向", df["情绪倾向"].unique(), default=list(df["情绪倾向"].unique()))
    selected_industry = st.multiselect("行业分类", df["行业分类"].unique(), default=list(df["行业分类"].unique()))

df_filtered = df[
    df["政策类型"].isin(selected_type) &
    df["情绪倾向"].isin(selected_sentiment) &
    df["行业分类"].isin(selected_industry)
]

st.success(f"共筛选出 {len(df_filtered)} 条政策动态")
st.dataframe(df_filtered, use_container_width=True)

st.download_button("📥 下载筛选结果 CSV", df_filtered.to_csv(index=False).encode("utf-8-sig"), file_name="筛选政策.csv", mime="text/csv")

st.markdown("---")
st.caption("© 2025 Alibaba México | 自动政策追踪工具 Powered by AI")
