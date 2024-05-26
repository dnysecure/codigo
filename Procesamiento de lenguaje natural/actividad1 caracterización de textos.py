import pathlib
import spacy
from nltk import word_tokenize
import pandas as pd
from spacy import displacy
import csv
import es_core_news_md
nlp = es_core_news_md.load()
filename = "./comentariosOdio.csv"
lines_number = 70
data = pd.read_csv(filename, low_memory=False, delimiter=';',nrows=lines_number,
#nrows=lines_number,
quoting=csv.QUOTE_NONE,
on_bad_lines='skip',
encoding_errors='ignore',
#usecols=['CONTENIDO A ANALIZAR', 'INTENSIDAD'],
usecols=['CONTENIDO A ANALIZAR'],
dtype=str,
)

