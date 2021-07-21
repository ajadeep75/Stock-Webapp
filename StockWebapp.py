# Importing Necessary packages that run our application
import streamlit as st
import pandas as pd
from PIL import Image

#Title
st.write("""
#Stock Market Application
Visually showing Data on stock (Data ranges from 17-07-2020 - 17-07-2021)
""")

#Image
image=Image.open("E:/Projects/Stock Webapp/stock_image.jpg")
st.image(image, use_column_width=True)

#SideBar
st.sidebar.header('User Input')

#Function to get users input
def get_input():
    start_date = st.sidebar.text_input("Start Date","2020-07-17")
    end_date = st.sidebar.text_input("End Date","2021-07-17")
    stock_symbol = st.sidebar.text_input("Stock Symbol","GOOG")
    return start_date,end_date,stock_symbol

#Function to get company name
def get_company_name(symbol):
    if symbol == 'GOOG':
        return 'Google'
    elif symbol == 'INTC':
        return 'Intel'
    elif symbol == 'FB':
        return 'Facebook'
    else:
        'None'

#Function to get a Company's Dataset and Proper Timezone
def get_data(symbol,start,end):
    if symbol.upper() == 'GOOG':
         df=pd.read_csv('E:/Projects/Stock Webapp/GOOG.csv')
    elif symbol.upper() == 'INTC':
        df=pd.read_csv('E:/Projects/Stock Webapp/INTC.csv')
    elif symbol.upper() == 'FB':
        df=pd.read_csv('E:/Projects/Stock Webapp/FB.csv')
    else:
        df=pd.DataFrame(columns = ['Date', 'Close', 'Open', 'Adj Close', 'High', 'Low'])

#Get the Date Range
start = pd.to_datetime(start)
end = pd.to_datetime(end)

start_row=0
end_row=0

for i in range(0,len(df)):
    if start <= pd.to_datetime(df['Date'][i]):
        start_row = i
        break

for j in range(0,len(df)):
    if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
        end_row = len(df)-1-j
        break

#Set the index to be the Date
df = df.set_index(pd.DateTimeIndex(df['Date'].values))

return df.iloc[start_row:end_row +1, :]

#Get the Users Input
start,end,symbol = get_input()
#Get Data
df = get_data(symbol,start,end)
#Get Company's Data
company_name = get_company_name(symbol.upper())

#Displaying Close Price
st.header(company_name+"Close Price\n")
st.line_chart(df['Close'])

#Displaying Volume
st.header(company_name+"Volume\n")
st.line_chart(df['Volume'])

#Statistics on Data
st.header('Data Statistics')
st.write(df.describe())
    




    