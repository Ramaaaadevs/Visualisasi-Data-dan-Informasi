# 🚦 Pola Sebaran dan Faktor Risiko Kecelakaan Lalu Lintas di Britania Raya 2024

> Analisis dan visualisasi interaktif data kecelakaan lalu lintas UK tahun 2024 berdasarkan tingkat keparahan, faktor risiko, dan pola temporal — menggunakan Tableau Public & Python.

**Kelompok 11 — Visualisasi Data dan Informasi, Teknik Informatika ITERA 2026**

---

## 🗺️ Dashboard

**Tableau Public →** [Visdat Kelompok 11 — UK Road Accident](https://public.tableau.com/app/profile/diwan.ramadhani.dwi.putra/viz/VisdatKelompok11/Dashboard)

---

## 🖼️ Poster

<img src="assets/Poster Visdat.png" width="600"/>

---

## 📋 Tentang Project

Dataset bersumber dari **UK STATS19 2024** yang diterbitkan secara terbuka oleh [Department for Transport Inggris](https://www.gov.uk/government/statistical-data-sets/road-safety-open-data#complete-dataset). Dataset memuat **101.904 baris** kejadian kecelakaan lalu lintas sepanjang tahun 2024 dengan 44 kolom atribut — mencakup lokasi, waktu, kondisi jalan, kondisi cuaca, tingkat keparahan, dan karakteristik kendaraan.

### ❓ Research Questions

1. Bagaimana **pola sebaran geografis** kecelakaan lalu lintas di Inggris tahun 2024 berdasarkan tingkat keparahan?
2. **Faktor risiko** apa saja yang berkaitan dengan tingkat keparahan kecelakaan, khususnya batas kecepatan dan kondisi wilayah urban/rural?
3. Bagaimana **pola temporal** kejadian kecelakaan berdasarkan hari dan waktu dalam sehari?

### 🎯 Research Objectives

- Memetakan sebaran geografis kecelakaan per wilayah county di Inggris menggunakan choropleth map
- Mengidentifikasi faktor risiko keparahan kecelakaan melalui analisis distribusi area dan batas kecepatan
- Menganalisis pola waktu kejadian kecelakaan untuk menemukan periode paling rawan dalam seminggu

---

## 📊 Visualisasi

### 1. Scatter Map — Sebaran Geografis per Titik Kejadian
Menampilkan lokasi kecelakaan secara individual menggunakan koordinat geografis. Kecelakaan terkonsentrasi di wilayah metropolitan seperti **Greater London, West Midlands, dan West Yorkshire**. Warna titik merepresentasikan tingkat keparahan: Fatal (merah gelap), Serious (oranye), dan Slight (merah muda).

### 2. Donut Chart — Distribusi Urban vs Rural
Proporsi kecelakaan didominasi oleh wilayah **Urban (67.469 kejadian)** dibanding Rural (33.621 kejadian), memperkuat bahwa kepadatan lalu lintas perkotaan merupakan faktor risiko utama.

### 3. Horizontal Bar Chart — Frekuensi per Batas Kecepatan
Jalan dengan batas kecepatan **30 mph** mencatat angka kecelakaan tertinggi dengan **50.257 kejadian** — mengindikasikan jalanan padat berkecepatan menengah-rendah memiliki risiko insiden lebih tinggi dibanding jalan berkecepatan tinggi.

### 4. Temporal Heatmap — Pola Waktu Kecelakaan
Konsentrasi intensitas tertinggi terjadi pada periode **Siang/Sore hari di hari kerja (Senin–Jumat)**, bertepatan dengan jam komuter — menunjukkan tingginya paparan risiko akibat kelelahan dan volume kendaraan yang memuncak.

---

## 🔧 Preprocessing

Data melalui 5 tahap preprocessing:

1. **Feature Selection** — dari 44 atribut dipilih 9 atribut paling relevan
2. **Variable Transformation** — konversi kode numerik ke label teks (Fatal/Serious/Slight, Urban/Rural, nama hari)
3. **Feature Creation** — ekstraksi kolom `Hour`, `Month`, `time_of_day` menggunakan Excel & Python (pandas)
4. **Discretization** — pengelompokan jam ke 4 kategori: Dini Hari, Pagi, Siang/Sore, Malam
5. **Aggregation** — PivotTable Excel untuk temporal heatmap dan choropleth map

---

## 🛠️ Tools

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Tableau-E97627?style=flat-square&logo=tableau&logoColor=white" />
  <img src="https://img.shields.io/badge/Microsoft%20Excel-217346?style=flat-square&logo=microsoftexcel&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" />
</div>

---

## 📁 Struktur Repo

```
├── data/
│   ├── kecelakaan_kepler.csv     # Dataset subset (longitude, latitude, severity)
│   └── top_wilayah.csv           # Agregasi top wilayah kecelakaan
├── src/
│   └── preprocessing_kecelakaan_uk.py  # Script preprocessing Python
├── assets/
│   └── Poster Visdat.png         # Poster presentasi
├── docs/
│   └── Laporan Visdat.pdf        # Laporan lengkap
├── visdat-kelompok11.twb         # Tableau Workbook
└── README.md
```

---

## 🧾 Kesimpulan

- **Sebaran Geografis** — Kecelakaan terpusat di wilayah metropolitan padat penduduk di Inggris bagian selatan dan tengah
- **Faktor Risiko** — Area Urban dan jalan 30 mph menjadi lokasi kejadian tertinggi; kepadatan interaksi antar kendaraan lebih berisiko dibanding jalan berkecepatan tinggi
- **Pola Waktu** — Insiden memuncak pada Siang–Sore hari kerja, bertepatan dengan jam sibuk komuter
- **Rekomendasi** — Peningkatan pengawasan pada jam sibuk di area perkotaan dengan batas kecepatan 30 mph

---

## 👥 Tim

| Nama | NIM |
|------|-----|
| Abel Fortino | 123140111 |
| Diwan Ramadhani Dwi Putra | 123140116 |
| M. Hafizurrahman Akbar | 123140123 |
| M. Gymnastiar Syahputra | 123140135 |

---

## 📚 Referensi

- World Health Organization. (2018). *Global status report on road safety 2018.*
- Department for Transport. (2024). *Road safety data (STATS19).* [data.gov.uk](https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data)
