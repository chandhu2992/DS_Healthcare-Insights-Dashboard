# 🏥 Healthcare Insights Dashboard

## 📌 Project Overview

The Healthcare Insights Dashboard is an interactive data analytics application developed using Python, MySQL, and Streamlit. The dashboard helps healthcare organizations analyze patient admissions, diagnoses, doctor performance, bed utilization, billing trends, and treatment outcomes through interactive visualizations and SQL-driven insights.

This project integrates MySQL for data storage and SQL analysis with Python and Streamlit for visualization, enabling healthcare providers to make data-driven decisions.

---

## 🎯 Objectives

* Analyze patient admission and discharge trends.
* Identify common diseases and diagnosis patterns.
* Monitor doctor performance and patient feedback.
* Evaluate hospital bed occupancy and utilization.
* Compare billing amounts with insurance coverage.
* Generate actionable insights for hospital management.

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* MySQL

### Libraries Used

* Pandas
* NumPy
* Plotly Express
* Matplotlib
* MySQL Connector
* SQLAlchemy
* PyMySQL
* Streamlit

---

## 🗄 Database Information

### Database Name

`healthcare`

### Table Name

`healthcare_data`

### Key Attributes

* Patient_ID
* Admit_Date
* Discharge_Date
* Diagnosis
* Bed_Occupancy
* Test
* Doctor
* Followup_Date
* Feedback
* Billing_Amount
* Health_Insurance_Amount

---

## 🚀 Features

### 📊 Patient Admission Analysis

* Monthly admission trends
* Seasonal admission patterns
* Peak admission periods

### 🩺 Diagnosis Analysis

* Most common diseases
* Seasonal disease occurrence
* Diagnosis frequency comparison

### 👨‍⚕️ Doctor Performance Dashboard

* Patient distribution by doctor
* Average patient feedback
* Doctor workload analysis

### 🏨 Bed Utilization Analysis

* ICU occupancy analysis
* General ward utilization
* Private room occupancy distribution

### 💰 Billing and Insurance Analysis

* Billing amount trends
* Insurance coverage comparison
* Billing discrepancy analysis

### 📈 Treatment and Recovery Analysis

* Follow-up appointment tracking
* Recovery time analysis
* Treatment outcome monitoring

---

## 🔍 Sample SQL Analysis

The dashboard performs several SQL-based analyses to generate healthcare insights:

1. **Admission Trends Over Time** – Track monthly hospital admissions and identify patterns in patient intake over different periods.

2. **Most Common Diagnoses** – Identify the top five most frequent diagnoses to understand prevalent health conditions.

3. **Bed Utilization Analysis** – Examine different types of bed occupancy, including ICU, General, and Private wards.

4. **Length of Stay Distribution** – Assess average and maximum patient stay durations to evaluate hospital resource utilization.

5. **Seasonal Admission Patterns** – Determine trends in hospital admissions across different seasons and identify peak periods.

Additional analyses are performed to evaluate patient outcomes, billing efficiency, doctor performance, follow-up appointments, and hospital resource utilization.

---

## 📊 Dashboard Modules

### 1. Trends in Admissions Over Time

Analyze monthly patient admissions and identify growth trends.

### 2. Diagnosis Frequency Analysis

Identify the most common diagnoses and disease patterns.

### 3. Bed Occupancy Analysis

Visualize occupancy distribution across different bed categories.

### 4. Length of Stay Distribution

Evaluate average and maximum patient stay durations.

### 5. Seasonal Admission Patterns

Track patient admission trends across different seasons.

### 6. Seasonal Disease Occurrence

Analyze disease prevalence during different times of the year.

### 7. Doctor Patient Distribution

Measure the number of patients treated by each doctor.

### 8. Patient Feedback Analysis

Assess doctor performance using patient ratings and reviews.

### 9. Length of Stay and Bed Utilization Analysis

Examine hospital resource usage and patient stay duration.

### 10. Billing vs Insurance Coverage Analysis

Identify differences between treatment costs and insurance coverage.

### 11. Test and Diagnosis Relationship

Determine the relationship between medical tests and diagnoses.

### 12. Follow-Up Appointment Analysis

Track patient follow-ups and treatment continuity.

### 13. Most Common Diseases with Average Billing Amount

Analyze disease frequency and associated treatment costs.

### 14. Bed Occupancy Trends and Peak Admission Periods

Monitor hospital capacity and patient volume fluctuations.

### 15. Patient Recovery and Treatment Outcomes

Evaluate recovery timelines and treatment effectiveness.

### 16. Impact of Tests on Total Billing Amount

Analyze how diagnostic tests contribute to overall healthcare costs.

---

## 📈 Key Insights

* Seasonal fluctuations significantly impact patient admissions.
* Certain diagnoses account for a large percentage of hospital visits.
* ICU beds experience higher occupancy during peak periods.
* Insurance coverage varies considerably across diagnoses.
* Patient feedback helps identify opportunities for improving healthcare services.

---

## 📢 Recommendations

### 1. Allocate More Staff to Busy Departments

Increase doctor and nurse availability in departments experiencing high admission rates to reduce waiting times and improve patient care.

### 2. Improve Patient Feedback Scores

Provide additional training and performance reviews for doctors with lower patient satisfaction ratings.

### 3. Optimize Bed Utilization

Monitor occupancy patterns and allocate resources efficiently during peak periods.

### 4. Reduce High Treatment Costs

Review expensive treatments and identify opportunities to improve affordability while maintaining quality care.

### 5. Enhance Follow-Up Management

Improve follow-up tracking systems to increase treatment effectiveness and patient recovery rates.

### 6. Improve Insurance Coverage Planning

Analyze coverage gaps and negotiate better insurance support for patients.

---

## 🚀 Future Enhancements

* Machine Learning-based disease prediction.
* Patient risk assessment models.
* Healthcare cost forecasting.
* Real-time hospital monitoring dashboard.
* Automated report generation.
* Interactive KPI tracking system.

---

## ▶️ How to Run the Project

### Step 1: Install Required Packages

```bash
pip install pandas numpy matplotlib plotly streamlit mysql-connector-python sqlalchemy pymysql
```

### Step 2: Import Dataset into MySQL

* Create a database named `healthcare`
* Import the healthcare dataset into the table `healthcare_data`

### Step 3: Run the Streamlit Application

```bash
streamlit run project_healthcare.py
```

### Step 4: Open in Browser

```text
http://localhost:8501
```

---

## 👨‍💻 Author

**Chandra Shekar**

Healthcare Analytics Project developed using Python, MySQL, SQL, Plotly, and Streamlit.
