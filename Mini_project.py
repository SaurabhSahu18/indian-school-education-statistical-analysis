from random import choices
import streamlit as st
import pandas as pd
import plotly_express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title("Indian School Education Statistical Analysis")
plt.style.use('ggplot')

st.header("-Gross Dataset")
def load_data():
    gross=pd.read_csv("C:/Users/HP/digipython/gross-enrollment-ratio.csv")
    return gross

data=load_data()
st.write(data)

graphchoice=[" Primary Girls in UP"," Primary Boys in UP","All State_UT Dropout Student data","Student enrolled in computer",
                  "Water Supply in all School"]
choice=st.sidebar.radio("Choice",graphchoice)
if choice== graphchoice[0]:
    st.header("Gross Dataset of Primary Girls in UP")
    fig,ax = plt.subplots(figsize=(10,5))
    # ax=plt.axes()
    ax.set_facecolor('lightgreen')
    gross_dataup=data[data['State_UT']=='Uttar Pradesh']
    plt.bar(gross_dataup['Primary_Girls'],gross_dataup['Year'],color='green')
    plt.xlabel('Primary_Girls')
    plt.ylabel('Year')
    plt.title('year basis data in UP')
    st.pyplot(fig)

if choice==graphchoice[1]:
    st.header("Gross Dataset of Primary Boys in UP")
    fig,ax=plt.subplots(figsize=(10,5))
    ax=plt.axes()
    ax.set_facecolor('lightblue')
    gross_dataup=data[data['State_UT']=='Uttar Pradesh']
    plt.bar(gross_dataup['Primary_Boys'],gross_dataup['Year'],color='red')
    plt.xlabel('Primary_Boys')
    plt.ylabel('Year')
    plt.title('year basis data in UP')
    st.pyplot(fig)

st.header("-Dropout Dataset")
def load_data1():
    dropout=pd.read_csv("C:/Users/HP/digipython/dropout-ratio-2012-2015.csv")
    return dropout

data1=load_data1()
st.write(data1)

if choice==graphchoice[2]:
    st.header("All State_UT Dropout Student data")
    fig,ax = plt.subplots(figsize=(10,5))
    sns.countplot(data1['State_UT'])
    plt.xticks(rotation=90)
    st.pyplot(fig)


st.header("-Computer Dataset")

def load_data2():
    computer=pd.read_csv("C:/Users/HP/digipython/percentage-of-schools-with-comps-2013-2016.csv")
    return computer

data2=load_data2()
st.write(data2)
if choice==graphchoice[3]:
    st.header("All States/UT Student enrolled in computer")
    fig = plt.figure(figsize = (10,5)) 
    ax=plt.axes()
    ax.set_facecolor('gray')
    plt.bar(x=data2['State_UT'], height= data2['All Schools'],color ='yellow', width = 0.6) 
    plt.xlabel("STATES") 
    plt.ylabel("All Schools") 
    plt.title("Student enrolled in computer") 
    plt.xticks(rotation=90)
    st.pyplot(fig)

st.header("-Water Dataset")
def load_data3():
    water=pd.read_csv("C:/Users/HP/digipython/percentage-of-schools-with-water-facility-2013-2016.csv")
    out = water.groupby(['State/UT','Year'])['Primary_Only'].sum().reset_index()
    return out

data3=load_data3()
st.write(data3)
if choice==graphchoice[4]:
    st.header("Water Supply in all School")
    water=pd.read_csv("C:/Users/HP/digipython/percentage-of-schools-with-water-facility-2013-2016.csv")
    out = water.groupby(['State/UT','Year'])['Primary_Only'].sum().reset_index()
    fig,ax= plt.subplots(figsize=(7,5))
    sns.barplot(y='Primary_Only',x='State/UT',data=out,hue='Year',color='darkorange',ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)









