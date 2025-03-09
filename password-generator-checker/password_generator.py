import re
import streamlit as st

st.set_page_config(page_title=("Password Strength Meter"))

st.markdown("""
<style>
    .main{text-align:center;}
    .stTextInput{width:60 !important; margin:auto;}
    .stButton button{width:50; background-color: blue; color:white; font-size:18px;}
    .stButton button hover:{background-color:red ; color:white;}
</style>    
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level.🔍")

def check_password_strength(password):
    score= 0
    feedback=[]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ password should be **atleast 8 characters long**.")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("❌ password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("❌ password should include **atleast one number (0-9)**.")
    
    if re.search(r"[*&^%$#!]",password):
        score += 1
    else:
        feedback.append("❌ Include **atleast one special character (*&^%$#!)**.")

    if score == 4:
        st.success("✅ **Strong Password** - your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - improve security by adding more features.")
    else:
        st.error("❌ **Week password** - follow the suggestions to strength your password.")


    if feedback:
        with st.expander("**Improve Your Password**"):
            for items in feedback:
              st.write(items)


password=st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐. ")
if st.button("Check strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter password first!")

st.write("----------------")
st.write("Made by Isha Khan")



