import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the dashboard
st.title("Simple Streamlit Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")
option = st.sidebar.selectbox("Select a number", range(1, 11))

# Display selected option
st.write(f"You selected: {option}")

# Generate some data
data = np.random.randn(100, 2)

# Create a DataFrame
df = pd.DataFrame(data, columns=["Column 1", "Column 2"])

# Display the DataFrame
st.write("DataFrame:", df)

# Plot the data
fig, ax = plt.subplots()
ax.scatter(df["Column 1"], df["Column 2"])
ax.set_title("Scatter Plot")
st.pyplot(fig)