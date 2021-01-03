# Cash Ratio Optimization

## Overview

<span style="font-size: 20px; font-weight: bold">Description</span>

- <span style="font-size: 17px; font-weight: bold">Cash Ratio Optimization</span>
  - Kurangnya efisiensi dalam pengelolaan uang tunai yang beredar di  lapangan, baik di unit kerja, mesin CRM (Cash Recycle Machine) dan mesin ATM (Automated Teller Machine) meningkatkan biaya operasional dan hilangnya potensi penggunaan uang tunai untuk bisnis perbankan BRI.
  - Dalam kategori use case Cash Ratio Optimization, peserta diminta untuk  membangun model berbasiskan Machine Learning yang dapat memberikan  rekomendasi pengelolaan uang tunai dengan akurat sehingga diharapkan mampu menekan biaya operasional dan mengurangi hilangnya kesempatan  bisnis BRI dalam penggunaan uang tunai.

- <span style="font-size: 17px; font-weight: bold">Task</span>

  - Menggunakan data yang ada, prediksi nilai `kas_kantor` dan `kas_echannel` untuk 31 hari kedepan (1 Oktober 2020 - 31 Oktober 2020), dimana nilai `kas_kantor` dan `kas_echannel` untuk waktu `t` didefiniskan sebagai berikut:

  $$
  \begin{align}
  kas\_kantor &= kas\_kantor_{t-1} + cash\_in\_kantor_{t} + cash\_out\_kantor_{t}\\
  kas\_echannel_{t} &= kas\_echannel_{t-1} + cash\_in\_echannel_{t} + cash\_out\_echannel_{t}
  \end{align}
  $$

<span style="font-size: 20px; font-weight: bold">Evaluation Metric</span>

- Metrik evaluasi yang akan digunakan adalah **RMSLE** (Root Mean Squared Logaritmic Error)

- Dimana Rumus dari RMSLE adalah sebagai berikut:
  $$
  RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^n (\log(p_i + 1) - \log(a_i+1))^2 }
  $$

- Keterangan:

  - $$n$$ : banyaknya observasi pada dataset
  - $$p_i$$ : prediksi data ke-i
  - $$a_i$$ : target asli data ke-i

<span style="font-size: 20px; font-weight: bold">Submission</span>

- Submission dari task ini berisi 62 baris dengan 2 kolom `id` dan `value` dengan ketentuan: 
  - 31 Baris pertama berisi prediksi kas_kantor dari tanggal 1-31 Oktober 2020
  - 31 Baris kedua berisi prediksi kas_echannel dari tanggal 1-31 Oktober 2020
- Berikut adalah ilustrasi dari submission yang diminta (contoh submission dapat dilihat pada file **sample_submission.csv**)

| index | value     |
| ----- | --------- |
| 0     | 123123123 |
| 1     | 123123123 |
| 2     | 123123123 |
| …     | …         |
| 59    | 123123123 |
| 60    | 123123123 |
| 61    | 123123123 |

## Data

<span style="font-size: 20px; font-weight: bold">File Descriptions</span>

- Dataset berisi: 
  - train.csv: Data historical yang digunakan untuk melatih model 
  - test.csv - Tanggal prediksi (31 Hari kas kantor, 31 hari kas echannel)
  - data_description.csv -  Deskripsi fields pada `train.csv`
  - sample_submission.csv -  Format submisi. Informasi lebih lengkap dapat dilihat pada overview-evaluation

<span style="font-size: 20px; font-weight: bold">Fields Descriptions</span>

- Deskripsi variable dapat dilihat pada `data_description.csv`
  - cash_in_echannel: Total Kas Masuk pada kas eChannel (ATM dan CRM)
  - cash_out_echannel: Total Kas keluar pada kas eChannel (ATM dan CRM)
  - cash_in_kantor: Total kas masuk pada kas kantor
  - cash_out_kantor: Total kas keluar pada kas kantor
  - cr_ketetapan_total_bkn_sum: Maksimum cash ratio yang dii tetapkan kantor pusat
  - giro: Total simpanan giro
  - deposito: Total simpanan deposito
  - kewajiban_lain: Simpanan selain giro tabungan dan deposito ,salah satunya adalah surat berharga yang diterbitkan
  - tabungan: Total simpanan tabungan
  - rata_dpk_mingguan: rata - rata saldo DPK mingguan
  - kas_kantor: Total Dari kas kantor
  - kas_echannel: Total dari kas eChannel