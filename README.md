# MocaScraper
![image](https://github.com/HilmiStd/MocaScraper/assets/147703897/4e0a72a1-563e-40d9-9e8f-e82db19a8d67)
MocaScraper adalah sebuah aplikasi terminal yang digunakan untuk melakukan scraping proses presensi dari web elearning moca. Pastikan untuk menggunakan dengan bijak dan tidak melakukan spam.

## Instalasi
1. Clone repository ini ke dalam lokal komputer Anda:

    ```bash
    git clone https://github.com/HilmiStd/MocaScraper.git
    ```

2. Masuk ke direktori MocaScraper:

    ```bash
    cd MocaScraper
    ```

3. Install semua dependencies yang diperlukan dengan menjalankan perintah:

    ```bash
    pip install -r requirements.txt
    ```

4. Isi file `config.json` dengan informasi yang sesuai. Untuk `course_id` bisa didapatkan dari link course di moca dan pastikan sudah enroll course tersebut. </br>
![image](https://github.com/HilmiStd/MocaScraper/assets/147703897/5535c292-7788-4b40-a376-cff10cea182b)

## Cara Penggunaan

### 1. Versi CLI

Jalankan perintah berikut untuk menjalankan aplikasi CLI:

```bash
python main.py
```
### 2. Setup Auto Hit
Pastikan Anda memiliki cron atau aplikasi scheduler lain yang dapat digunakan juga jangan lupa untuk menggunakan logging. Masukan command berikut ke scheduler:
```bash
python main.py [id_course]
```
contoh menggunakan cron dan nohup untuk menjalankan setiap hari senin jam 1 siang:
```bash
0 13 * * 1 nohup python main.py 15291 &
```
## Setup telebot notif (BETA)
Fitur ini hanya berfungsi untuk mode `Setup auto hit`. Untuk mengirim notifikasi ke telegram, tambahkan key telegram di `config.json` berisi value dari id bot dan id user telegram formatnya sebagai berikut:
```bash
  "telegram":{
    "bot_id": "isi_id_bot_telegram",
    "user_id": "isi_id_user_telegram"
  }
```

