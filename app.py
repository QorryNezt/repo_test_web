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
        st.write("Mengapa peran Cyber Security itu penting? Fungsinya apa aja?")
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