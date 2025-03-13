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
        import pandas as pd
import streamlit as st

# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx", engine='openpyxl')

    # Create filters for 'Region' and 'State'
    selected_region = st.selectbox('Select Region', df['Region'].unique())
    selected_state = st.selectbox('Select State', df['State'].unique())

    # Filter the DataFrame based on selected region and state
    filtered_df = df[(df['Region'] == selected_region) & (df['State'] == selected_state)]

    # Display the first row of the filtered data (or an empty DataFrame if no match)
    if not filtered_df.empty:
        st.write(filtered_df.head(1))  # Show only one result
    else:
        st.write("No data found for the selected region and state.")
