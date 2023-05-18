import pandas as pd

base=pd.read_csv('data/base_censo.csv', sep=";", encoding='latin1')
anio_censo=base["Año del censo"].sort_values(ascending=True).unique().tolist()
municipios=base["Partido"].sort_values(ascending=True).unique().tolist()