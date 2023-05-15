#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image

openai.api_key = st.secrets["API_key"]

def generate_image(input_string): 
  response = openai.Image.create(
    prompt=input_string,
    n=1,
    size="256x256"
  )
  image_url = response['data'][0]['url']
  return image_url

# Define the Streamlit app
def app():
    st.title("Weebsu Biswal")
    st.header("AI Generated Images")
    st.write('Thank you for appreciating my chatting skills! But my neurons can do other useful things besides chat. For instance, I can help you visualize challenging ideas and concepts.') 
    # Create a multiline text field
    user_input = st.text_area('Describe the image with as much details as possible. Try "deep learning using artificial intelligence"', height=5)

    # Display the text when the user submits the form
    if st.button('Submit'):
        output = generate_image(user_input)
        urllib.request.urlretrieve(output, 'output.png')
        img = Image.open('output.png')
        img_array = np.array(img)
        fig = plt.figure(figsize=(9,9))
        ax = plt.axes(xticks=[], yticks=[])
        ax.imshow(img_array)
        st.pyplot(fig)
        
    st.write('\n\n\n© 2023 West Visayas State University - Management Information System Office.')
    st.write('\n\n\nDisclaimer: Weebsu may produce inappropriate images. Please avoid using prompts that constitute unlawful use of AI.')
    text = "*WVSU at the forefront of AI-research in Western Visayas.*"
    st.markdown(text)
     

# Run the app
if __name__ == "__main__":
    app()
