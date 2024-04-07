import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..") 
from utils.model_utils import load_qa_model

# Streamlit app title and description
st.title("Give me the text and I will answer your questions!")
st.write("This is a simple Streamlit app that utilizes a RoBERTa model for question answering.")

# Text input box for user input
context = st.text_area("Enter the context:", "Enter or paste the context here.")
question = st.text_input("Enter your question:", "e.g. What is the answer?")

# Load the question answering model
qa_pipeline = load_qa_model()

# Button to generate response
if st.button("Get Answer"):
    # Get answer using the RoBERTa model
    answer = qa_pipeline(question=question, context=context)
    st.write("Answer:")
    st.write(answer['answer'])
