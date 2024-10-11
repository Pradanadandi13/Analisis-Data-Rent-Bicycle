
# Belajar Analisis Data dengan Python (Bike Sharing) ✨

Proyek ini adalah dashboard interaktif untuk analisis data penggunaan sepeda (Bike Sharing) yang dikembangkan menggunakan Python dan Streamlit. Dashboard ini memungkinkan pengguna untuk mengeksplorasi data dan mendapatkan wawasan yang bermanfaat melalui visualisasi interaktif.

## Persiapan Lingkungan Pengembangan

Untuk menjalankan proyek ini, Anda bisa menggunakan salah satu pendekatan berikut: **Anaconda** atau **Shell/Terminal**. Ikuti salah satu langkah di bawah ini untuk mempersiapkan lingkungan pengembangan.

### Setup Environment - Anaconda

1. **Buat Environment Baru**:
   ```sh
   conda create --name bike-sharing-env python=3.9
   ```

2. **Aktifkan Environment**:
   ```sh
   conda activate bike-sharing-env
   ```

3. **Install Dependensi**:
   Install semua dependensi yang diperlukan dari file `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

### Setup Environment - Shell/Terminal

1. **Buat Direktori Proyek**:
   ```sh
   mkdir bike_sharing_analysis
   cd bike_sharing_analysis
   ```

2. **Install Pipenv**:
   Proyek ini menggunakan `pipenv` untuk mengelola virtual environment.

   - **Install Pipenv** (jika belum terinstall):
     ```sh
     pip install pipenv
     ```

3. **Buat dan Aktifkan Environment**:
   ```sh
   pipenv install
   pipenv shell
   ```

4. **Install Dependensi**:
   Install semua dependensi dari file `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi Streamlit

Setelah setup environment selesai, Anda dapat menjalankan aplikasi Streamlit menggunakan perintah berikut:

```sh
streamlit run dashboard/dashboard.py
```

Perintah di atas akan membuka dashboard di browser Anda, yang memungkinkan Anda untuk mengeksplorasi data secara interaktif.

## Struktur Direktori

Proyek ini memiliki struktur direktori sebagai berikut:

```
bike_sharing_analysis/
│
├── dashboard/                 # Folder berisi script untuk Streamlit dashboard
│   ├── dashboard.py           # Script utama untuk menjalankan aplikasi Streamlit
│   ├── data_day.csv           # Dataset harian yang telah diproses
│   └── hour_data.csv          # Dataset per jam yang telah diproses
├── data/                      # Folder berisi dataset asli
│   ├── data1.csv              # Dataset day
│   └── data2.csv              # Dataset hour
├── notebook.ipynb             # Jupyter Notebook untuk analisis data eksploratif
├── Belajar Analisis Data dengan Python (Bike Sharing).README.md  # Panduan proyek ini
├── requirements.txt           # File berisi daftar dependensi yang diperlukan untuk proyek
└── url.txt                    # File berisi informasi URL terkait proyek
```

## Dependensi

Proyek ini memerlukan beberapa library Python yang tercantum dalam file `requirements.txt`. Pastikan untuk menginstall semua dependensi tersebut agar aplikasi berjalan dengan baik.

Berikut adalah daftar dependensi yang diperlukan, yang dapat Anda temukan di dalam `requirements.txt`:

```
- pandas
- numpy
- matplotlib
- seaborn
- streamlit
```

## Fitur Dashboard

Dashboard ini memungkinkan pengguna untuk:
1. **Visualisasi Penggunaan Sepeda Berdasarkan Musim dan Bulan**: Mengetahui pola penggunaan sepeda pada berbagai musim dan bulan.
2. **Analisis Cuaca**: Mengamati bagaimana kondisi cuaca mempengaruhi jumlah pengguna sepeda (kasual maupun terdaftar).
3. **Pola Penggunaan Sepeda pada Hari Kerja vs Akhir Pekan**: Melihat perbedaan pola penggunaan antara hari kerja dan akhir pekan.
4. **Penggunaan Sepeda Sepanjang Hari**: Memvisualisasikan jumlah pengguna berdasarkan jam dalam sehari.

## Panduan Menjalankan Analisis Data di Jupyter Notebook

Selain dashboard, proyek ini juga berisi file `notebook.ipynb`, yang berisi analisis data eksploratif (Exploratory Data Analysis/EDA) pada dataset penggunaan sepeda. Untuk menjalankannya, Anda bisa menggunakan Jupyter Notebook:

1. **Jalankan Jupyter Notebook**:
   ```sh
   jupyter notebook notebook.ipynb
   ```

2. **Eksplorasi Data**:
   Gunakan notebook untuk eksplorasi data lebih mendalam, melihat statistik deskriptif, dan memvisualisasikan data menggunakan `matplotlib` dan `seaborn`.
