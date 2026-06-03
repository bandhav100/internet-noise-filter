import streamlit as st
import pandas as pd
import json
import sqlite3
import os
# ==========================================
# PAGE CONFIG
# ==========================================
required_files = [
    "outputs/trend_scores.json",
    "outputs/source_stats.json",
    "outputs/source_comparison.json",
    "outputs/top_trends_v2.json",
    "outputs/trend_changes.json",
    "outputs/topic_models.json",
    "outputs/insights.json",
    "outputs/executive_brief.txt",
    "outputs/last_run.txt",
    "history/trend_history.csv",
    "trend_intelligence.db"
]

for file in required_files:
    if not os.path.exists(file):
        st.error(f"Missing file: {file}")
        st.stop()
st.set_page_config(
    page_title="Trend Intelligence Platform",
    page_icon="|*|",
    layout="wide"
)

st.title("Trend Intelligence Platform")
# ==========================================
# LOAD JSON FILES
# ==========================================

with open("outputs/trend_scores.json", "r") as file:
    trend_scores = json.load(file)

with open("outputs/source_stats.json", "r") as file:
    source_stats = json.load(file)

with open("outputs/source_comparison.json", "r") as file:
    source_comparison = json.load(file)

with open("outputs/top_trends_v2.json", "r") as file:
    top_keywords = json.load(file)

with open("outputs/trend_changes.json", "r") as file:
    trend_changes = json.load(file)
with open(
    "outputs/topic_models.json",
    "r"
) as file:
    topic_models = json.load(file)
with open(
    "outputs/insights.json",
    "r"
) as file:

    insights = json.load(file)
with open(
    "outputs/executive_brief.txt",
    "r"
) as file:
    executive_brief = file.read()

with open(
    "outputs/last_run.txt",
    "r"
) as file:

    last_run = file.read()
st.caption(
    f"Last Updated: {last_run}"
)

st.sidebar.success(
    f"Last Updated: {last_run}"
)

# ==========================================
# LOAD HISTORY
# ==========================================

history_df = pd.read_csv(
    "history/trend_history.csv"
)

# ==========================================
# LOAD SQLITE DATA
# ==========================================

conn = sqlite3.connect(
    "trend_intelligence.db"
)

dataset_df = pd.read_sql_query(
    """
    SELECT *
    FROM articles
    """,
    conn
)

conn.close()

# ==========================================
# DATAFRAMES
# ==========================================

trend_df = pd.DataFrame(
    list(trend_scores.items()),
    columns=[
        "Category",
        "Score"
    ]
)

source_df = pd.DataFrame(
    list(source_stats.items()),
    columns=[
        "Source",
        "Count"
    ]
)

keywords_df = pd.DataFrame(
    list(top_keywords.items()),
    columns=[
        "Keyword",
        "Frequency"
    ]
)

comparison_df = pd.DataFrame(
    source_comparison
)
topic_df = pd.DataFrame(
    list(topic_models.items()),
    columns=[
        "Topic",
        "Score"
    ]
)

topic_df = topic_df.sort_values(
    by="Score",
    ascending=False
)
# ==========================================
# EXECUTIVE MARKET BRIEF
# ==========================================

st.header(
    "Executive Market Brief"
)

st.success(
    executive_brief
)
# ==========================================
# EXECUTIVE SUMMARY
# ==========================================

st.header("Executive Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "AI",
    trend_scores["AI"],
    trend_changes["AI"]
)

col2.metric(
    "Programming",
    trend_scores["Programming"],
    trend_changes["Programming"]
)

col3.metric(
    "Security",
    trend_scores["Security"],
    trend_changes["Security"]
)

col4.metric(
    "Startups",
    trend_scores["Startups"],
    trend_changes["Startups"]
)

# ==========================================
# DATASET STATISTICS
# ==========================================

st.header("Dataset Statistics")

total_records = len(dataset_df)

total_sources = len(source_df)

top_trend = max(
    trend_scores,
    key=trend_scores.get
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Records",
    total_records
)

col2.metric(
    "Sources",
    total_sources
)

col3.metric(
    "Top Trend",
    top_trend
)

# ==========================================
# SOURCE DISTRIBUTION
# ==========================================

st.header("Source Distribution")

col1, col2 = st.columns(2)

with col1:

    st.dataframe(
        source_df,
        use_container_width=True
    )

with col2:

    st.bar_chart(
        source_df.set_index(
            "Source"
        )
    )

# ==========================================
# TREND CLUSTER ANALYSIS
# ==========================================

st.header("Trend Cluster Analysis")

col1, col2 = st.columns(2)

with col1:

    st.dataframe(
        trend_df,
        use_container_width=True
    )

with col2:

    st.bar_chart(
        trend_df.set_index(
            "Category"
        )
    )

