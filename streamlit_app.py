import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vREj6UjW5ykyL4n89OuOlbIu0S5AVUuC7Y9aDG1tDrJerg7FusLqfrR7XLVwxFqTehJlbktv0r-JzCJ/pub?output=csv')
st.dataframe(voc)
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr['Definition'].values[i]
word_chi['Hanzi'].values[i]
