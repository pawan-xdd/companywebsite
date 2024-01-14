import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. 
Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. 
Fusce nec tellus sed augue semper porta. Mauris massa. 
Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora 
torquent per conubia nostra, 
per inceptos himenaeos.
"""
st.write(content)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].title()} {row["last name"].title()}")
        st.subheader(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row["last name"].title()}")
        st.subheader(row["role"])
        st.image("images/" + row["image"])


with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].title()} {row["last name"].title()}")
        st.subheader(row["role"])
        st.image("images/" + row["image"])

    


