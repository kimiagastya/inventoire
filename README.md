<h3>Tugas 4</h3>
 
 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya? <br>
    Django 'UserCreationForm' adalah form yang bertugas untuk mendaftarkan user baru ke dalam aplikasi kita.<br>
    Kelebihan:
    - UserCreationForm merupakan fitur bawaan Django yang siap digunakan sehingga dapat menghemat waktu dalam pembuatan aplikasi
    - UserCreationForm dapat diimplementasikan pada app yang berbeda dari project sehingga memungkinkan untuk membuat sebuah app yang bertugas sepenuhnya untuk membuat user baru.
    - UserCreationForm mendukung validasi input, seperti kesesuaian ketentuan username dan kesesuaian antara field "Password" dan "Password confirmation".<br>

    Kekurangan:
    - Hanya terdapat field username dan password. Jika ingin menambahkan field baru (seperti e-mail), maka harus memodifikasi UserCreationForm dengan menambahkan field serta validasi inputnya, atau dengan membuat form registrasi dari awal tanpa menggunakan UserCreationForm.

 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>
    Autentikasi merupakan proses untuk memverifikasi identitas user dengan mengecek username dan passwordnya dengan data yang tersimpan di dalam database. Jika verifikasi sukses, maka sistem akan mengonfirmasi keabsahan user. Otorisasi adalah proses menentukan apa saja yang bisa dan tidak bisa dilakukan oleh user dengan mengecek apakah suatu user punya izin untuk mengakses atau melakukan sesuatu. <br>
    Keduanya penting untuk menjaga data sensitif agar tidak dapat dilihat dan disalahgunakan oleh sembarang user. Autentikasi dan otorisasi juga dapat memudahkan kita untuk memantau aktivitas user dengan mengetahui siapa user yang melakukan suatu hal di dalam sistem.

 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna? <br>
    Cookies adalah sebuah text file berukuran kecil yang menyimpan data seperti username dan password yang digunakan untuk mengidentifikasi komputer yang kita gunakan untuk mengakses sebuah website. Django menggunakan cookies sebagai bagian dari session management system. Ketika seorang user melakukan login, Django akan meletakkan session ID cookie pada client dan meletakkan session data pada server. Dengan itu, maka hanya session ID yang dapat dilihat oleh user, sedangkan session data aman tersembunyi di dalam server.

 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? <br>
    Ada beberapa risiko potensial yang harus diwaspadai dalam menggunakan cookies: <br>
    - Jika terjadi penyerangan pada situs web, cookies bisa terekspos oleh penyerang
    - Potensi terjadinya Cross-Site Scripting, yang dapat terjadi ketika script berbahaya dimasukkan ke dalam situs web yang dapat digunakan untuk mencuri informasi sensitif seperti session token
    - Potensi terjadinya session fixation, yaitu serangan yang memungkinkan penyerang membajak sesi user.<br>
    
 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

<h3>Tugas 3</h3>

1. Apa perbedaan antara form POST dan form GET dalam Django? <br>
POST dan GET adalah metode HTTP yang hanya bisa digunakan ketika bekerja dengan forms. Perbedaan antara keduanya adalah sebagai berkut <br>
  * POST digunakan untuk memproses request yang berkaitan dengan perubahan kondisi sistem, contohnya seperti menambahkan atau menghapus data di database. Metode ini juga digunakan untuk form login. Dalam prosesnya, browser akan menggabungkan data form, kemudian data tersebut di-encode, dikirimkan ke server, dan akhirnya menerima response yang diberikan. POST juga men-handle request yang berkaitan dengan password karena data akan di-encode terlebih dahulu sehingga membuat prosesnya menjadi aman.
  * GET digunakan untuk menerima data tanpa membuat perubahan dalam database, seperti web search. Dalam prosesnya, GET akan menggabungkan data menjadi sebuat string yang selanjutnya akan digunakan untuk membuat URL yang berisi address tujuan data serta key dan value nya. GET tidak cocok digunakan untuk men-handle data yang sensitif seperti password karena password akan muncul di URL yang dibuat.
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? <br>
  * XML digunaknan untuk pertukaran data. XML merepresentasikan data dengan menggunakan struktur tag, yang mirip dengan tag HTML. Data yang terdapat di file XML bersifat human-readable dan juga machine-readable.
  * JSON merepresentasikan data sebagai objek dan datanya disimpan dengan pasangan key value.
  * HTML digunakan untuk menampilkan data. HTML tidak cocok untuk pertukaran data antar platform yang berbeda karena HTML menggunakan sintaks dan atribut yang tidak relevan dalam memproses data <br>
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? <br>
  * JSON menyimpan data dalam sebuah array sehingga membuat proses transfer data menjadi lebih sederhana.
  * Sintaks JSON mudah digunakan dan sangat ringan untuk diproses sehingga lebih cepat dalam merespon dan mengeksekusi request client.
  * Semua browser dan sistem operasi kompatibel dengan JSON. Semua browser dan bahasa pemrograman memiliki parser JSON.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
