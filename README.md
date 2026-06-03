# Trend Intelligence Platform

An automated trend discovery and intelligence platform that continuously collects technology news and signals from multiple sources, analyzes emerging trends, generates AI-powered insights, and presents results through an interactive dashboard.

## Features

* Automated HackerNews data collection
* RSS feed aggregation
* GitHub trending analysis
* Data deduplication and preprocessing
* Trend clustering and scoring
* Topic modeling using NLP
* AI-generated insights
* Executive market brief generation
* PDF report generation
* Interactive Streamlit dashboard
* Automated execution every 6 hours using GitHub Actions
* Cloud deployment using Streamlit Community Cloud

---

## Live Demo

https://internet-noise-filter-qwqrbc78dmibtjkz4ut95a.streamlit.app/

---

## Architecture

### Data Sources

* HackerNews
* RSS Feeds
* GitHub Trending

### Pipeline

Data Collection → Data Processing → Trend Analysis → Trend Clustering → Topic Modeling → AI Insights → Report Generation → Dashboard

---

## Tech Stack

### Backend

* Python

### Data Processing

* Pandas
* Scikit-Learn

### Database

* SQLite

### Dashboard

* Streamlit

### Reporting

* ReportLab

### Automation

* GitHub Actions

### Deployment

* Docker
* Streamlit Community Cloud

---

## Project Structure

```text
internet-noise-filter/

├── analysis/
├── collectors/
├── dashboard/
├── database/
├── preprocess/
├── outputs/
├── history/

├── main.py
├── run_pipeline.py
├── requirements.txt
├── trend_intelligence.db
├── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/bandhav100/internet-noise-filter.git
cd internet-noise-filter
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

```bash
python3 run_pipeline.py
```

### Pipeline Stages

1. Collect HackerNews Data
2. Collect RSS Data
3. Collect GitHub Trending Data
4. Merge Datasets
5. Remove Duplicates
6. Trend Analysis
7. Trend Clustering
8. Save Trend History
9. Trend Change Analysis
10. Topic Modeling
11. AI Insight Generation
12. Executive Summary
13. Report Generation
14. PDF Report Generation

---

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard Includes:

* Dataset Explorer
* Database Preview
* Trend Analysis
* Topic Discovery
* Historical Trend Tracking
* AI Generated Insights
* Executive Market Brief

---

## Automation

The platform automatically executes every 6 hours using GitHub Actions.

Workflow:

```text
GitHub Actions
      ↓
run_pipeline.py
      ↓
Collect Data
      ↓
Analyze Trends
      ↓
Generate Reports
      ↓
Update Dashboard Data
```

---

## Deployment

### Streamlit Cloud

The dashboard is deployed and publicly accessible through Streamlit Community Cloud.

### Docker

Containerized deployment support is included for local and VPS deployments.

---

## Sample Insights

* AI remains the dominant technology trend across monitored sources.
* NVIDIA continues to play a major role in technology discussions.
* OpenAI remains a key ecosystem driver.
* GitHub activity indicates growing interest in agentic workflows.

---

## Future Improvements

* Trend Forecasting
* Email Alert System
* API Access
* User-specific Dashboards
* Multi-source Trend Scoring Improvements

---

## Author

Bandhav

GitHub:
https://github.com/bandhav100

