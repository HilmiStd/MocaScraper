# MocaScraper
![image](https://github.com/HilmiStd/MocaScraper/assets/147703897/a5f4206b-0db2-4f7b-8207-7bf209d4b420)
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
![image](https://github.com/HilmiStd/MocaScraper/assets/147703897/70514c06-fa9f-427a-a278-891f7a0eda2f)

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
