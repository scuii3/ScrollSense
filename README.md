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
