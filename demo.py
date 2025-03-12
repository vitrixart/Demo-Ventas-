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
import matplotlib.pyplot as plt

# ... (your existing code) ...

try:
    df = pd.read_excel("SalidaFinal.xlsx", engine='openpyxl')

    # Assuming 'Region' and 'Sales' are column names in your DataFrame
    sales_by_region = df.groupby('Region')['Sales'].sum()

    plt.figure(figsize=(10, 6))
    sales_by_region.plot(kind='bar')
    plt.title('Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    st.pyplot(plt)


except FileNotFoundError:
    st.error("Error: 'SalidaFinal.xlsx' not found. Please check the file path.")
except KeyError:
    st.error("Error: 'Region' or 'Sales' column not found in the DataFrame.")
except Exception as e:
    st.error(f"An error occurred: {e}")
