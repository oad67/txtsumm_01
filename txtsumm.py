import streamlit as st

import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


nltk.download("stopwords")
nltk.download("punkt")

import joblib

st.set_page_config(page_title="Text Summarizer_OA")
st.header("OA's Text Summarizer")

text=st.text_area("Enter text to summarize:")

#clicked=st.button("Summarize")
####



if st.button("Summarize"):
    import pandas as pd
    import numpy as np


    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize

    sw=set(stopwords.words('english'))
    words=word_tokenize(text)

    freqTable=dict()
    for word in words:
        word=word.lower()
        if word in sw:
            continue
        if word in freqTable:
            freqTable[word]+=1
        else: freqTable[word]=1
    
    sentences=sent_tokenize(text)

    def get_sentencevalue():
        sentencevalue=dict()
        for sentence in sentences:
            for word,freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentencevalue:
                        sentencevalue[sentence]+=freq
                    else:sentencevalue[sentence]=freq
        return sentencevalue
    sentencevalue=get_sentencevalue()

    
    def get_sumvalues():
        sumvalues=0
        for sentence in sentencevalue:
            sumvalues+=sentencevalue[sentence]
        
        average=int(sumvalues/len(sentencevalue))
        return(average)

    average=get_sumvalues()

    

    summary=''
    for sentence in sentences:
        if(sentence in sentencevalue) and (sentencevalue[sentence]>(1.2*average)):
            summary+=" "+sentence


    st.write("---------------")
    
    st.write(summary)
