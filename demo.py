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
        # Assuming df is your DataFrame and it's already loaded
# Replace this with your actual data loading code if needed
try:
    df = pd.read_excel("SalidaFinal.xlsx", engine='openpyxl')
except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
    st.stop() # Stop execution if the file is not found
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

# Create filters
region_filter = st.selectbox("Select Region", df['Region'].unique())
state_filter = st.selectbox("Select State", df['State'].unique())

# Apply filters and display the result
filtered_df = df[(df['Region'] == region_filter) & (df['State'] == state_filter)]
