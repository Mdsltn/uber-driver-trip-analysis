# 🚗 Uber Driver Trip Analysis
### Python · Pandas · Matplotlib · Seaborn · EDA
*PG Program in Data Science & Business Analytics — McCombs School of Business, UT Austin*

---

## 📌 Project Overview

This project analyses **1,155 Uber trips** made by a single driver over the course of 2016, using Python for end-to-end exploratory data analysis (EDA). The goal was to surface actionable patterns in trip behaviour — including peak demand windows, distance distribution, and purpose-level breakdowns — to answer the business question:

> *"How does a driver's trip behaviour vary across time, purpose, and category — and what patterns can inform smarter scheduling decisions?"*

---

## 📂 Dataset

| Field | Description |
|---|---|
| Source | [Kaggle — My Uber Drives](https://www.kaggle.com/datasets/zusmani/uberdrives) |
| Records | 1,155 trips |
| Period | January – December 2016 |
| Features | START_DATE, END_DATE, CATEGORY, START, STOP, MILES, PURPOSE |

---

## 🛠️ Tools & Techniques

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- Data cleaning: null handling, datetime parsing, column normalisation
- Feature engineering: extracted month, day-of-week, and hour from timestamps
- EDA: value counts, groupby aggregations, distribution analysis
- Visualisation: bar charts, pie chart, histogram, time-series line plot

---

## 🔍 Key Findings

| Insight | Finding |
|---|---|
| **Trip category split** | ~96% of trips were Business; Personal trips were rare |
| **Top trip purpose** | Meeting — the dominant driver of ride demand |
| **Busiest day** | Friday recorded the highest number of trips |
| **Peak month** | October/November had the highest cumulative mileage |
| **Typical trip distance** | Median trip was ~5–6 miles; most trips under 15 miles |
| **Long-haul outliers** | A small number of trips exceeded 50 miles — likely airport/client site runs |

> 💡 **Business implication:** Since nearly all trips were business-related, scheduling optimisation should focus on weekday working hours — particularly Tuesday through Friday. Weekend availability has minimal impact on utilisation.

---

## 📊 Visualisations

### 1. Business vs Personal Trip Split
![Category Split](images/01_category_split.png)

---

### 2. Top 10 Trip Purposes
![Top Purposes](images/02_top_purposes.png)

---

### 3. Trips by Day of Week
![Day of Week](images/03_trips_by_dow.png)

---

### 4. Total Miles Driven per Month
![Monthly Miles](images/04_monthly_miles.png)

---

### 5. Distribution of Trip Distances
![Distance Distribution](images/05_distance_distribution.png)

---

## 📁 Repository Structure

```
📦 Uber-Drives-Analysis
 ┣ 📓 Solution.ipynb        — Full analysis notebook with code + outputs
 ┣ 📄 uberdrive-2.csv       — Raw dataset
 ┣ 🐍 generate_charts.py    — Standalone script to regenerate all charts
 ┣ 📁 images/               — Exported chart PNGs (used in this README)
 ┗ 📄 README.md
```

---

## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Mdsltn/Python-For-Data-Science---Uber-Drives-Project.git
cd Python-For-Data-Science---Uber-Drives-Project

# 2. Install dependencies
pip install pandas matplotlib seaborn numpy

# 3. Run the notebook
jupyter notebook Solution.ipynb

# 4. Or regenerate charts only
python generate_charts.py
```

---

## 👤 Author

**Mohammed Sultan**
Data Analyst | 11+ years Enterprise SaaS | Bengaluru, India
[LinkedIn](https://linkedin.com/in/mdsltn) · [GitHub](https://github.com/Mdsltn)

*Part of a data analytics portfolio built during the PG Program in Data Science & Business Analytics (McCombs School of Business, UT Austin)*