# ==========================================
# SOURCE-WISE TREND COMPARISON
# ==========================================

st.header("Source-wise Trend Comparison")

st.dataframe(
    comparison_df,
    use_container_width=True
)

st.bar_chart(
    comparison_df
)

# ==========================================
# TOP KEYWORDS
# ==========================================

st.header("Top Keywords")

col1, col2 = st.columns(2)

with col1:

    st.dataframe(
        keywords_df,
        use_container_width=True
    )

with col2:

    st.bar_chart(
        keywords_df.set_index(
            "Keyword"
        )
    )
# ==========================================
# TOPIC DISCOVERY
# ==========================================

st.header(
    "Topic Discovery"
)

col1, col2 = st.columns(2)

with col1:

    st.dataframe(
        topic_df,
        use_container_width=True
    )

with col2:

    st.bar_chart(
        topic_df.set_index(
            "Topic"
        )
    )
# ==========================================
# TREND LEADERBOARD
# ==========================================

st.header("Trend Leaderboard")

leaderboard = trend_df.sort_values(
    by="Score",
    ascending=False
)

leaderboard.index = (
    leaderboard.index + 1
)

st.dataframe(
    leaderboard,
    use_container_width=True
)

# ==========================================
# GENERATED INSIGHTS
# ==========================================

st.header("Generated Insights")

top_category = max(
    trend_scores,
    key=trend_scores.get
)

st.success(
    f"{top_category} is currently the dominant trend across all sources."
)

hn_ai = source_comparison["HackerNews"]["AI"]
rss_ai = source_comparison["TechCrunch"]["AI"]

if hn_ai > rss_ai:

    st.info(
        "AI discussions are primarily driven by HackerNews."
    )

hn_programming = source_comparison["HackerNews"]["Programming"]
rss_programming = source_comparison["TechCrunch"]["Programming"]

if hn_programming > rss_programming:

    st.info(
        "Programming discussions are significantly stronger on HackerNews."
    )

hn_startups = source_comparison["HackerNews"]["Startups"]
rss_startups = source_comparison["TechCrunch"]["Startups"]

if rss_startups > hn_startups:

    st.info(
        "Startup discussions are proportionally stronger on TechCrunch."
    )

if trend_scores["Security"] < 15:

    st.warning(
        "Security discussions currently represent a smaller share of the overall dataset."
    )

# ==========================================
# HISTORICAL TREND TRACKING
# ==========================================

st.header("Historical Trend Tracking")

st.dataframe(
    history_df,
    use_container_width=True
)

history_chart = history_df.set_index(
    "date"
)

st.line_chart(
    history_chart
)

# ==========================================
# TREND MOVEMENTS
# ==========================================

st.header("Trend Movements")

top_gainer = max(
    trend_changes,
    key=trend_changes.get
)

top_decliner = min(
    trend_changes,
    key=trend_changes.get
)

col1, col2 = st.columns(2)

with col1:

    st.success(
        f"Top Gainer: {top_gainer} ({trend_changes[top_gainer]})"
    )

with col2:

    st.error(
        f"Top Decliner: {top_decliner} ({trend_changes[top_decliner]})"
    )

# ==========================================
# SEARCH ARTICLES
# ==========================================

st.header("Search Articles")

search = st.text_input(
    "Search by keyword"
)

if search:

    filtered_df = dataset_df[
        dataset_df["title"]
        .astype(str)
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.write(
        f"Articles Found: {len(filtered_df)}"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# ==========================================
# DATASET EXPLORER
# ==========================================

st.header("Dataset Explorer")

with st.expander(
    "View Full Dataset"
):

    st.dataframe(
        dataset_df,
        use_container_width=True
    )

# ==========================================
# DATABASE PREVIEW
# ==========================================

st.header("Database Preview")

st.write(
    "Showing first 10 records from SQLite database"
)

st.dataframe(
    dataset_df.head(10),
    use_container_width=True
)
#==========================================
#EXECUTIVE SUMMARY
#==========================================
st.header(
    "Executive Intelligence Brief"
)

with open(
    "outputs/executive_summary.txt",
    "r"
) as file:

    summary = file.read()

st.info(
    summary
)
# ==========================================
# AI GENERATED INSIGHTS
# ==========================================

st.header(
    "AI Generated Insights"
)

for insight in insights:

    st.info(
        insight
    )
# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.header(
    "Download Reports"
)

with open(
    "outputs/trend_report.pdf",
    "rb"
) as pdf:

    st.download_button(
        label="Download Trend Report PDF",
        data=pdf,
        file_name="trend_report.pdf",
        mime="application/pdf"
    )
# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Trend Intelligence Platform | SQLite Powered Analytics Dashboard"
)
