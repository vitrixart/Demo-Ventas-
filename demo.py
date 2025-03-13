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
    # Filtro por Región
region_filter = st.selectbox("Selecciona una región:", df['Region'].unique())
filtered_df = df[df['Region'] == region_filter]


# Filtro por Estado basado en la selección de Región
if not filtered_df.empty: #Check if the filtered df is not empty
    state_filter = st.selectbox("Selecciona un estado:", filtered_df['State'].unique())
    filtered_df = filtered_df[filtered_df['State'] == state_filter]
else:
    st.warning("No hay datos para la región seleccionada.")

# Mostrar el DataFrame filtrado
st.write(filtered_df)


# Gráfica de pastel por categoría
if 'Category' in df.columns:  # Check if the 'Category' column exists
    if not filtered_df.empty:
      fig = px.pie(filtered_df, names='Category', title='Distribución por Categoría')
      st.plotly_chart(fig)
