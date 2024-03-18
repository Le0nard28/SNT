import streamlit as st
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vREj6UjW5ykyL4n89OuOlbIu0S5AVUuC7Y9aDG1tDrJerg7FusLqfrR7XLVwxFqTehJlbktv0r-JzCJ/pub?output=csv')
l=voc.sharpe[0]
i=np.random.choice(range(l))
word_fr=voc['Definition'].values[i]
word_chi=voc['hanzi'].values[i]
sti.write(word_fr+"hanzi"+wrd_chi)
