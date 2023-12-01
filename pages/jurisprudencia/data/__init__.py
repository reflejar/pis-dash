import pandas as pd

data = pd.read_csv('pages/jurisprudencia/data/doctrinario.csv')



DATA = {
    'filtros': {
        'voces-tematicas': sorted(data['Voces temáticas'].dropna().unique()),
        'provincia': sorted(data['Provincia'].dropna().unique()),
        'tipo-fallo': sorted(data['Tipo de fallo'].dropna().unique()),
        'organismo': sorted(data['Organismo judicial o administrativo'].dropna().unique()),
    },
    'contenido': data
}



