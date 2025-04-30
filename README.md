# Myanmar Supermarket Sales Analysis

## Repository Outline
1. README.md - Penjelasan mengenai gambaran umum project
2. ddl.sql - File ini berisi query SQL dimulai dari create table sampai copy data mentah ke PostgreSQL
3. data_raw.csv - Data mentah yang didapatkan dari Kaggle
4. data_clean.csv - Hasil dari data cleaning menggunakan python
5. DAG.py - Python script ini berisi code proses pengambilan data dari PostgreSQL, dilanjutkan dengan data cleaning, dan diakhiri dengan pengiriman data ke Elasticsearch untuk selanjutnya divisualisasikan dengan Kibana
6. images - Folder ini berisi hasil exploratory data analysis yang telah dilakukan melalui Kibana

## Problem Background
Saya merupakan bagian dari tim Data Analyst di perusahaan multinasional supermarket yang memiliki cabang di berbagai negara, termasuk Myanmar. Perusahaan ini mengelola beberapa cabang yang tersebar di Myanmar. Untuk mendukung dalam pengambilan keputusan strategis, divisi sales ingin mengetahui analisis performa penjualan dari masing-masing cabang berdasarkan data transaksi penjualan yang telah dikumpulkan.

## Project Output
Output dari project ini yaitu berupa hasil analisis dari performa tiap cabang supermarket. Antara lain seperti cabang mana yang memiliki penjualan tertinggi, mengetahui rata-rata rating pelanggan dari setiap cabang, dan lain-lain. Dengan informasi ini, Divisi Sales dapat mengambil keputusan yang lebih tepat dalam menyusun strategi penjualan dan peningkatan layanan di tiap cabang.

## Data
Dataset berasal dari Kaggle. Dataset berisi informasi detail menganai invoice id (identifier unik dari setiap transaksi penjualan), kategori barang, harga barang, tanggal transaksi, dan lain-lain. Dataset ini memiliki 1000 baris dan 17 kolom.

## Method
Langkah pertama yang dilakukan setelah mendapatkan data dari Kaggle adalah membuat tabel di PostgreSQL dan menyalin dataset ke dalamnya. Selanjutnya, dibuat DAG untuk mengambil data dari PostgreSQL, melakukan proses data cleaning, dan mengimpor data ke Elasticsearch. Terakhir, data divisualisasikan menggunakan Kibana.

## Stacks
Proyek ini dijalankan dengan menggunakan Docker dengan stack utama yang terdiri dari Airflow, PostgreSQL, Elasticsearch, dan Kibana. Untuk menjalankan proyek, diperlukan konfigurasi melalui docker-compose. Bahasa pemrograman yang digunakan adalah Python, dengan library seperti pandas, datetime, psycopg2, dan elasticsearch untuk pipeline di Airflow.