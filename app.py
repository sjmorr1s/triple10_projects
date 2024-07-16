#Import Libraries
import streamlit as st
import pandas as pd
import plotly.express as px

#read dataset
df = pd.read_csv('vehicles_us.csv')

#Adding Streamlit Components
# Title and header
st.title("Car Sales Dashboard")
st.header("Exploratory Data Analysis of Car Sales")

# Histogram for price
fig_price = px.histogram(df, x='price', title='Distribution of Prices')
st.plotly_chart(fig_price)

# Histogram for odometer readings
fig_odometer = px.histogram(df, x='odometer', title='Distribution of Odometer Readings')
st.plotly_chart(fig_odometer)

# Scatter plot for price vs. odometer
fig_price_odometer = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
st.plotly_chart(fig_price_odometer)

# Scatter plot for model year vs. price
fig_model_year_price = px.scatter(df, x='model_year', y='price', title='Model Year vs. Price')
st.plotly_chart(fig_model_year_price)

# Checkbox to show/hide price histogram
if st.checkbox('Show Price Histogram'):
    st.plotly_chart(fig_price)