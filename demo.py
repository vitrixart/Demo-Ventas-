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
import plotly.express as px

# Load the dataframe (assuming it's already loaded as 'df')
try:
    df = pd.read_excel("SalidaFinal.xlsx", engine='openpyxl')
except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
    st.stop() # Stop execution if the file is not found
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

# Create a filter for the 'Region' column
selected_region = st.selectbox("Select Region", df['Region'].unique())
df_filtered = df[df['Region'] == selected_region]

# Create a second filter for 'State' based on the selected region
if not df_filtered.empty: # Check if df_filtered is not empty
    selected_state = st.selectbox("Select State", df_filtered['State'].unique())
    df_final = df_filtered[df_filtered['State'] == selected_state]

    # Check if 'Category' column exists
    if 'Category' in df_final.columns:
        # Create a pie chart for 'Category'
        fig = px.pie(df_final, names='Category', title='Category Distribution')
        st.plotly_chart(fig)
