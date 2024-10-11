
# Belajar Analisis Data dengan Streamlit

Proyek ini merupakan sebuah aplikasi dashboard interaktif yang dibangun menggunakan Streamlit untuk menganalisis data pemakaian sepeda. Aplikasi ini memberikan visualisasi pengguna sepeda berdasarkan musim, kondisi cuaca, dan waktu.

## Struktur Proyek

Struktur folder proyek ini adalah sebagai berikut:

```
.
├── dashboard/
│   ├── bike_day.csv
│   ├── bike_hour.csv
│   └── dashboard.py
├── data/
│   ├── data1.csv
│   ├── data2.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

- **dashboard/**: Folder yang berisi file aplikasi Streamlit dan dataset terkait analisis pemakaian sepeda.
    - `bike_day.csv`: Data harian pemakaian sepeda.
    - `bike_hour.csv`: Data per jam pemakaian sepeda.
    - `dashboard.py`: File aplikasi Streamlit untuk menampilkan dashboard analisis.
- **data/**: Folder yang berisi dataset tambahan yang digunakan untuk analisis lebih lanjut (misalnya di dalam notebook).
    - `data1.csv`: Dataset tambahan 1.
    - `data2.csv`: Dataset tambahan 2.
- **notebook.ipynb**: Jupyter Notebook untuk analisis lebih lanjut atau eksplorasi data.
- **requirements.txt**: Daftar pustaka Python yang dibutuhkan untuk menjalankan aplikasi.
- **url.txt**: File yang mungkin berisi URL atau referensi terkait data atau proyek ini.

## Cara Menjalankan Aplikasi

### 1. Clone Repository

Clone repository ini ke mesin lokal kamu:

```bash
git clone https://github.com/Pradanadandi13/Analisis-Data-Rent-Bicycle.git
cd Analisis-Data-Rent-Bicycle
```

### 2. Install Dependencies

Buat virtual environment (opsional tapi disarankan) dan install dependencies:

```bash
# Buat virtual environment
python -m venv env

# Aktifkan virtual environment (Windows)
.\env\Scriptsctivate

# Aktifkan virtual environment (macOS/Linux)
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi Streamlit

Setelah dependencies terinstall, jalankan aplikasi dengan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

Aplikasi akan berjalan di browser di `http://localhost:8501`.

## Dataset

- **bike_day.csv**: Data harian yang berisi informasi mengenai total pengguna sepeda per hari, termasuk pengguna terdaftar dan pengguna kasual.
- **bike_hour.csv**: Data per jam yang berisi informasi serupa namun dalam skala jam.
- **data1.csv** dan **data2.csv**: Dataset tambahan yang digunakan untuk analisis lebih lanjut di notebook.

## Notebook

Jika kamu ingin melakukan eksplorasi data atau analisis tambahan, kamu dapat membuka file `notebook.ipynb` menggunakan Jupyter Notebook atau JupyterLab.

### Menjalankan Jupyter Notebook:

```bash
jupyter notebook
```

## Deployment

Untuk melakukan deploy aplikasi ini ke **Streamlit Cloud**:

1. Fork repository ini ke GitHub kamu.
2. Masuk ke [Streamlit Cloud](https://share.streamlit.io/).
3. Pilih repository dan branch tempat kode aplikasi berada.
4. Pilih file utama `dashboard/dashboard.py` untuk dijalankan.
5. Klik **Deploy**.

## Lisensi

Proyek ini menggunakan lisensi MIT. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.
