import pandas as pd

data = pd.read_csv('pages/jurisprudencia/data/doctrinario.csv')



DATA = {
    'filtros': {
        'voces-tematicas': data['Voces temáticas'].dropna().unique(),
        'provincia': data['Provincia'].dropna().unique(),
        'tipo-fallo': data['Tipo de fallo'].dropna().unique(),
        'organismo': data['Organismo judicial o administrativo'].dropna().unique(),
    },
    'contenido': data
}



