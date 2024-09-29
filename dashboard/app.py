import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
hour_df = pd.read_csv("dataset_clean.csv")

# Set page title and header
st.title("Bike Sharing Analysis")
st.header("Exploratory Data Analysis")

# Display the dataframe
st.subheader("Dataset")
st.dataframe(hour_df.head())

# Visualisasi pengaruh suhu dan cuaca terhadap jumlah penyewaan sepeda
st.subheader("Pengaruh Suhu dan Cuaca terhadap Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', hue='weathersit', data=hour_df, ax=ax)
plt.xlabel('Suhu (Celcius)')
plt.ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Visualisasi pola penyewaan sepeda antara hari kerja dan akhir pekan
st.subheader("Perbedaan Pola Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weekday', y='cnt', data=hour_df, hue='workingday', ax=ax)
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.xticks(rotation=45)
st.pyplot(fig)

# Analisis rata-rata jumlah penyewaan sepeda pada hari kerja dan akhir pekan
rata_rata_penyewaan_hari_kerja = hour_df[hour_df['workingday'] == 1]['cnt'].mean()
rata_rata_penyewaan_akhir_pekan = hour_df[hour_df['workingday'] == 0]['cnt'].mean()

st.subheader("Rata-Rata Penyewaan Sepeda")
st.write(f"Rata-rata penyewaan sepeda pada hari kerja: {rata_rata_penyewaan_hari_kerja:.2f}")
st.write(f"Rata-rata penyewaan sepeda pada akhir pekan: {rata_rata_penyewaan_akhir_pekan:.2f}")

# Conclusion
st.header("Conclusion")
st.write("- Poor weather conditions, such as rain or snow, significantly decrease bike rentals. This is likely due to safety concerns and discomfort associated with cycling in adverse weather.")
st.write("- Bike rentals tend to be higher on weekdays, suggesting that a substantial portion of users utilize bikes for commuting purposes or daily errands.")

# Run the app
!streamlit run app.py &>/dev/null&

!npx localtunnel --port 8501
