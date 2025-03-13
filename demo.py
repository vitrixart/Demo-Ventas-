import streamlit as st
import pandas as pd

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx", engine='openpyxl')
    st.write(df)  # Display the DataFrame using Streamlit
except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")
import pandas as pd
import streamlit as st
import plotly.express as px

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx", engine='openpyxl')

    # Check if 'Region' and 'Ventas' columns exist
    if 'Region' not in df.columns or 'Sales' not in df.columns:
        st.error("Error: The DataFrame does not contain 'Region' and/or 'Sales' columns.")
    else:
        # Create the bar chart using Plotly Express
        fig = px.bar(df, x='Region', y='Sales', title='Ventas por Región')

        # Display the chart in Streamlit
        st.plotly_chart(fig)
    # Create a filter for the 'Region' column
region_filter = st.selectbox("Select Region", df['Region'].unique)

# Filter the dataframe based on the selected region
filtered_df = df[df['Region'] == region_filter]

# Create a second filter for the 'State' column using the filtered dataframe
if not filtered_df.empty: # Check if the filtered dataframe is not empty
    state_filter = st.selectbox("Select State", filtered_df['State'].unique())
    # Filter the dataframe again based on the selected state
    filtered_df = filtered_df[filtered_df['State'] == state_filter]

# Create the pie chart
if not filtered_df.empty: #Check if the filtered dataframe is not empty
    if 'Category' in filtered_df.columns: # Check if the 'Category' column exists
        fig = px.pie(filtered_df, names='Category', title='Category Distribution')
        st.plotly_chart(fig)
