#Libs

import pandas as pd
import numpy as np

#libs gráficas
import plotly.express as px
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt

#Streamlit
import streamlit as st

#Lendo a base de dados e tratanto a base de dados
df_idhm_esp = pd.read_csv('IDHM_ESP.csv')

#Titulo de Página
st.title('IDHM-SP: Índice de Desenvolvimento Humano do Estado de São Paulo')

# Layout do aplicativo
tab0, tab1, tab2, tab3, tab4 = st.tabs(["Geral","IDHM", "IDHM - Escolaridade", "IDHM - Longevidade", "IDHM - Renda"])

# Separando as Tabs
with tab0:
    '''
    ## O que é o IDHM

    Links importantes:

    https://www.undp.org/pt/brazil/o-que-%C3%A9-o-idhm

    Base de dados Ipea

    https://www.ipea.gov.br/ipeageo/arquivos/bases/IDH_2010.xls

    O Índice de Desenvolvimento Humano Municipal (IDHM) é uma medida composta de indicadores de três dimensões do desenvolvimento humano: longevidade, educação e renda. O índice varia de 0 a 1. Quanto mais próximo de 1, maior o desenvolvimento humano.

    O IDHM brasileiro segue as mesmas três dimensões do IDH Global - longevidade, educação e renda, mas vai além: adequa a metodologia global ao contexto brasileiro e à disponibilidade de indicadores nacionais. Embora meçam os mesmos fenômenos, os indicadores levados em conta no IDHM são mais adequados para avaliar o desenvolvimento dos municípios brasileiros. Assim, o IDHM - incluindo seus três componentes, IDHM Longevidade, IDHM Educação e IDHM Renda - conta um pouco da história dos municípios em três importantes dimensões do desenvolvimento humano durantes duas décadas da história brasileira.
    '''
    #DataFrame
    df = pd.DataFrame(df_idhm_esp)
    st.dataframe(df, use_container_width=True)
    # Gráfico pairplot (Descobrir)
    st.markdown('Pairplot')
    st.pyplot(sns.pairplot(df_idhm_esp, hue = 'classe'))

with tab1:
    
    #boxsplot
    fig1 = px.box(df_idhm_esp, y='idhm', color = 'classe')
    fig1.update_layout(title_text="Boxsplot IDHM")
    st.plotly_chart(fig1,  use_container_width = True)
    
    #Grafico Donut
    fig5 = go.Figure(go.Pie(labels=df_idhm_esp['classe'], values=df_idhm_esp['idhm'], hole = 0.5))
    fig5.update_layout(title_text="IDHM Estado de São Paulo")
    st.plotly_chart(fig5,  use_container_width = True)

with tab2:
    #Boxsplot
    fig2 = px.box(df_idhm_esp, y='idhm_educacao', color = 'classe')
    fig2.update_layout(title_text="Boxsplot IDHM com o indicador de Educação")
    st.plotly_chart(fig2,  use_container_width = True)

    #Grafico Donut
    #IDHM - Escolaridade
    fig6 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig6.add_trace(go.Pie(labels=df_idhm_esp['classe'], values=df_idhm_esp['idhm'], name="IDHM"), 1, 1)
    fig6.add_trace(go.Pie(labels=df_idhm_esp['classe'], values=df_idhm_esp['idhm_educacao'], name="IDHM Escolaridade"), 1, 2)
    # Tamanho do buraco da rosca
    fig6.update_traces(hole=0.7, hoverinfo="label+percent+name")

    fig6.update_layout(
        title_text="Comparando as Características do IDHM com o indicador de Escolaridade",
        # OPrganizando as anotações no gra´fico.
        annotations=[dict(text='IDHM', x=0.16, y=0.5, font_size=20, showarrow=False),
                    dict(text='Escolaridade', x=0.915, y=0.5, font_size=20, showarrow=False)])
    st.plotly_chart(fig6,  use_container_width = True)

with tab3:
    #Boxsplot
    fig3 = px.box(df_idhm_esp, y='idhm_longevidade', color = 'classe')
    fig3.update_layout(title_text="Boxsplot IDHM com o indicador de Longevidade")
    st.plotly_chart(fig3,  use_container_width = True)
    #Donut
    fig7 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig7.add_trace(go.Pie(labels=df_idhm_esp['classe'], values=df_idhm_esp['idhm'], name="IDHM"),
                1, 1)
    fig7.add_trace(go.Pie(labels=df_idhm_esp['classe'], values=df_idhm_esp['idhm_longevidade'], name="IDHM Longevidade"),
                1, 2)

    # Tamanho do buraco da rosca
    fig7.update_traces(hole=0.7, hoverinfo="label+percent+name")

    fig7.update_layout(
        title_text="Comparando as Características do IDHM com o indicador de Longevidade",
        # Organizando as anotações no gra´fico.
        annotations=[dict(text='IDHM', x=0.165, y=0.5, font_size=20, showarrow=False),
                    dict(text='Longevidade', x=0.925, y=0.5, font_size=20, showarrow=False)])
    
    st.plotly_chart(fig7,  use_container_width = True)

with tab4:
    #Boxsplot
    fig4 = px.box(df_idhm_esp, y='idhm_renda', color = 'classe')
    fig4.update_layout(title_text="Boxsplot IDHM com o indicador de Renda")
    st.plotly_chart(fig4,  use_container_width = True)

    #Donut
    fig8 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig8.add_trace(go.Pie(labels=df_idhm_esp['classe'], values=df_idhm_esp['idhm'], name="IDHM"),
                1, 1)
    fig8.add_trace(go.Pie(labels=df_idhm_esp['classe'], values=df_idhm_esp['idhm_renda'], name="IDHM Renda"),
                1, 2)
    # Tamanho do buraco da rosca
    fig8.update_traces(hole=0.7, hoverinfo="label+percent+name")

    fig8.update_layout(
        title_text="Comparando as Características do IDHM com o indicador de Renda",
        # Organizando as anotações no gráfico.
        annotations=[dict(text='IDHM', x=0.165, y=0.5, font_size=20, showarrow=False),
                    dict(text='Renda', x=0.85, y=0.5, font_size=20, showarrow=False)])
    st.plotly_chart(fig8,  use_container_width = True)

