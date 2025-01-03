import json
import requests
import streamlit as sLit


sLit.set_page_config(page_title="Portfolio", page_icon=":tada:", layout="wide")




# LOAD



with sLit.container():
    sLit.title("Hi, I'm Hunter")
    sLit.subheader("Recent Computer Science Graduate")
    sLit.write("Seeking employment in the Software/IT career path")


with sLit.container():
    sLit.write("----")
    left_column, right_column = sLit.columns(2)
    with left_column:
        sLit.header("About Me")
        
        sLit.write("""  I recently graduated from Michigan Technological University and
        have Advanced knowledge in SQL, Python, C#, and Excel. I have experience in PHP, HTML, CSS
        Java, C++, and Microsoft Suite. """)

   
#CONTACT
with sLit.container():
    sLit.write("---")
    sLit.header("Contact Me!")
    

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
