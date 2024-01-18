import pandas as pd
import plotly.express as px
import streamlit as st
import math


class Visualization:
    
    def __init__(self, df):
        self.df = df
    
    # vewing data 
    def viewData(self):
        st.subheader("View dataset")
        items_per_page = 10
        page_number = st.number_input("Select a page number", min_value=1, value=1)
        
        # Sort the DataFrame by the 'Company' column
        total_pages = math.ceil(len(self.df) / items_per_page)
        page_number = max(1, min(page_number, total_pages))
        
        start_index = (page_number - 1) * items_per_page
        end_index = min(start_index + items_per_page, len(self.df))
        
        styled_df = self.df.iloc[start_index:end_index].style
                
        # Display dataframe with pagination
        styled_df = styled_df.set_table_styles(
            [{'selector': 'table', 
                'props': [('width', '800px'), ('height', '800px')]
                }]
        )
        st.write(styled_df)
        
        # Display "Page X of Y" indicator
        st.text(f"Page {page_number} of {total_pages}")
        