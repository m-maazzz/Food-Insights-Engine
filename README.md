# 🍎 Food Insights Engine

A Python-based nutrition analytics platform built using the USDA FoodData Central dataset. The project demonstrates data loading, cleaning, analysis, visualization, and report generation using Pandas and Object-Oriented Programming (OOP).

## 🚀 Project Overview

Food Insights Engine processes real-world nutrition data from the USDA Foundation Foods dataset and generates valuable nutritional insights such as:

* Top protein-rich foods
* Top calorie-dense foods
* Top fat-rich foods
* Dataset quality reports
* Nutrition summary reports
* Data visualizations

The project is designed to simulate a real-world data analytics pipeline and demonstrate practical Pandas, Python, and software engineering skills.

---

## 📂 Project Structure

```text
Food Insights Engine/

├── food_data/
├── reports/
├── charts/
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── cleaner.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── report_generator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🏗️ Architecture

```text
USDA Dataset
      │
      ▼
DataLoader
      │
      ▼
NutritionCleaner
      │
      ▼
NutritionAnalyzer
      │
      ▼
ReportGenerator
      │
      ▼
NutritionVisualizer
```

---

## 📊 Features

### Data Loading

* Load USDA nutrition datasets
* Modular data ingestion using DataLoader

### Data Quality Checks

* Missing value analysis
* Duplicate detection
* Dataset summary generation

### Nutrition Analytics

* Top protein foods
* Top fat foods
* Top calorie foods
* Nutrient-based ranking

### Report Generation

* Nutrition summary report
* CSV exports for analytics results

### Visualization

* Top protein foods chart
* Top fat foods chart
* Top calorie foods chart
* Category distribution chart

---

## 🧠 Technologies Used

* Python
* Pandas
* Matplotlib
* Object-Oriented Programming (OOP)
* USDA FoodData Central Dataset

---

## 📈 Example Outputs

Generated Reports:

```text
reports/
├── nutrition_summary.txt
├── top_protein_foods.csv
├── top_fat_foods.csv
└── top_calorie_foods.csv
```

Generated Charts:

```text
charts/
├── top_protein_foods.png
├── top_fat_foods.png
├── top_calorie_foods.png
└── category_distribution.png
```

---

## ▶️ Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## 📚 Key Concepts Demonstrated

* Pandas Data Analysis
* Data Cleaning
* Data Visualization
* Relational Data Modeling
* DataFrame Merging
* OOP Design
* Modular Python Architecture
* Report Generation

---

## 🎯 Future Improvements

* Advanced nutrient analytics
* Nutrient comparison dashboard
* Interactive visualizations
* FastAPI integration
* Nutrition recommendation engine

---

## 👨‍💻 Author

Built as a hands-on learning project to strengthen Python, Pandas, OOP, and Data Analytics skills using real-world nutrition datasets.
