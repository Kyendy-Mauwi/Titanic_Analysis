# Titanic Analysis

This project explores the Titanic dataset to analyze factors that influenced survival rates. The app visualizes key data insights and allows users to filter and interact with the dataset.

## Table of Contents
1. [Introduction](#introduction)
2. [App Features](#app-features)
3. [How to Interact with the Data](#how-to-interact-with-the-data)
4. [Setup Instructions](#setup-instructions)
5. [Dependencies](#dependencies)
6. [License](#license)

## Introduction

This app uses the Titanic dataset to analyze the survival rates of passengers aboard the Titanic. The data is analyzed based on various factors such as:
- **Passenger Class**
- **Age Group**
- **Gender**
- **Family Size**

Visualizations are provided to give users insights into how these factors influenced survival.

## App Features

- **Filter by Passenger Class:** Select between classes 1, 2, or 3 to see the survival rate for each class.
- **Age Group Analysis:** View survival rates segmented by different age groups (e.g., Child, Adult, Elderly).
- **Survival Rate Visualizations:** Visualize survival data based on passenger class, age, and gender.

## How to Interact with the Data

Once the app is running, you can interact with the data in the following ways:

### 1. **Select Passenger Class:**
   - Use the sidebar to select a passenger class (1, 2, or 3).
   - The bar charts will update to show the survival rate for the selected class.

### 2. **Select Age Group:**
   - The app will categorize passengers into different age groups such as Child, Adult, and Elderly.
   - Use the Age Group filter to see how survival rates varied by age.

### 3. **Visualize Survival Data:**
   - The app provides bar charts that show survival rates based on various features like **Pclass**, **AgeGroup**, and **Sex**.
   - The visualizations dynamically update as you adjust filters.

### 4. **Hover for Details:**
   - Hover over the visualizations to see more detailed information such as exact survival rates for each category.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kyendy-Mauwi/Titanic_Analysis.git
   cd Titanic_Analysis
   ```

2. **Create and activate a virtual environment (optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   Ensure that you have the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run titanic_analysis.py
   ```

5. **Interact with the app** by navigating to `http://localhost:8501` in your web browser.

## Dependencies

This project requires the following Python libraries:

- `pandas`
- `seaborn`
- `matplotlib`
- `streamlit`
- `numpy`
- `scikit-learn`

To install the dependencies, you can run:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
