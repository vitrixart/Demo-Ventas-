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
# Assuming the file is in the current working directory.
# If not, provide the full path to the file.
try:
    df = pd.read_excel("SalidaFinal.xlsx", engine='openpyxl')

    # Check if 'Region' column exists
    if 'Region' not in df.columns:
        st.error("Error: The DataFrame does not contain the 'Region' column.")
    else:
        # Create a selectbox for region filtering
        selected_region = st.selectbox("Select Region", df['Region'].unique())

        # Filter the DataFrame based on the selected region
        filtered_df = df[df['Region'] == selected_region]

        # Display the filtered DataFrame
        st.write(filtered_df)

        # Check if 'Ventas' column exists in the filtered dataframe
        if 'Ventas' in filtered_df.columns:
            # Create the bar chart using Plotly Express for the filtered data
            fig = px.bar(filtered_df, x='Region', y='Ventas', title=f'Ventas por Región ({selected_region})')
            st.plotly_chart(fig)
        else:
            st.warning("The 'Ventas' column is not present in the filtered data. Cannot create chart.")

except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")
except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")
