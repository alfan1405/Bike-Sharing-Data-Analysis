import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
hour_df = pd.read_csv("dashboard/main_data.csv")

# Set page title and header
st.title("Bike Sharing Analysis")
st.header("Exploratory Data Analysis")

# Display the dataframe
st.subheader("Dataset")
st.dataframe(hour_df.head())

# Visualization of the effect of temperature and weather on the number of bicycle rentals
st.subheader("The Effect of Temperature and Weather on the Number of Bicycle Rentals")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', hue='weathersit', data=hour_df, ax=ax)
plt.xlabel('Suhu (Celcius)')
plt.ylabel('Number of Bike Rentals')
st.pyplot(fig)

# Visualization of bicycle rental patterns between weekdays and weekends
st.subheader("Difference in Bike Rental Patterns between Weekdays and Weekends")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weekday', y='cnt', data=hour_df, hue='workingday', ax=ax)
plt.xlabel('Days of the Week')
plt.ylabel('Number of Bike Rentals')
plt.xticks(rotation=45)
st.pyplot(fig)

# Analysis of the average number of bicycle rentals on weekdays and weekends
average_working_days_rental = hour_df[hour_df['workingday'] == 1]['cnt'].mean()
average_weekend_rental = hour_df[hour_df['workingday'] == 0]['cnt'].mean()

st.subheader("Bike Rental Average")
st.write(f"Average bike rentals on weekdays: {average_working_days_rental}:.2f")
st.write(f"Average bike rentals on weekends: {average_weekend_rental}:.2f")

# Conclusion
st.header("Conclusion")
st.write("- Poor weather conditions, such as rain or snow, significantly decrease bike rentals. This is likely due to safety concerns and discomfort associated with cycling in adverse weather.")
st.write("- Bike rentals tend to be higher on weekdays, suggesting that a substantial portion of users utilize bikes for commuting purposes or daily errands.")

plt.tight_layout()
st.pyplot(fig)

st.caption('Copyright (c) Alfan Alfiansyah 2024')
