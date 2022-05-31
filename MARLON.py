from cmath import nan
import pandas as pd
import seaborn as sns
import numpy as np
from plotly import express as px
from matplotlib import pyplot as plt 
from matplotlib import gridspec
from sqlalchemy import false, true
import streamlit as st 

st.title('Aplicacion de prueba')

st.write('**Datos de king country, USA (20xx a 20xx)**:')
data=pd.read_csv('C:/Users/mfvar/OneDrive/Escritorio/MARLON/MARLONDATA.csv')
st.dataframe(data)

st.write('**Casas en el periodo analisado:**','Disponibles {} casas'.format(data['id'].nunique()))

st.write('**Casa mas barata:**')
st.dataframe(data[data['price']==data['price'].min()])

st.write('**Casa mas cara:**')
st.dataframe(data[data['price']==data['price'].max()])

st.title('Filtros')
##forma de seleccionarlos los datos para el filtro
OptFiltro = st.multiselect(
     'Que quieres filtrar',
     ['Precios','Habitaciones', 'Baños', 'Metros cuadrados (Espacio habitable)','Pisos','Vista al mar','Indice de construccion','Condicion'],
     ['Habitaciones', 'Baños','Pisos'])

if 'Precios' in OptFiltro:
	Price = st.number_input ('Precios',step=1,min_value=0,max_value=round(data['price'].max()))

if 'Habitaciones' in OptFiltro:
	Bedrooms = st.number_input('Habitaciones',step=1,min_value=0,max_value=round(data['bedrooms'].max()))

if 'Baños' in OptFiltro:
	Bathrooms = st.number_input ('Baños',step=1,min_value=0,max_value=round(data['bathrooms'].max()))

if 'Metros cuadrados (Espacio habitable)' in OptFiltro:
	Mt2 = st.number_input('Metros cuadrados (Espacio habitable)',step=1,min_value=0,max_value=round(data['sqft_living'].max()))

if 'Pisos' in OptFiltro:
	Floors = st.number_input('Pisos',step=1,min_value=0,max_value=round(data['floors'].max()))

if 'Vista al mar' in OptFiltro:
	Waterfront= st.number_input('Vista al mar',step=1,min_value=0,max_value=round(data['waterfront'].max()))

if 'Condicion' in OptFiltro:
	Cond = st.number_input('Condicion',step=1,min_value=0,max_value=round(data['condition'].max()))

if 'Indice de construccion' in OptFiltro:
	Grade = st.number_input('Indice de construccion',step=1,min_value=0,max_value=round(data['grade'].max()))






st.write('**Numero de habitaciones:**', Bedrooms)

st.write('**Baños:**', Bathrooms)



st.write('**Pisos:**', Floors)



st.write('**Condicion:**', Cond)

if 0<=Grade<=3:
	st.write('**Indice de construccion:**','Sin construir')
elif 4<=Grade<=6:
	st.write('**Indice de construccion:**','Construccion y diseño pobre')
elif 7<=Grade<=10:
	st.write('**Indice de construccion:**','Construccion y diseño promedio')
elif 11<=Grade<=13:
	st.write('**Indice de construccion:**','Construccion y diseño de alta calidad')


st.title('Info de las casas:')


if 'Precios' in OptFiltro:
	if Price>0:
		st.write('Hay {} casas con Valor igual a {}'.format(data[data['price']==Price].shape[0],Price))

if 'Habitaciones' in OptFiltro:
	if Bedrooms>0:
		st.write('Hay {} casas con {} Habitacion/nes'.format(data[data['bedrooms']==Bedrooms].shape[0],Bedrooms))

if 'Baños' in OptFiltro:
	if Bathrooms>0:
		st.write('Hay {} casas con {} baño/s'.format(data[data['bathrooms']==Bathrooms].shape[0],Bathrooms))

if 'Metros cuadrados (Espacio habitable)' in OptFiltro:
	if Mt2>0:
		st.write('Hay {} casas con {} metros cuadrados habitables'.format(data[data['sqft_living']==Mt2].shape[0],Mt2))

if 'Pisos' in OptFiltro:
	if Floors>0:
		st.write('Hay {} casas con {} Piso/s construidos'.format(data[data['floors']==Floors].shape[0],Floors))

if 'Vista al mar' in OptFiltro:
	if Waterfront ==1:
		st.write('Hay {} casas con vista al mar'.format(data[data['waterfront']==Waterfront].shape[0]))

if 'Condicion' in OptFiltro:
	if Cond>0:
		st.write('Hay {} casas con una condicion igual a {}'.format(data[data['condition']==Cond].shape[0],Cond))

if 'Indice de construccion' in OptFiltro:
	if Grade>0:
		st.write('Hay {} casas con un Indice de construccion igual a {}'.format(data[data['grade']==Grade].shape[0],Grade))


import pandas as pd
import seaborn as sns
from plotly import express as px
from matplotlib import pyplot as plt
from matplotlib import gridspec 
import time

pd.set_option('display.float_format', lambda x: '%.2f' % x)
listas = ['a','b','c']
tuplas = ('a','b','c')
diccionarios = {'Var1':1, 'Var':2}
data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data)
data = pd.read_csv('C:/Users/mfvar/OneDrive/Escritorio/MARLON/MARLONDATA.csv')
data.tail(10)
