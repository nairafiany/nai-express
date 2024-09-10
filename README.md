Link menuju aplikasi PWS yang sudah di-deploy : http://naira-shafiqa-naiexpress1.pbp.cs.ui.ac.id/

# Jawaban Pertanyaan Tugas 2

## Pertanyaan 1

_Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)._

Jawaban :

### Step 1: Setup Proyek dan Lingkungan Django

Pada tahap ini, saya menyiapkan _environment_ untuk proyek Django agar dapat berjalan dengan baik.

1. **Membuat Direktori Proyek**  
   Saya akan membuat direktori khusus untuk proyek ini dengan nama direktori `nai-express` dan mengaktifkan virtual environment untuk memastikan bahwa semua dependensi proyek tidak bercampur dengan proyek lain.

   ```bash
   mkdir nai-express
   cd nai-express
   ```

2. **Aktifkan Virtual Environment**  
   Saya membuat virtual environment agar proyek ini terisolasi dari dependensi global.

   ```bash
   python -m venv env
   source env/bin/activate  # MacOS/Linux
   env\Scripts\activate     # Windows
   ```

3. **Instalasi Django dan Dependencies**  
   Setelah virtual environment diaktifkan, saya menginstal Django dan dependensi lain yang diperlukan dengan menjalankan perintah:

   ```bash
   pip install django
   ```

4. **Membuat `requirements.txt`**  
   File `requirements.txt` akan mencatat semua dependensi proyek yang diinstal untuk memudahkan pengembang lain atau deployment proyek:

   ```bash
    pip install -r requirements.txt
   ```

5. **Membuat Proyek Django**  
   Dengan menjalankan perintah berikut, saya membuat proyek Django baru:

   ```bash
   django-admin startproject nai_project .
   ```

6. **Konfigurasi `settings.py`**  
   Saya perlu menambahkan `ALLOWED_HOSTS` di `settings.py` agar proyek bisa berjalan di `localhost` dan domain yang ditentukan situs PBP:

   ```python
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "naira-shafiqa-naiexpress.pbp.cs.ui.ac.id"]
   ```

### Step 2: Membuat Aplikasi dan Konfigurasi (MTV) Proyek

Setelah proyek Django dibuat, saya akan menambahkan aplikasi bernama `main` yang akan menangani logika utama dari proyek.

1. **Membuat Aplikasi**  
   Perintah ini akan membuat aplikasi bernama `main` di dalam proyek:

   ```bash
   python manage.py startapp main
   ```

2. **Menambahkan Aplikasi ke `settings.py`**  
   Agar aplikasi `main` dikenali oleh proyek, saya menambahkannya di dalam daftar `INSTALLED_APPS` yang ada di `settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'main',
   ]
   ```

3. **Menjalankan Proyek Secara Lokal**  
   Untuk melihat apakah proyek dan aplikasi sudah berfungsi dengan baik, saya menjalankan server Django secara lokal:

   ```bash
   python manage.py runserver
   ```

4. **Membuat Template HTML**
   Saya membuat direktori templates di dalam aplikasi main dan menambahkan file main.html yang berisi template variables untuk menampilkan produk.

   Saya menambahkan CSS untuk memberikan style pada halaman agar lebih menarik.

5. **Modifikasi Model**
   Saya mengubah model `Product` di dalam `models.py` agar sesuai dengan spesifikasi tugas :

   ```bash
   class Product(models.Model):
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
      image = models.CharField(max_length=255, default='images/default.avif')
      availability = models.CharField(max_length=50, default='In Stock')
      stock = models.IntegerField(default=0)
      discount = models.CharField(max_length=20, default='No discount')
   ```

6. **Migrasi Model**
   Setelah melakukan perubahan model, saya menjalankan perintah berikut untuk melakukan migrasi:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Menghubungkan View dengan Template**
   Saya membuat fungsi `show main` di `views.py` untuk menampilkan produk dari database di template.

   ```bash
   from django.shortcuts import render
   from .models import Product


   def show_main(request):
      products = Product.objects.all()
      return render(request, 'main/main.html', {'products': products})
   ```

8. **Mengkonfigurasi Routing URL**
   Saya membuat file `urls.py` di dalam aplikasi `main` untuk mengatur routing halaman.

   ```bash
   from django.urls import path
   from main.views import show_main


   app_name = 'main'


   urlpatterns = [
      path('', show_main, name='show_main'),
   ]
   ```

## Pertanyaan 2

_Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`._

Jawaban :

![alt text](static/images/CLIENT.png)

Diagram ini menunjukkan alur permintaan (request) dari klien dalam aplikasi web berbasis Django. Berikut penjelasan alur secara rinci:

1. **Klien (Browser)**

Klien, biasanya browser, mengirimkan HTTP Request (permintaan HTTP) ke aplikasi web. Permintaan ini bisa berupa permintaan untuk halaman tertentu atau data (misalnya, /products/).

2. **URLs (urls.py)**
   Permintaan pertama kali diteruskan ke file urls.py. File ini berfungsi untuk memetakan URL yang diminta ke fungsi view yang sesuai. Misalnya, jika permintaan adalah untuk halaman /products/, urls.py akan menentukan fungsi view mana yang harus menangani permintaan tersebut.

3. **View (views.py)**
   Setelah permintaan dipetakan, permintaan tersebut diteruskan ke fungsi view yang berada di views.py. Fungsi ini memproses permintaan dan, jika diperlukan, berinteraksi dengan Model (models.py) untuk mengambil atau menulis data.

4. **Model (models.py)**
   berperan sebagai representasi struktur basis data. View dapat mengambil data yang diperlukan (misalnya, daftar produk atau detail pengguna) atau memperbarui basis data melalui model.
   HTML Template: Setelah data diproses, view akan meneruskannya ke template HTML yang berfungsi untuk merender (menyusun) halaman dengan konten dinamis yang sesuai.

5. **HTTP Response**
   Template HTML yang sudah dirender dikembalikan sebagai HTTP Response (respons HTTP), yang kemudian dikirim kembali ke browser klien untuk ditampilkan.

Alur ini memastikan bahwa permintaan klien ditangani secara efisien oleh setiap komponen Django. URLs memetakan permintaan, views memprosesnya, models berinteraksi dengan basis data, dan template merender tampilan akhir yang dikirim kembali kepada klien.

Referensi : https://learnbatta.com/blog/understanding-request-response-lifecycle-in-django-29/

## Pertanyaan 3

_Jelaskan fungsi git dalam pengembangan perangkat lunak!_

Jawaban :

Git adalah sistem kontrol versi modern yang paling banyak digunakan di dunia saat ini. Git memainkan peran penting dalam pengembangan perangkat lunak dengan menyediakan arsitektur terdistribusi yang memungkinkan setiap salinan kode pengembang juga bertindak sebagai repository penuh yang mencakup seluruh riwayat perubahan.

Berikut adalah beberapa fungsi utama Git dalam pengembangan perangkat lunak:

1. Versi Kontrol Terdistribusi (DVCS):

Git memungkinkan setiap pengembang memiliki salinan lengkap dari riwayat proyek, bukan hanya satu server pusat. Ini membuat kolaborasi lebih fleksibel karena pengembang dapat bekerja secara offline dan mengunggah perubahan mereka nanti.

2. Kinerja Tinggi:

Git dirancang untuk memberikan kinerja yang optimal. Operasi seperti commit, branching, dan merging dilakukan dengan cepat karena Git menggunakan algoritma yang dioptimalkan untuk menangani pohon file kode sumber.

3. Keamanan:

Git menjamin integritas kode dan riwayat perubahan dengan menggunakan algoritma hashing kriptografi (SHA1). Ini memastikan bahwa semua perubahan dapat dilacak secara aman dan terhindar dari modifikasi berbahaya atau tak terduga.

4. Fleksibilitas:

Git sangat fleksibel dalam mendukung berbagai alur kerja pengembangan yang tidak linear, proyek besar atau kecil, dan kompatibel dengan banyak sistem dan protokol. Branching dan tagging merupakan fitur penting dalam Git yang memungkinkan tim melacak versi perangkat lunak dengan lebih efektif.

Git memberikan pengembang perangkat lunak alat yang kuat untuk mengelola perubahan kode secara efisien, aman, dan fleksibel, yang membuatnya menjadi pilihan utama di antara tim pengembang di seluruh dunia.

Referensi : https://www.atlassian.com/git/tutorials/what-is-git

## Pertanyaan 4

_Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?_

Jawaban :

1. **Menggunakan Bahasa Python yang Populer dan Mudah Dipelajari**
   Django dibangun dengan Python, salah satu bahasa pemrograman paling populer dan efektif. Python dikenal mudah dipelajari dan digunakan, sehingga Django sangat cocok untuk pemula dalam pengembangan perangkat lunak.

2. **Fitur Bawaan yang Lengkap**
   Django hadir dengan berbagai fitur bawaan seperti ORM, area admin, migrasi database, dan autentikasi. Ini memungkinkan pengembang langsung fokus pada pengembangan aplikasi tanpa harus menyiapkan banyak hal dari awal.

3. **Modular dan Reusable**
   Django menerapkan konsep aplikasi yang dapat digunakan kembali, sehingga kode dapat dimodularisasi dengan baik. Ini membuat pengembangan proyek lebih efisien dan mudah diperluas seiring waktu.

4. **Komunitas Besar dan Dokumentasi Lengkap**
   Django memiliki komunitas besar dan aktif, ditambah dengan dokumentasi yang sangat lengkap. Banyak sumber daya yang tersedia untuk membantu ketika menghadapi kesulitan, baik melalui komunitas maupun dokumentasi resmi.

5. **Mempermudah Pembelajaran Framework Lain**
   Belajar Django memberikan fondasi kuat dalam pengembangan web, sehingga lebih mudah untuk mempelajari framework lain. Konsep yang dipelajari di Django dapat diterapkan pada banyak framework lain dalam pengembangan perangkat lunak.

Referensi : https://dev.to/msnmongare/mastering-django-now-a-comprehensive-guide-from-beginner-to-advanced-4b2d

## Pertanyaan 5

_Mengapa model pada Django disebut sebagai ORM?_

Jawaban :

Django Web Framework sudah menyertakan **Object-Relational Mapping (ORM)**, yang memungkinkan pengguna berinteraksi dengan data dari berbagai relational databases dengan cara yang lebih sederhana dan efisien. Django ORM memungkinkan untuk menambah (add), menghapus (delete), memodifikasi (modify), dan melakukan query terhadap objek, semuanya melalui antarmuka API yang disebut ORM.

ORM itu sendiri adalah singkatan dari Object-Relational Mapping, yaitu sebuah teknik yang memetakan model-model objek dalam kode Python ke tabel-tabel dalam basis data relasional. Hal ini berarti, data dapat diolah menggunakan objek-objek Python tanpa perlu menulis perintah SQL secara manual. Misalnya, ketika kita ingin mengambil data dari tabel, cukup lakukan query menggunakan Python, dan ORM akan menerjemahkannya menjadi perintah SQL yang sesuai.

Referensi : https://www.scaler.com/topics/django/django-orm/
