import streamlit as st
import pandas as pd

from app.data_loader import DataLoader
from app.correlation_analyzer import CorrelationAnalyzer

st.set_page_config(
    page_title="AI Feature Engineering Pipeline",
    layout="wide"
)

st.title("🧠 AI Feature Engineering Pipeline")

loader = DataLoader()

df = loader.load_data(
    "data/sample_dataset.csv"
)

st.subheader("📋 Dataset Preview")

st.dataframe(df.head())

analyzer = CorrelationAnalyzer()

correlation_matrix = analyzer.analyze(df)

st.subheader("📊 Correlation Matrix")

st.dataframe(correlation_matrix)