Pertama-tama dimulai dengan membuat file forms.py di dalam direktori main dan menambahkan kode yang terdapat pada tutorial, tetapi isi dari variabel fields diganti dengan '["name", "price", "description"]'. Kemudian file views.py ditambahkan dengan beberapa line import sesuai dengan yang ada pada tutorial. Di file yang sama, saya juga membuat fungsi baru yang bernama 'create_product' dengan parameter 'request' untuk menghasilkan form dan menambahkan data form otomatis setelah datanya di-submit. Selanjutnya, fungsi 'show.main' pada file yang sama ditambahkan variabel 'product' yang di-assign dengan value 'Product.objects.all()' serta menambahkan key ''product'' dengan value product pada variabel dictionary 'context'. Selanjutnya pindah ke file urls.py yang ada pada direktori main untuk menambahkan import fungsi 'create_product' yang telah dibuat sebelumnya dan menambahkan path url ke dalam variabel 'urlpatterns'. Berikutnya dibuat file HTML bernama create_product.html pada direktori main/templates dan diisi dengan kode sesuai dengan tutorial 2. Kemudian untuk menampilkan data dalam tabel, file main.html ditambahkan kode yang mirip dengan tutorial 2 yang dimodifikasi sesuai dengan atribut produk pada tugas 2, yaitu Name, Amount, dan Description. Teks pada button juga diubah menjadi "Add New Car" sesuai dengan tema tugas 2 saya, yaitu Supercar Dealership. <br>
<br>Agar data yang di-submit dapat dikembalikan dalam bentuk XML, JSON, dan berdasarkan ID nya, pertama-tama file views.py di direktori main ditambahkan import 'HttpResponse' dan 'Serializers'. Selanjutnya dibuat variabel 'data' dengan value 'Product.objects.filter(pk=id)'. Kemudian ditambahkan 4 fungsi dengan parameternya masing-masing, yaitu 'show_xml(request)', 'show_json(request)', 'show_xml_by_id(request, id)', dan 'show_json_by_id(request, id)'. Fungsi-fungsi tersebut diisi dengan kode sesuai dengan turtorial 2. Berikutnya pada file 'urls.py' yang terdapat pada direktori main ditambahkan impor 4 fungsi yang telah dibuat sebelumnya, serta ditambahkan path url-nya masing-masing. <br>

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md. <br>
  * HTML
  ![Screenshot Postman HTML1](assets_tugas/POSTMAN_HTML1.png) <br>
  ![Screenshot Postman HTML2](assets_tugas/POSTMAN_HTML2.png) <br>
  ![Screenshot Postman HTML3](assets_tugas/POSTMAN_HTML3.png) <br>

  * JSON
  ![Screenshot Postman JSON](assets_tugas/POSTMAN_JSON.png) <br>
  ![Screenshot Postman JSON1](assets_tugas/POSTMAN_JSON1.png) <br>
  ![Screenshot Postman JSON4](assets_tugas/POSTMAN_JSON4.png) <br>

  * XML
  ![Screenshot Postman XML](assets_tugas/POSTMAN_XML.png) <br>
  ![Screenshot Postman XML1](assets_tugas/POSTMAN_XML1.png) <br>
  ![Screenshot Postman XML4](assets_tugas/POSTMAN_XML4.png) <br>

<h3>Tugas 2</h3>

**Link Adaptable:** https://inventoire.adaptable.app <br>

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
Dalam mengerjakan checklist di atas, saya mulai dengan membuat project Django baru. Pertama-tama, saya membuat direktori utama yang bernama inventoire. Selanjutnya, saya membuat dan mengaktifkan virtual environment melalui command prompt. Kemudian, di dalam direktori utama, saya membuat file `requirements.txt` yang berisi dependencies aplikasi saya dan menginstall semuanya. Lalu, saya sudah bisa membuat project Django baru dengan command `django-admin startproject inventoire`. Variabel `ALLOWED_HOSTS` pada file settings.py saya assign value nya dengan ["*"] untuk keperluan deployment di Adaptable. Sekarang, saya membuat aplikasi main di dalam proyek inventoire dan menambahkan 'main' ke dalam variabel `INSTALLED_APPS` pada file settings.py. File models.py diisi dengan atribut name, amount, dan description dengan menyesuaikan tipenya masing-masing. Fungsi pada file views.py dibuat dengan menambahkan pasangan key nama dan kelas dan value yang berisi nama lengkap dan kelas PBP saya. Routing aplikasi main pada file urls.py dilakukan dengan membuat perintah baru untuk memproses routing ke main. Untuk deployment ke Adaptable dilakukan mirip seperti tutorial, tetapi yang berbeda adalah deployment berjalan dengan lancar, tidak seperti sewaktu tutorial. <br>

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. <br>
![Bagan proses request clinet](Tugas2_BaganRequestClient.png) <br>

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
Virtual environment digunakan untuk mengisolasi dependencies dari project yang kita kerjakan agar tidak tercampur dengan dependencies dari project lain. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi terdapat risiko tercampurnya dependencies antar project yang terdapat pada komputer kita yang bisa menimbulkan banyak masalah. Jadi, sangat disarankan untuk menggunakan virtual environment ketika bekerja dalam project Django. <br>

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. <br>
  - MVC
    - Model: mengelola database;
    - View: menyajikan tampilan informasi berupa Graphical User Interface (GUI) kepada user;
    - Controller: menghubungkan model dan view.

  - MVT
    - Model: mengelola database;
    - View: menerima request dan mengembalikan respons yang sesuai;
    - Template: mengatur user interface dan menyusun tampilan yang datanya diisi oleh model dan view.

  - MVVM
    - Model: mengelola database;
    - View: menentukan tata letak elemen-elemen yang akan dilihat oleh user;
    - ViewModel: melakukan interaksi dengan model dan meneruskan data ke bagian view. <br>
MVC menggunakan controller sebagai pengatur logika aplikasi. MVT menggunakan Template untuk mengatur logika serta mengembalikan tampilan aplikasi. MVVM   menggunakan ViewModel untuk mengatur logika aplikasi.