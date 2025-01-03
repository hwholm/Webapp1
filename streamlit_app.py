import json
import requests
import streamlit as sLit
from streamlit_lottie import st_lottie

sLit.set_page_config(page_title="Portfolio", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# LOAD
data_anim = load_lottieurl("https://lottie.host/671e9cbb-e466-4556-8a88-61bd0d4e21dc/WH5NXnSzyQ.json")


with sLit.container():
    sLit.subheader("Hi, I'm Hunter")
    sLit.title("Recent Computer Science Graduate")
    sLit.write("Seeking employment in the Data/Business Analyst career path")


with sLit.container():
    sLit.write("----")
    left_column, right_column = sLit.columns(2)
    with left_column:
        sLit.header("About Me")
        sLit.write("##")
        sLit.write("""I recently graduated from Michigan Technological University and
                     am pursuing my PL-300 Power Bi Microsoft Certification.
                     I have advanced knowledge of Excel, SQL, and Python. """)

    with right_column:
        st_lottie(data_anim, height=300, key="dataswag")

#CONTACT
with sLit.container():
    sLit.write("---")
    sLit.header("Contact Me!")
    sLit.write("##")

    contact_form = """
    <form action="https://formsubmit.co/3c453c5127a8018a4793fd8f6c9951ef" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = sLit.columns(2)
with left_column:
    sLit.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    sLit.empty()
