# 📱 Laporan Proyek Machine Learning: ScrollSense
**Prediksi Risiko Ketergantungan Media Sosial Berdasarkan Pola Aktivitas Digital Pengguna**

> 👤 **Nama:** Try Suci Wulandari  
> 🎓 **NIM:** 2330511099  

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/scuii/ScrollSense)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/scuii3/ScrollSense)

---

## 📖 Project Overview

Perkembangan teknologi digital dan media sosial telah mengubah cara mahasiswa berinteraksi, memperoleh informasi, dan menghabiskan waktu sehari-hari. Platform seperti Instagram, TikTok, Twitter, dan YouTube menjadi bagian penting dalam kehidupan mahasiswa. Namun, penggunaan media sosial yang berlebihan dapat menimbulkan berbagai dampak negatif, seperti:
*   📉 Penurunan kualitas tidur
*   🧠 Gangguan kesehatan mental
*   🗣️ Konflik sosial
*   📚 Menurunnya performa akademik

**Ketergantungan media sosial** merupakan kondisi ketika seseorang mengalami kesulitan mengontrol penggunaan media sosial sehingga aktivitas sehari-hari menjadi terganggu. Oleh karena itu, diperlukan suatu sistem yang mampu mengidentifikasi tingkat risiko ketergantungan ini sejak dini.

> **Tujuan Proyek:** Membangun model *machine learning* untuk memprediksi tingkat risiko ketergantungan media sosial berdasarkan pola aktivitas digital pengguna, sehingga tindakan pencegahan dapat dilakukan lebih awal.

---

## 🎯 Business Understanding

### ❓ Problem Statements
1. Bagaimana membangun model *machine learning* yang mampu memprediksi tingkat risiko ketergantungan media sosial berdasarkan karakteristik dan aktivitas digital pengguna?
2. Faktor apa saja yang paling berpengaruh terhadap tingkat risiko ketergantungan media sosial?

### 💡 Goals
1. Mengembangkan model klasifikasi untuk memprediksi tingkat risiko ketergantungan media sosial berdasarkan pola aktivitas digital pengguna.
2. Mengidentifikasi fitur-fitur yang memiliki pengaruh terbesar terhadap tingkat risiko tersebut.

### 🛠️ Solution Statements
Eksperimen dilakukan menggunakan tiga algoritma klasifikasi:
*   🌲 **Decision Tree**
*   🌳 **Random Forest**
*   📈 **Logistic Regression**

*Performa setiap model dievaluasi menggunakan metrik **Accuracy**. Model terbaik divalidasi menggunakan **Cross Validation** untuk memastikan kemampuan generalisasinya terhadap data baru.*

---

## 📊 Data Understanding

Dataset yang digunakan adalah **Students Social Media Addiction Dataset**, berisi informasi mengenai karakteristik mahasiswa dan pola penggunaan media sosial.

*   **Jumlah data:** 705 baris
*   **Jumlah atribut:** 13 kolom
*   **Kondisi Data:** Tidak ada *missing value* maupun data duplikat. Terdiri dari data numerik dan kategorikal yang siap dimodelkan.

### 📋 Deskripsi Fitur

| Fitur | Keterangan |
|---|---|
| `Student_ID` | Identitas unik mahasiswa |
| `Age` | Usia mahasiswa |
| `Gender` | Jenis kelamin |
| `Academic_Level` | Jenjang pendidikan |
| `Country` | Negara asal |
| `Avg_Daily_Usage_Hours` | Rata-rata penggunaan media sosial per hari |
| `Most_Used_Platform` | Platform media sosial yang paling sering digunakan |
| `Affects_Academic_Performance` | Pengaruh media sosial terhadap performa akademik |
| `Sleep_Hours_Per_Night` | Rata-rata jam tidur per malam |
| `Mental_Health_Score` | Skor kesehatan mental |
| `Relationship_Status` | Status hubungan |
| `Conflicts_Over_Social_Media` | Jumlah konflik yang disebabkan media sosial |
| `Addicted_Score` | Skor tingkat ketergantungan media sosial |

### 🎯 Target Variable (Feature Engineering)
Dataset asli tidak memiliki label tingkat risiko. Oleh karena itu, dibuat variabel target baru `Risk_Level` berdasarkan rentang nilai `Addicted_Score`:
*   🟢 **Rendah:** `Addicted_Score` ≤ 4
*   🟡 **Sedang:** `Addicted_Score` > 4 dan ≤ 7
*   🔴 **Tinggi:** `Addicted_Score` > 7

---

## 🔍 Exploratory Data Analysis (EDA)

Fokus analisis pada tahap EDA meliputi:
1.  **Distribusi Tingkat Risiko:** Melihat persebaran jumlah data pada kategori Rendah, Sedang, dan Tinggi.
2.  **Distribusi Durasi Penggunaan:** Menggunakan histogram untuk mengetahui pola penggunaan media sosial harian.
3.  **Distribusi Mental Health Score:** Memetakan kondisi kesehatan mental responden.
4.  **Analisis Korelasi (Heatmap):** Mengidentifikasi hubungan antar fitur numerik (`Age`, `Avg_Daily_Usage_Hours`, `Sleep_Hours_Per_Night`, `Mental_Health_Score`, `Addicted_Score`).

