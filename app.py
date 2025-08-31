import numpy as np
import pandas as pd
#import Scikit_learn
import streamlit as st
import  pickle

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.header("Welcome to Predictor. here you can predict the price of laptop")
company = st.selectbox('Brand',df['Company'].unique())
type = st.selectbox('Type',df['TypeName'].unique())

ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

weight = st.number_input('Weight of the Laptop')

touchscreen = st.selectbox('Touchscreen',['No','Yes'])

ips = st.selectbox('Ips',['No','Yes'])

screen_size = st.slider('Scrensize in inches', 10.0, 18.0, 13.0)
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

cpu = st.selectbox('CPU',df['cpu_brand'].unique())
cpu_gen= st.selectbox('Cpu_gen',sorted(df['cpu_gen'].unique()))
cpu_speed= st.selectbox('CPU Speed in GHz', sorted(df['cpu_speed'].unique()))


hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu,cpu_gen, cpu_speed, hdd, ssd, gpu, os])

    query = query.reshape(1, 14)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))