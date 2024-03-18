import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vREj6UjW5ykyL4n89OuOlbIu0S5AVUuC7Y9aDG1tDrJerg7FusLqfrR7XLVwxFqTehJlbktv0r-JzCJ/pub?output=csv')
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['Hanzi'].values[i]
word_pin=voc['Pinyin'].values[i]
st.write(word_fr+"|"+word_chi+"|"+word_pin)
st.button("refresh")
indices=np.random.choice(l,size=4,replace=False)
i=np.random.choice(indices)
for i range(4)
