import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Loading dataset
def load_data():
    df = pd.read_csv("Datasets/Titanic_tested.csv")
    df['Agegroup'] = pd.cut(df['Age'], bins = [0, 12, 18, 35, 60, 80], labels=['child', 'teen', 'adult', 'senior', 'elderly'])
    return df

df = load_data()

# Adding widgets for user input (optional)
# sidebar for filtering data
st.sidebar.header('Filters')

# dropdown to select passenger class
pclass_filter = st.sidebar.selectbox('Select Passenger Class:', [1, 2, 3])

# Apply filter
filtered_df = df[df['Pclass'] == pclass_filter]

# Visualization and Analysis
# survival by passenger class and gender
st.header('Survival by Passenger Class and Gender')

# Grouped bar chart for Survival by Passenger Class and Gender
plt.figure(figsize=(10, 6))
sns.barplot(x='Pclass', y='Survived', hue='Sex', data=filtered_df, palette='Set2')

# Show plot in Streamlit
st.pyplot(plt)

# # survival by age group
# st.header('Survival by Age Group')

# # Grouped bar chart for Survival by Age Group
# plt.figure(figsize=(10, 6))
# sns.barplot(x='AgeGroup', y='Survived', hue='Pclass', data=filtered_df, palette='Blues_d')

# # Show plot in Streamlit
# st.pyplot(plt)

# box plot for age distribution vs survival
st.header('Age Distribution by Survival')

# Box plot for Age vs Survival
plt.figure(figsize=(8, 6))
sns.boxplot(x='Survived', y='Age', data=filtered_df, palette='Set1')

# Show plot in Streamlit
st.pyplot(plt)

#box plot for fare dist ve survival
st.header('Fare Distribution by Survival')

# Box plot for Fare vs Survival
plt.figure(figsize=(8, 6))
sns.boxplot(x='Survived', y='Fare', data=filtered_df, palette='Set2')

# Show plot in Streamlit
st.pyplot(plt)

# Display Data Tables
st.header('Data Overview')
st.write(df.head())  # Display first 5 rows of the dataset

# Optionally display filtered data
st.write(f"Filtered Data (Passenger Class: {pclass_filter})")
st.write(filtered_df)
