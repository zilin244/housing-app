import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median House Price', 0, 500001, 200000)  # min, max, default

# create a multi select
location_type_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio 
income_level = st.sidebar.radio(
    'Choose Income Level:',
    ('Low', 'Medium', 'High')
)


if income_level == 'Low':
    df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium':
    df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:  # High (> 4.5)
    df = df[df['median_income'] > 4.5]

# filter by price
df = df[df.median_house_value >= price_filter]

# filter by location type
df = df[df.ocean_proximity.isin(location_type_filter)]

st.subheader('See more filters in the sidebar:')

# show on map
st.map(df)


# show the plot
st.subheader('A Histogram of The Median House Value')
fig, ax = plt.subplots()
# df.median_house_value.plot(kind='hist', bins=30)
plt.hist(df['median_house_value'], bins=30, edgecolor='none')
st.pyplot(fig)







