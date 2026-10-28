import streamlit as st
from PIL import Image

col1, col2 = st.columns((4, 5))
with col1:
    st.title("Parker Millsap")
    st.header("Freshman at JBU")

with col2:
    image = Image.open('images.webp')
    st.image(image, width=200)

st.subheader("About Me")
st.text("I am 19 years old")
st.text("I am double majoring in CS and GD")
st.divider()

st.subheader("Qualifications")
st.text("Valedictorian")
st.text("Secretary of Student Council")
st.text("Honors Student")
st.divider()

st.subheader("Work Experience")
st.markdown("**Part-time IT at NCS**")
st.text("I organized hardware products and helped identify which would be better suited for each situation. In addition, I held a spreadsheet keeping inventory of all hardware present. My coworkers and I also helped set up laptops for the new school year.")
st.markdown("**Part-time at Summer Sno Co.**")
st.text("I worked together with others to provide shaved-ice products efficiently.")
st.divider()

st.subheader("Projects")
st.markdown("**Budgeting App**")
st.text("While collaborating with a partner, we developed an application to assist in handling and budgeting money within each user's custom categories.")
st.markdown("**Ceiling Tile Painting**")
st.text("Working alone, I hand painted a ceiling tile to be a mural representing the senior class of 2026 at my high school.")
st.divider()

st.subheader("Contact Me")
user_name = st.text_input("Enter your name:")
user_email = st.text_input("Enter your email:")
user_message = st.text_input("Enter your message:")
st.button("Submit")