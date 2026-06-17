# Laporan Proyek Machine Learning - ScrollSense

## Prediksi Risiko Ketergantungan Media Sosial Berdasarkan Pola Aktivitas Digital Pengguna

Nama: Try Suci Wulandari

NIM: 2330511099

## Project Overview

Perkembangan teknologi digital dan media sosial telah mengubah cara mahasiswa berinteraksi, memperoleh informasi, dan menghabiskan waktu sehari-hari. Platform seperti Instagram, TikTok, Twitter, dan YouTube menjadi bagian penting dalam kehidupan mahasiswa. Namun, penggunaan media sosial yang berlebihan dapat menimbulkan berbagai dampak negatif, seperti penurunan kualitas tidur, gangguan kesehatan mental, konflik sosial, hingga menurunnya performa akademik.

Ketergantungan media sosial merupakan kondisi ketika seseorang mengalami kesulitan mengontrol penggunaan media sosial sehingga aktivitas sehari-hari menjadi terganggu. Oleh karena itu, diperlukan suatu sistem yang mampu mengidentifikasi tingkat risiko ketergantungan media sosial sejak dini.

Pada proyek ini dibangun model machine learning untuk memprediksi tingkat risiko ketergantungan media sosial berdasarkan pola aktivitas digital pengguna. Model yang dihasilkan diharapkan dapat membantu mengidentifikasi pengguna yang berpotensi mengalami ketergantungan media sosial sehingga dapat dilakukan tindakan pencegahan lebih awal.

## Business Understanding

### Problem Statements

1. Bagaimana membangun model machine learning yang mampu memprediksi tingkat risiko ketergantungan media sosial berdasarkan karakteristik dan aktivitas digital pengguna?

2. Faktor apa saja yang paling berpengaruh terhadap tingkat risiko ketergantungan media sosial?

### Goals

1. Mengembangkan model klasifikasi untuk memprediksi tingkat risiko ketergantungan media sosial berdasarkan pola aktivitas digital pengguna.

2. Mengidentifikasi fitur-fitur yang memiliki pengaruh terbesar terhadap tingkat risiko ketergantungan media sosial.

### Solution Statements

Untuk menyelesaikan permasalahan tersebut, dilakukan eksperimen menggunakan beberapa algoritma klasifikasi, yaitu:

- Decision Tree
- Random Forest
- Logistic Regression

Performa setiap model dievaluasi menggunakan metrik Accuracy. Model dengan performa terbaik dipilih sebagai model akhir dan divalidasi menggunakan Cross Validation untuk memastikan kemampuan generalisasi model terhadap data baru.


## Data Understanding

Dataset yang digunakan dalam proyek ini adalah **Students Social Media Addiction Dataset** yang berisi informasi mengenai karakteristik mahasiswa dan pola penggunaan media sosial. Dataset ini digunakan untuk memprediksi tingkat risiko ketergantungan media sosial berdasarkan aktivitas digital pengguna.

### Jumlah Data

Dataset terdiri dari:

- Jumlah data: 705 baris
- Jumlah atribut: 13 kolom

### Deskripsi Fitur

| Fitur | Keterangan |
|---------|---------|
| Student_ID | Identitas unik mahasiswa |
| Age | Usia mahasiswa |
| Gender | Jenis kelamin |
| Academic_Level | Jenjang pendidikan |
| Country | Negara asal |
| Avg_Daily_Usage_Hours | Rata-rata penggunaan media sosial per hari |
| Most_Used_Platform | Platform media sosial yang paling sering digunakan |
| Affects_Academic_Performance | Pengaruh media sosial terhadap performa akademik |
| Sleep_Hours_Per_Night | Rata-rata jam tidur per malam |
| Mental_Health_Score | Skor kesehatan mental |
| Relationship_Status | Status hubungan |
| Conflicts_Over_Social_Media | Jumlah konflik yang disebabkan media sosial |
| Addicted_Score | Skor tingkat ketergantungan media sosial |

### Kondisi Dataset

Berdasarkan proses eksplorasi data diperoleh:

- Tidak terdapat missing value pada dataset.
- Tidak terdapat data duplikat.
- Dataset terdiri dari data numerik dan kategorikal.
- Dataset memiliki 705 data yang siap digunakan dalam proses pemodelan.

### Target Variable

Dataset asli tidak memiliki label tingkat risiko ketergantungan media sosial. Oleh karena itu dilakukan proses Feature Engineering untuk membentuk variabel target baru yaitu Risk_Level berdasarkan nilai Addicted_Score.

