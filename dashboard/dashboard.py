import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
# sns.set(style='dark')

day_df = pd.read_csv('bike_day.csv')
hour_df = pd.read_csv('bike_hour.csv')

st.title('Bike Sharing Usage Analysis')

season_order = ['Spring', 'Summer', 'Fall', 'Winter']

day_df['season'] = pd.Categorical(day_df['season'], categories=season_order, ordered=True)

st.header("Total Pengguna Berdasarkan Musim")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='season', y='total_users', data=day_df, ax=ax, color='#4682B4', ci=None)
ax.set_title('Total Pengguna Berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Total Pengguna')

plt.tight_layout()
st.pyplot(fig)

st.header("Total Pengguna Berdasarkan Cuaca")

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='weather_situation', y='registered_users', data=day_df, color='#4682B4', ci=None, label='Pengguna Terdaftar')
sns.barplot(x='weather_situation', y='casual_users', data=day_df, color='#FFA500', ci=None, label='Pengguna Kasual')

ax.set_title('Total Pengguna Berdasarkan Cuaca')
ax.set_xlabel('Cuaca')
ax.set_ylabel('Total Pengguna')
ax.legend()

plt.tight_layout()
st.pyplot(fig)

st.header("Pengguna Sepeda: Hari Kerja vs Akhir Pekan")

working_day_summary = hour_df.groupby('working_day')[['total_users', 'casual_users', 'registered_users']].sum()

fig, ax = plt.subplots(figsize=(8, 6))
bar_width = 0.4
index = np.arange(len(working_day_summary))

ax.bar(index, working_day_summary['casual_users'], bar_width, label='Pengguna Kasual', color='#FFA500')
ax.bar(index, working_day_summary['registered_users'], bar_width, bottom=working_day_summary['casual_users'], label='Pengguna Terdaftar', color='#4682B4')

ax.set_xlabel('Jenis Hari (Tidak = Akhir Pekan, Ya = Hari Kerja)', fontsize=12)
ax.set_ylabel('Jumlah Pengguna', fontsize=12)
ax.set_title('Pengguna Sepeda: Hari Kerja vs Akhir Pekan', fontsize=14)
ax.set_xticks(index)
ax.set_xticklabels(['Tidak (Akhir Pekan)', 'Ya (Hari Kerja)'], fontsize=11)
ax.legend(title='Jenis Pengguna', fontsize=10, title_fontsize=11)

plt.tight_layout()
st.pyplot(fig)

st.header("Penggunaan Sepeda Sepanjang Hari")

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hour', y='total_users', data=hour_df, label='Total Users', color='#4682B4')
sns.lineplot(x='hour', y='casual_users', data=hour_df, label='Casual Users', color='#90EE90')
sns.lineplot(x='hour', y='registered_users', data=hour_df, label='Registered Users', color='#FFA500')

ax.set_title('Penggunaan Sepeda Sepanjang Hari')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Pengguna')
ax.set_xticks(range(0, 24))
ax.legend()
ax.grid(True)

plt.tight_layout()
st.pyplot(fig)
