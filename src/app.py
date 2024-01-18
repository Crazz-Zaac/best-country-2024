import pandas as pd
import streamlit as st

from visualize import Visualization

from settings import DATASET_DIR
from settings import SRC_DIR


st.header("Visualizing best countries to live in 2024")

def main():
    raw_data = pd.read_csv(DATASET_DIR+'/'+'best-countries-2024.csv')
    
    # data cleaning
    clean_df = raw_data.dropna()
    
    viz = Visualization(clean_df)
    
    st.sidebar.subheader("Select an option")
    choice = st.sidebar.radio("Choose one", 
                     ('View data', 'Visualize data'))
    
    if choice == 'View data':
        viz.viewData()
    


if __name__ == '__main__':
    main()