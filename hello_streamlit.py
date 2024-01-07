import streamlit as st

#Title
st.title("welcome to streamlit ")

#Header
st.header("Streamlit page header")

# Subheader 
st.subheader("Subheader Example") 

# Text 
st.text("This is some text.")

# Displaying data 
data = [1, 2, 3, 4, 5] 
st.write("Data:", data) 

# Dataframe 
import pandas as pd 
df = pd.DataFrame({"col1": [1.1, 2.2, 3.3], "col2": [4.4, 5.5, 6.6]}) 
st.write("DataFrame:", df)

# Plotting 
import matplotlib.pyplot as plt 
import numpy as np 
x = np.linspace(0, 10, 100) 
y = np.sin(x) 
plt.plot(x, y) 
st.pyplot(plt) 
# Interactive widgets 
name = st.text_input("Enter your name:") 
st.write("Hello,", name) 
age = st.slider("Select your age:", 0, 100, 25) 
st.write("Age:", age) 
# Selectbox
color = st.selectbox("Select a color:", ["Red", "Green", "Blue"]) 
st.write("Color:", color)