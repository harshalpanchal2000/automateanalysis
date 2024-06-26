import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

# Function to visualize distribution
def visualize_data_distribution(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=20, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    st.pyplot()

# Function to visualize pairwise relationships
def visualize_pairwise_relationships(df):
    sns.pairplot(df)
    st.pyplot()

# Function to visualize feature relationships
def visualize_feature_relationships(df, column_x, column_y):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=column_x, y=column_y, data=df)
    plt.title(f'Relationship between {column_x} and {column_y}')
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    st.pyplot()

# Function to visualize correlation
def visualize_correlation(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    st.pyplot()

# Function for numerical analysis
def perform_numerical_analysis(df):
    numerical_columns = df.select_dtypes(include=['int', 'float']).columns
    st.subheader("Numerical Features:")
    st.write(numerical_columns)
    for column in numerical_columns:
        st.subheader(f"Analysis for Feature named '{column}':")
        st.write("Sample Values:")
        st.write(df[column].sample(min(5, df.shape[0])))
        visualize_data_distribution(df, column)
        visualize_feature_relationships(df, column, df.columns[-1])  # Assuming last column is the target variable
        visualize_pairwise_relationships(df)
    st.subheader("Correlation Heatmap:")
    visualize_correlation(df)