---

## ⚙️ Data Preparation

Langkah-langkah yang dilakukan sebelum pelatihan model:

1.  **Feature Engineering:** Pembuatan target `Risk_Level` sesuai deskripsi sebelumnya.
2.  **Pemisahan Fitur & Target:** Memisahkan fitur (X) dan target (y). Kolom `Student_ID` dan `Addicted_Score` dihapus dari fitur latih.
3.  **Encoding:** Konversi data kategorikal menjadi numerik menggunakan *One Hot Encoding* (`pd.get_dummies()`).
4.  **Train-Test Split:** Membagi dataset dengan rasio **80% latih : 20% uji** (`test_size=0.2`, `random_state=42`). Parameter `stratify=y` digunakan untuk menjaga proporsi kelas tetap seimbang.

---

## 🤖 Modeling

Tiga algoritma dievaluasi untuk menemukan model prediktif terbaik:

1.  **Decision Tree:** Dipilih karena mudah diinterpretasikan dan sangat baik sebagai *baseline*.
2.  **Random Forest:** *Ensemble learning* dari kumpulan pohon keputusan untuk mengurangi *overfitting* dan meningkatkan stabilitas prediksi.
3.  **Logistic Regression:** Model pembanding yang sederhana, cepat, dan umum digunakan.

### 🏆 Hasil Perbandingan Model

| Model | Accuracy |
|---|---|
| **Decision Tree** | 98.58% |
| **Random Forest** | **98.58%** |
| **Logistic Regression** | 97.87% |

> **Kesimpulan Modeling:** **Random Forest** dipilih sebagai model utama karena performa akurasinya yang tinggi dan kemampuannya menjaga kestabilan generalisasi dengan baik (diuji lebih lanjut pada evaluasi).

---

## 📈 Evaluation

### 🔄 Cross Validation (Random Forest)
Validasi silang (*5-fold CV*) dilakukan untuk menguji kestabilan model.

| Fold | Accuracy |
|:---:|:---:|
| 1 | 95.04% |
| 2 | 93.62% |
| 3 | 99.29% |
| 4 | 100.00% |
| 5 | 93.62% |

> ⭐ **Mean Cross Validation Score = 96.31%**  
> *Model terbukti sangat stabil dan mampu melakukan generalisasi dengan baik terhadap data baru.*

### Confusion Matrix
Selain menggunakan metrik akurasi, performa model juga dievaluasi menggunakan *Confusion Matrix* untuk melihat detail klasifikasi pada masing-masing kelas target (Rendah, Sedang, Tinggi). Hasil evaluasi menunjukkan model mampu mengklasifikasikan hampir seluruh data uji dengan benar, dengan tingkat *False Positive* dan *False Negative* yang sangat minim.

### 🔑 Feature Importance
Faktor apa yang paling mendorong risiko ketergantungan? Berikut 10 fitur teratas:

| Fitur | Importance |
|---|---|
| **Conflicts_Over_Social_Media** | **0.278295** |
| **Mental_Health_Score** | **0.193981** |
| **Avg_Daily_Usage_Hours** | **0.109737** |
| **Sleep_Hours_Per_Night** | **0.102536** |
| Affects_Academic_Performance_Yes | 0.036326 |
| Country_Japan | 0.019421 |
| Age | 0.016921 |
| Most_Used_Platform_LinkedIn | 0.015452 |
| Country_Switzerland | 0.014665 |
| Relationship_Status_In Relationship | 0.014253 |

*Insight: Aspek **perilaku penggunaan** (konflik, kesehatan mental, durasi, dan pola tidur) jauh lebih krusial memengaruhi ketergantungan dibandingkan faktor demografis.*

---

## ✅ Kesimpulan

Berdasarkan keseluruhan proses, diperoleh kesimpulan:
*   📌 Dataset mahasiswa (705 baris, 13 atribut) berhasil diolah dengan pembentukan target risiko berdasar *Addicted Score*.
*   📌 **Random Forest** terpilih sebagai model terbaik dengan akurasi pengujian **98.58%** dan rata-rata CV **96.31%**.
*   📌 Tingkat ketergantungan sangat dipengaruhi oleh variabel: **Konflik media sosial, skor kesehatan mental, durasi harian, dan jam tidur**.

---

## 🚀 Deployment

Model telah di-deploy secara interaktif menggunakan framework **Gradio** dan di-hosting melalui **Hugging Face Spaces**. Anda dapat mencoba sistem prediksinya secara langsung melalui tautan berikut:

🔗 **Live App:** [ScrollSense on Hugging Face](https://huggingface.co/spaces/scuii/ScrollSense)  
🔗 **Repository:** [ScrollSense GitHub Repo](https://github.com/scuii3/ScrollSense)

