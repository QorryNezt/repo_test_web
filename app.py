from typing import Container
import streamlit as st  
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
# insert emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config (page_title="Cyber Security_WIT KEL 8", page_icon=":computer:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#------------ LOAD ASSETS ---------
lottie_girl = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_jlkylbqc.json")
lottie_role = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_sy6mqjxk.json")
lottie_wonder= load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ibujvnor.json")
lottie_benefits= load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_p9cnyffr.json")
lottie_thanks = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_totrpclr.json")
lottie_sosmed = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_zwn6fmnu.json")
lottie_insta= load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_5jrklsmp.json")
lottie_linkedin= load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_kaqevbnk.json")
lottie_gmail= load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_tszzqucf.json")

# ----- HEADER -----
with st.container():
    st.title(":computer::woman:Women in TECH Kelas J:woman::computer:")
    st.subheader("Kelompok 8 Project: Cybersecurity :information_desk_person::computer:")
    st.subheader(":sparkling_heart:1. Yasindy Risma Hani:sparkling_heart:") 
    st.subheader(":sparkling_heart:2. Sayyida Qurrata A'yunin:sparkling_heart:")
    
#------- MAIN --------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title(":computer:Cyber Security:computer:")
        st.subheader(":revolving_hearts:Let's Get to Know About CyberSecurity~:revolving_hearts:")
        st.write("##")
        st.write("Jadi sebenarnya Cybersecurity itu apa sih?")
        st.write(
            """
            Di dalam bahasa Indonesia, Cyber security artinya keamanan komputer.
            Jika mengacu pada International Telecommunication Unit (ITU), 
            cyber security adalah aktivitas yang meliputi kebijakan 
            dan konsep keamanan dan berfungsi melindungi aset organisasi. 
            Perlindungan dapat berupa perangkat lunak (software), aplikasi atau apa pun 
            yang berhubungan dengan sistem komputer.
            
            """
                )
    with right_column:
        st_lottie(lottie_girl, height= 300, key="girl")
        st.write("##")
        st.subheader(":revolving_hearts:Cyber Security: Roles and Function~!:revolving_hearts:")
        st.write("##")
        st.write(":question:Mengapa peran Cyber Security itu penting? Fungsinya apa aja?:question:")
        st.write(
            """
            Karena dengan adanya Cyber Security, data - data penting seperti 
            data pribadi kita, rekam medis, dan banyak lagi menjadi aman
            dan tidak disalahgunakan! Peran Cyber Security sangatlah penting bagi
            semua orang di era modern.

            Fungsi Cyber Security yaitu mengamankan data kita agar terhindar dari
            Tindakan kriminal dan mengurangi potensi kriminalitas virtual.

            Memangnya apa sih gunanya data - data itu?
            Nah, data - data yang disebutkan diatas dapat digunakan
            untuk si peretas menggunakan data kita untuk tindakan kriminal virtual!
            Memang seperti halnya mengisi tanggal lahir, tempat tinggal, dan lainnya
            terlihat sepele tapi bagi mereka yang berniat jahat itu potensi bisnis besar untuk
            mereka, lho!
            """
        )
    with left_column:
        st.write("##")
        st_lottie(lottie_role, height= 300, key="role")
        st.write("##")
        st.subheader(":exclamation:Resiko dan Dampak Jika Perangkat atau Gawai Kita Tidak Aman Secara Skala Besar dan Kecil:exclamation:")
        st.write(
            """
            Apa yang terjadi jika perangkat digital kita tidak terlindungi dengan aman?
            Tentu banyak sekali yang terjadi jika kita tidak dapat menjaga gawai atau perangkat digital.
            Salah satu contohnya yaitu kebocoran data pribadi kita, para hacker atau dalam bahasa Indonesia
            peretas akan menggunakan data pribadi kita untuk kegiatan kriminal. Misalnya seperti mereka menggunakan
            nama kita dan segala biodata kita untuk melakukan transaksi gelap. Tiba - tiba nama
            kita tercoreng padahal kita sama sekali tidak tahu apa yang telah terjadi pada saat itu.

            Pernahkah kalian mendengar berita tentang rekening seseorang tiba - tiba memiliki uang yang banyak 
            dan juga dapat berkurang dengan jumlah nominal yang besar ataupun 
            terjadi penambahan uang padahal kamu sama sekali belum menyetorkan uangmu dengan jangka waktu yang lama?
            Itu salah satu contoh kebocoran data di suatu bank. Nah, jika kasus yang
            sama terjadi tetapi di gawai mu? Di telepon genggam kita tersimpan banyak sekali data pribadi kita
            yang sangat berharga. Jika data tersebut jatuh ke tangan yang salah maka dapat mengakibatkan dampak
            yang fatal bagi kita!

            Dengan adanya kebocoran data pribadi kita, para peretas mudah memanipulasi data kita.
            Yang mengakibatkan adanya transaksi yang tidak kita ketahui, akun sosial media kita yang tidak
            terkontrol sehingga mengikuti akun yang bahkan kita tidak tahu itu apa. Adanya
            akses ke situs - situs asing, dan tentu banyak hal negatif lainnya.

            Contoh diatas tersebut dampak skala pribadi atau kecil. Nah, apa yang terjadi jika suatu perusahaan atau
            rumah sakit yang terjadi kebocoran data tersebut? Tentu dampaknya akan sangat merugikan pihak perusahaan
            atau rumah sakit, bukan?

            Para peretas biasanya mengincar data - data yang sangat rahasia agar dapat mereka buat
            sebagai lahan bisnis. Ada yang dapat menjual data tersebut, dan ada juga yang berkedok
            mereka dapat memperbaiki masalah tersebut dengan sejumlah uang yang bernominal tinggi.
            Padahal kebocoran tersebut diakibatkan oleh mereka sendiri.

            """
            )

    with right_column:
        st.write("##")
        st_lottie(lottie_wonder, height= 300, key="wonder")
        st.write("##")
        st.subheader(":star2::iphone:Solusi dan Upaya Serta Manfaat Menjaga Keamanan Perangkat atau Gawai:star2::iphone:")
        st.write(
            """
            Lantas apa solusi dan upaya yang dapat kita lakukan agar perangkat atau gawai kita aman
            dari serangan digital tersebut?
            :sparkles:Ada beberapa cara yang dapat dilakukan,Yaitu:
            
            1. Menghindari instalasi suatu aplikasi diluar tempat resmi 
            seperti Playstore dan Appstore untuk telepon genggam dan Microsoft Store(untuk Windows)
            dan banyak lagi. Situs atau tempat resmi suatu gawai pasti sudah terdapat di dalamnya.

            2. Selalu meng-update sistem menjadi paling baru dan menghindari menggunakan
            aplikasi bajakan agar terhindar dari virus yang berbahaya.

            3. Menghindari kontak yang tidak dikenal jika membagikan suatu link
            ke chat pribadi kamu itu bisa juga penipu lho! Jika kamu dimasukkan ke dalam
            grup percakapan yang tidak dikenal segera keluar dari grup itu dan aktifkan izin
            setiap orang lain ingin memasukkan kamu ke suatu grup (ada di pengaturan sosial media kamu ya)

            Cara - cara diatas hanya sebagiannya saja. Tentu banyak lagi cara yang dapat kamu coba untuk
            membuat perangkat atau gawaimu menjadi aman!
            """
        )
    with left_column:
        st.write("##")
        st_lottie(lottie_benefits, height= 300, key="benefits")
        st.write(
            """
            :star2::iphone:Manfaat apa saja yang kita dapat jika gawai kita aman?:star2::iphone:
            Banyak sekali manfaat yang dapat kita rasakan apabila 
            gawai kita aman dan terlindungi, yakni:
            
            1. Gawai kita akan memberikan performa maksimal
            Apakah kamu pernah mengeluh setiap telepon genggam mu sangat lambat? Seperti membuka sosial media
            dan semacamnya? Salah satunya juga dapat berdampak karena keamanan suatu hp yang buruk
            membuat banyak iklan dan virus masuk dibelakangnya. Sehingga jika kita ingin membersihkannya
            memerlukan waktu dan kesabaran yang lama seperti menyimpan data kita ke tempat lain (Backup Data) 
            dan me-reset pabrik (Factory Reset) sehingga banyak waktu yang terkuras.

            2. Tidak perlu takut kebocoran data!
            Dengan gawai kita aman, kita tidak perlu khawatir akan data yang bocor. Data kita aman
            tersimpan, tapi jangan sampai lengah! Tidak pernah salah untuk selalu mencek keamanan gawai kita
            dengan rutin. Ingat! Sedia payung sebelum hujan ya teman - teman~!

            3. Tidak akan dipidana karena menggunakan aplikasi resmi / tidak bajakan!
            Jika kalian ingin membuat suatu tutorial untuk dibagikan ke seluruh dunia seperti 
            share video tutorialnya di Youtube, dll. Apabila alat atau aplikasi yang 
            kalian gunakan itu bajakan maka kalian termasuk orang yang melanggar hak cipta, lho!
            Menggunakan aplikasi bajakan sama saja mencuri barang milik orang lain!

            Nah, ini sebagian dari manfaat yang kita dapatkan jika gawai kita aman!
            Pastikan jaga data kalian dengan baik ya teman - teman!
            """
        )
        st.write("##")

