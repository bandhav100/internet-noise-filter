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
* Automated execution every 6 hours using Cron

---

## Architecture

Data Sources

* HackerNews
* RSS Feeds
* GitHub Trending

Pipeline

Data Collection → Data Processing → Trend Analysis → Topic Modeling → AI Insights → Report Generation → Dashboard

---

## Tech Stack

### Backend

* Python

### Data Processing

* Pandas
* Scikit-learn

### Database

* SQLite

### Dashboard

* Streamlit

### Reporting

* ReportLab

### Automation

* Cron Jobs

---

## Project Structure

```text
internet-noise-filter/

├── analysis/
├── collectors/
├── dashboard/
├── database/
├── preprocess/

├── main.py
├── run_pipeline.py
├── requirements.txt
├── README.md
```

---

## Installation

Clone Repository

```bash
git clone https://github.com/bandhav100/internet-noise-filter.git
cd internet-noise-filter
```

Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

```bash
python3 run_pipeline.py
```

Pipeline Stages

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

Dashboard includes:

* Dataset Explorer
* Database Preview
* Trend Analysis
* Topic Discovery
* Historical Trend Tracking
* AI Generated Insights
* Executive Market Brief

---

## Automation

The platform automatically runs every 6 hours using Cron.

Example:

```bash
0 */6 * * * python run_pipeline.py
```

---

## Sample Insights

* AI remains the dominant technology trend across monitored sources.
* NVIDIA continues to play a major role in technology discussions.
* OpenAI and Anthropic remain key ecosystem drivers.
* GitHub activity indicates growing interest in agentic workflows.

---

## Future Improvements

* Docker Deployment
* VPS Deployment
* Nginx Reverse Proxy
* SSL/HTTPS Support
* CI/CD with GitHub Actions
* Multi-source Trend Scoring
* Email Alert System

---

## Author

Bandhav

GitHub:
https://github.com/bandhav100
