import pandas as pd
import plotly.express as px
import streamlit as st
import math
from plotly.subplots import make_subplots
import plotly.graph_objects as go

class HdiVisualization:
    
    def __init__(self, df):
        self.df = df
        
    def scattViz(self):
        fig = px.bar(self.df, x='country', y='Hdi2020',
                     text_auto='.2s',
             barmode='group', title='HDI Comparison (2020 vs 2021)',
             labels={'value': 'HDI'},
             height=400,
             width=800)
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig)