import pandas as pd
import streamlit as st
import math
from popviz import PopVisualization
from hdiviz import HdiVisualization

from settings import DATASET_DIR
from settings import SRC_DIR


st.header("Visualizing best countries :earth_africa: to live in 2024")

def viewData(dataframe):
    st.subheader("Dataset 2024")
    items_per_page = 10
    page_number = st.number_input("Select a page number", min_value=1, value=1)
    
    # Sort the DataFrame by the 'Company' column
    total_pages = math.ceil(len(dataframe) / items_per_page)
    page_number = max(1, min(page_number, total_pages))
    
    start_index = (page_number - 1) * items_per_page
    end_index = min(start_index + items_per_page, len(dataframe))
    
    styled_df = dataframe.iloc[start_index:end_index].style
            
    # Display dataframe with pagination
    styled_df = styled_df.set_table_styles(
        [{'selector': 'table', 
            'props': [('width', '800px'), ('height', '800px')]
            }]
    )
    st.write(styled_df)
    
    # Display "Page X of Y" indicator
    st.text(f"Page {page_number} of {total_pages}")
    st.subheader("Overview of data")
    st.table(dataframe.describe())


def main():
    raw_data = pd.read_csv(DATASET_DIR+'/'+'best-countries-2024.csv')
    
    # data cleaning
    clean_df = raw_data.dropna()
    
    
    pop_viz = PopVisualization(clean_df)
    hdi_viz = HdiVisualization(clean_df)
    
    
    st.sidebar.subheader("Select one or more option")
    
    view_dataset = st.sidebar.checkbox('View dataset')
    pop_growth_rate = st.sidebar.checkbox('Population growth rate')
    region_wise_pop = st.sidebar.checkbox('Region wise population')
    region_pop_dist = st.sidebar.checkbox('Region wise population distribution')
    hdi_view = st.sidebar.checkbox('Visualize HDI 2020/21')
    stat_test = st.sidebar.checkbox("Perform statistical analysis")
    
    if view_dataset:
        viewData(clean_df)
    
    if pop_growth_rate:
        pop_viz.popVsPopGrowth()
    
    if region_wise_pop:
        pop_viz.regionPop()
        
    if region_pop_dist:
        pop_viz.regionMemPop()
        
    if hdi_view:
        hdi_viz.scattViz()

    if stat_test:
        st.sidebar.radio('Choose tests', 
                         ('Wilcoxon Signed-Ranked Test', 'Paired T-test'))

if __name__ == '__main__':
    main()