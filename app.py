import streamlit as st
from transformers import pipeline


pipe_sent = pipeline('sentiment-analysis')
pipe_summ = pipeline("summarization", model="facebook/bart-large-cnn")

text = st.text_area('Enter the text to analyze')

if text:
    st.write("Sentiment")
    out = pipe_sent(text)
    st.json(out)

    st.write("Summarization")
    out_summ = pipe_summ(text)
    st.json(out_summ)
