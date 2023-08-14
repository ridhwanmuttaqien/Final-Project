Ridhwan Muttaqien - HCK06

Deployment Link : https://huggingface.co/spaces/Ridhwanm/final_project

Loan Risk Prediction

Bidang perbankan sebagaimana bidang bisnis lainnya berusaha untuk menambah pemasukan dan menekan pengeluaran. Salah satu cara menambah pemasukan adalah dengan memberikan tawaran pinjaman pada masyarakat. Tetapi selain berpotensi menambah pemasukan, pinjaman tetap mengandung resiko yaitu gagal bayar atau tidak lancarnya pembayaran dari customer. Untuk mengatasi hal tersebut pihak bank perlu melakukan screening pada customer yang mengajukan pinjaman. Screening hanya sebagai penyaringan awal oleh pihak bank agar terhindar dari memberikan pinjaman pada customer yang beresiko. Penentuan pinjaman apakah dia akan beresiko atau tidak bisa dibantu menggunakan sebuah permodelan machine learning berdasarkan data historis yang dimiliki pihak bank.

Data yang digunakan adalah data open source dari kaggle dan berisi data bank di India. Dataset berisi customer ID, data demografi customer (umur, status perkawinan, domisili,dan pekerjaan), status kepemilikan aset, jumlah pendapatan, status resiko pinjaman. Digunakan juga data populasi di India.

Dari dataset dengan menganalisa kolom state dapat disimpulkan:
- secara umum di semua state, jumlah customer dengan pinjaman tidak beresiko jauh lebih banyak dari yang beresiko. Ini adalah salah satu sebab state tidak dimasukkan sebagai feature untuk memprediksi status resiko. Sebab kita tidak mau kehilangan potensi customer yang besar.

- Uttar Pradesh adalah state dengan jumlah customer dengan pinjaman beresiko terbanyak tapi ini sangat wajar karena Uttar Pradesh juga menjadi state dengan jumlah customer terbanyak bahkan jika dilihat dari data populasi Uttar Pradesh juga state dengan jumlah populasi terbanyak.

- State Maharashtra, Andhra Pradesh, dan West Bengal dimana ketiganya memiliki jumlah customer dengan pinjaman beresiko yang berdekatan sedangkan memiliki jumlah customer yang berbeda-beda. Andhra Pradesh dan West Bengal memiliki tingkat pinjaman beresiko yang lebih besar jika dibandingkan dengan Maharashtra padahal jumlah customer di kedua state tersebut lebih sedikit dari Maharashtra. Maka ini bisa jadi perhatian bagi pihak bank ketika akan memberikan pinjaman pada customer di Andhra Pradesh dan West Bengal. 

- State Karnataka juga terlihat menarik dimana Karnataka menempati urutan ke-8 dari jumlah customer tetapi jumlah pinjaman beresiko nya menempati urutan ke-11. Bisa disimpulkan Kamataka menjadi state yang cukup aman untuk diberikan pinjaman.

- Jika mengacu pada data populasi, Odisha termasuk 15 state dengan jumlah populasi terbanyak tapi tidak termasuk dalam jumlah customer terbanyak. Maka ini bisa menjadi saran bagi tim marketing untuk memperluas customer di Odisha

- State Haryana tidak termasuk state dengan jumlah populasi terbanyak tapi termasuk ke dalam 15 teratas state dengan jumlah customer terbanyak. Maka customer di Haryana bisa diberikan promo untuk menjaga loyalitas customer di Haryana

- State Manipur dengan income rata-rata tertinggi ternyata tidak termasuk 15 besar state dengan jumlah customer terbanyak. Ini disebabkan karena Manipur memiliki jumlah populasi yang juga tidak banyak. Tapi ini juga perlu jadi perhatian jika pihak bank ingi memperluas pasar

Dari kolom umur terlihat bank ini memiliki penerimaan yang cukup baik pada tiap jenjang umur dibuktikan dari jumlah yang hampir rata di tiap jenjang umur. Terlihat juga ada 33.86% customer bank yang ada di usia pensiun di India yaitu di atas 60 tahun. Pada customer ini bisa ditawarkan produk asuransi jiwa atau kesehatan.

Dari kolom profesi, customer paling banyak bekerja di bidang engineering dan teknologi. Untuk itu bisa diberikan promo potongan harga untuk pembelian barang-barang terkait teknologi contohnya laptop. Atau bisa juga potongan harga jika mengikuti pelatihan di bidang engineering dan teknologi jika melakukan pembayaran dari bank kita.

Model dibuat dengan semua kolom sebagai feature kecuali customer id, city, dan state. Kemudian feature dilakukan preprocessing sehingga semua kolom terepresentasi ke dalam numerik. Disini digunakan library pycaret untuk mencari algoritma mana yang menghasilkan performa terbaik. Semua algoritma tersebut dengan default parameter. Dari hasil pycaret didapatkan Random forest classifier sebagai algoritma terbaik dengan performa 55.47%. Digunakan f1 score metrics evaluasi karena kita sama-sama tidak menginginkan kedua kondisi berikut yaitu customer yang tidak beresiko diprediksi beresiko atau customer beresiko diprediksi tidak beresiko.
