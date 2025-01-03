import json
import requests
import streamlit as sLit
from streamlit_drawable_canvas import sLit_canvas
import pandas as pd
from PIL import Image

sLit.set_page_config(page_title="Portfolio", page_icon=":tada:", layout="wide")

drawing_mode = sLit.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = sLit.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = sLit.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = sLit.sidebar.color_picker("Stroke color hex: ")
bg_color = sLit.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = sLit.sidebar.file_uploader("Background image:", type=["png", "jpg"])

realtime_update = sLit.sidebar.checkbox("Update in realtime", True)


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

        canvas_result = sLit_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    sLit.image(canvas_result.image_data)
if canvas_result.json_data is not None:
    objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
    for col in objects.select_dtypes(include=['object']).columns:
        objects[col] = objects[col].astype("str")
    sLit.dataframe(objects)

   
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