#--------------- CLOSING AND SPECIAL THANKS -----------
with st.container():
    st.write("---")
    st.write("##")
    left_column, right_column = st.columns(2)
    with right_column:
        st.title("Terima Kasih Telah Membaca Ya Teman - Teman~")
        st_lottie(lottie_thanks, height= 300, key="thanks")
        st.subheader(":sparkles:Special Thanks To::sparkles:")
        st.write(
            """
           :star2: Allah Swt. :star2:
            And...
           :sparkles: Our tutors::sparkles:
            1. Ibu Dania
            2. Ibu Ike
          :sparkles:And everyone who helped me::sparkles:
            1. Kak Nadine
            2. Kak Yasindy Risma Hani
            3. Github
            4. Everyone on Streamlit Forums
            5. Streamlit
            6. Python
            """
        )
        st.write("##")
        
#----------- EXTRAS ----------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Jika kalian tertarik menjaga keamanan dan ketertiban 
            di dunia cyber, yuk! Simak artikel ini!
            Jangan lupa baca E-book-nya juga ya~! 
        """
        )
        st.write(
            """
            :newspaper:Artikel Kak Yasindy:newspaper:
            
            [12 Prospek Pekerjaan Cyber Security yang Menjanjikan, Skill Apa yang Dibutuhkan?](https://www.kompasiana.com/yasindyrismahani8101/62e7fa6a3555e42436240fe2/12-prospek-pekerjaan-cyber-security-yang-menjanjikan-skill-apa-yang-dibutuhkan)
            """)
        st.write("[9 Tools Cyber Security Paling Kuat di Tahun 2022](https://www.kompasiana.com/yasindyrismahani8101/62eccfd908a8b55419787c24/9-tools-cyber-security-paling-kuat-di-tahun-2022-part-1)")
    st.write(
        """
        Penasaran dengan kasus - kasus yang pernah terjadi di Cyber Security 
        dan penjelasan lebih dalamnya? Yuk! Simak presentasi ini ya~!
        [Our Module Study Case~!](https://drive.google.com/file/d/1HHyD5ENQCZnOApzktPRf7yEl8xv01_QG/view?usp=sharing)
        """
    )
#-------------- CONTACT US -------------
with st.container():
    st.write("---")
    st.subheader("Contact Us:")
    st_lottie(lottie_sosmed, height= 300, key="sosmed")
    st.write("##")
    st.subheader("Instagram")
    st_lottie(lottie_insta, height= 200, key="insta")
    st.write(":sparkling_heart:Yasindy Risma Hani:sparkling_heart:")
    st.write("[@yrismhan](https://instagram.com/yrismhan?igshid=YmMyMTA2M2Y=)")
    st.write(":sparkling_heart:Sayyida Qurrata A'yunin:sparkling_heart:")
    st.write("[@koriqory](https://www.instagram.com/koriqory/)")
    st.write("##")
    st.subheader("LinkedIn")
    st_lottie(lottie_linkedin, height= 200, key="linkedin")
    st.write(":sparkling_heart:Yasindy Risma Hani:sparkling_heart:")
    st.write("[Yasindy Risma Hani](https://www.linkedin.com/in/yasindy-risma-hani)")
    st.write("##")
    st.subheader("Google Mail")
    st_lottie(lottie_gmail, height= 200, key= "gmail")
    st.write(":sparkling_heart:Yasindy Risma Hani:sparkling_heart:")
    st.write("yasindyrh@gmail.com")
    st.write(":sparkling_heart:Sayyida Qurrata A'yunin:sparkling_heart:")
    st.write("sayyidaqurrataayunin@gmail.com")