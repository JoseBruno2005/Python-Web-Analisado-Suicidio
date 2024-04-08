import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def lerdados_continente():
    dados_continente = pd.read_csv(r'C:\Users\joseb\Desktop\Catolica\projetoMatematicaAplicada\analiseSuicidio\dados\continente.csv',delimiter=';')
    return dados_continente

def lerdados_linha():
    dados_linha = pd.read_csv(r'C:\Users\joseb\Desktop\Catolica\projetoMatematicaAplicada\analiseSuicidio\dados\linhatempopb.csv', delimiter=';')
    return dados_linha

def lerdados():
    dados = pd.read_csv(r'C:\Users\joseb\Desktop\Catolica\projetoMatematicaAplicada\analiseSuicidio\dados\dataset.csv', delimiter=';')
    dados_ordenados = dados.sort_values(by='suicidios', ascending=False)
    return dados_ordenados

def exibir_grafico_continente(dados):
    fig = px.bar(dados, x='Continente', y='Porcentagem')
    return fig


def exibir_grafico_pais(dados):
    fig = px.pie(dados, values='suicidios', names='estado', title='Suicídios por estado em 2019')
    fig.update_layout(
        width=800,
        height=600
    )
    return fig

def exibir_grafico_linhas_uf(dados):
    fig = px.line(dados, x='anos', y='suicidios')
    return fig

def exibircorrelacao(dados):
    dados.drop(columns=['estado'], inplace=True)
    fig = px.imshow(dados.corr())
    return fig