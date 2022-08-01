import streamlit as st  
# insert emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config (page_title="Cyber Security_WIT KEL 8", page_icon=":computer:", layout="wide")

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
        st.subheader(":revolving_hearts:Cyber Security: Roles and Function~!:revolving_hearts:")
        st.write("Mengapa peran Cyber Security itu penting? Fungsinya apa aja?")