Kategori risiko dibentuk menggunakan aturan berikut:

- Rendah : Addicted_Score ≤ 4
- Sedang : Addicted_Score > 4 dan ≤ 7
- Tinggi : Addicted_Score > 7

Variabel Risk_Level kemudian digunakan sebagai target pada proses klasifikasi machine learning.

## Exploratory Data Analysis (EDA)

Pada tahap Exploratory Data Analysis (EDA), dilakukan analisis untuk memahami karakteristik data dan hubungan antar variabel yang digunakan dalam proses pemodelan.

### Distribusi Tingkat Risiko

Visualisasi distribusi Risk_Level dilakukan untuk melihat persebaran jumlah data pada masing-masing kategori risiko ketergantungan media sosial, yaitu Rendah, Sedang, dan Tinggi.

### Distribusi Durasi Penggunaan Media Sosial

Distribusi Avg_Daily_Usage_Hours dianalisis menggunakan histogram untuk mengetahui pola penggunaan media sosial mahasiswa setiap harinya.

### Distribusi Mental Health Score

Analisis terhadap Mental_Health_Score dilakukan untuk melihat persebaran kondisi kesehatan mental responden pada dataset.

### Analisis Korelasi

Heatmap korelasi digunakan untuk melihat hubungan antar fitur numerik, yaitu:

- Age
- Avg_Daily_Usage_Hours
- Sleep_Hours_Per_Night
- Mental_Health_Score
- Addicted_Score

Hasil analisis korelasi membantu memahami fitur-fitur yang memiliki hubungan terhadap tingkat ketergantungan media sosial.

## Data Preparation

Tahap Data Preparation dilakukan untuk mempersiapkan data sebelum digunakan dalam proses pelatihan model machine learning.

### Feature Engineering

Karena dataset asli tidak memiliki label tingkat risiko ketergantungan media sosial, dibuat variabel target baru yaitu Risk_Level berdasarkan nilai Addicted_Score dengan kategori:

- Rendah : Addicted_Score ≤ 4
- Sedang : Addicted_Score > 4 dan ≤ 7
- Tinggi : Addicted_Score > 7

### Pemisahan Fitur dan Target

Fitur (X) dan target (y) dipisahkan untuk keperluan proses pelatihan model.

Kolom yang tidak digunakan dalam pemodelan:

- Student_ID
- Addicted_Score
- Risk_Level (sebagai target)

### Encoding Data Kategorikal

Data kategorikal dikonversi menjadi data numerik menggunakan One Hot Encoding melalui fungsi `pd.get_dummies()` agar dapat diproses oleh algoritma machine learning.

### Train Test Split

Dataset dibagi menjadi data latih dan data uji menggunakan rasio:

- Data latih : 80%
- Data uji : 20%

Pembagian dilakukan menggunakan `train_test_split()` dengan parameter:

- test_size = 0.2
- random_state = 42
- stratify = y

Penggunaan stratify bertujuan untuk menjaga proporsi kelas pada data latih dan data uji tetap seimbang.

## Modeling

Pada tahap modeling dilakukan pelatihan dan perbandingan beberapa algoritma klasifikasi untuk menentukan model terbaik dalam memprediksi tingkat risiko ketergantungan media sosial.

Algoritma yang digunakan yaitu:

### 1. Decision Tree

Decision Tree merupakan algoritma klasifikasi yang membangun struktur pohon keputusan berdasarkan fitur-fitur pada dataset. Algoritma ini dipilih karena mudah diinterpretasikan dan sering digunakan sebagai baseline model klasifikasi.

### 2. Random Forest

Random Forest merupakan pengembangan dari Decision Tree yang menggunakan banyak pohon keputusan (ensemble learning). Algoritma ini mampu mengurangi overfitting dan menghasilkan performa yang lebih stabil.

### 3. Logistic Regression

Logistic Regression digunakan sebagai model pembanding karena merupakan algoritma klasifikasi yang sederhana, cepat, dan umum digunakan pada berbagai permasalahan klasifikasi.

### Hasil Perbandingan Model

| Model | Accuracy |
|---------|---------|
| Decision Tree | 98.58% |
| Random Forest | 98.58% |
| Logistic Regression | 97.87% |

Berdasarkan hasil evaluasi, Random Forest dipilih sebagai model terbaik karena memiliki akurasi tertinggi dan kemampuan generalisasi yang baik pada proses Cross Validation.
