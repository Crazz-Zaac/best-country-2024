import pandas as pd
import plotly.express as px
import streamlit as st
import math
from plotly.subplots import make_subplots
import plotly.graph_objects as go

class PopVisualization:
    
    def __init__(self, df):
        self.df = df
    
    
    def popVsPopGrowth(self):
        st.subheader("Which country experienced how much population growth rate?")
        # Plotting population_growthRate with respect to country
        fig = px.bar(self.df, x='country', y='population_growthRate',
                    title='Population Growth Rate with respect to Country',
                    labels={'population_growthRate': 'Population Growth Rate'})

        # Rotate x-axis labels for better visibility
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig)
    
    def regionPop(self):
        st.subheader("Which region has how much population?")
        # Plotting population_2024 with respect to region on a choropleth map
        fig = px.choropleth(self.df, 
                            locations='country',  # Assuming 'country' column contains country codes or names
                            locationmode='country names',  # Specify the location mode
                            color='population_2024',
                            hover_name='country',  # Display country names on hover
                            title='Population 2024 by Region',
                            labels={'population_2024': 'Population 2024'},
                            color_continuous_scale='rainbow')  # Choose the color scale

        # Set the projection to Natural Earth
        fig.update_geos(projection_type="orthographic")
        # Set height and width
        fig.update_layout(height=700, width=700)

        st.plotly_chart(fig)
        
    def regionMemPop(self):
        st.subheader("Which country has the highest populaton region wise?")
        
        # First Pie Chart: region wise Population
        asian_df = self.df[self.df['region'] == 'Asia']
        europe_df = self.df[self.df['region'] == 'Europe']
        africa_df = self.df[self.df['region'] == 'Africa']
        north_america_df = self.df[self.df['region'] == 'North America']
        south_america_df = self.df[self.df['region'] == 'South America']
        
        

        # asian population
        pop_gt_100m_df = asian_df[asian_df['population_2024'] > 60000000]
        pop_lte_100m_df = asian_df[asian_df['population_2024'] <= 60000000]
        
        # european population
        pop_gt_10m_eu = europe_df[europe_df['population_2024'] > 10000000]
        pop_lte_10m_eu = europe_df[europe_df['population_2024'] <= 10000000]

        
        # Africa population
        pop_gt_35m_africa = africa_df[africa_df['population_2024'] > 30000000]
        pop_lte_35m_africa = africa_df[africa_df['population_2024'] <= 30000000]


       
        # Subplots
        fig_asia = make_subplots(rows=1, cols=2, 
                            specs=[[{"type": "domain"}, {"type": "domain"}]],
                            subplot_titles=['Population > 60M', 'Population <= 60M'])

        fig_eu = make_subplots(rows=1, cols=2, 
                            specs=[[{"type": "domain"}, {"type": "domain"}]],
                            subplot_titles=['Population > 10M', 'Population <= 10M'])

        fig_africa = make_subplots(rows=1, cols=2, 
                            specs=[[{"type": "domain"}, {"type": "domain"}]],
                            subplot_titles=['Population > 30M', 'Population <= 30M'])

              
        # Asian chart
        fig_asia.add_trace(go.Pie(labels=pop_gt_100m_df['country'], values=pop_gt_100m_df['population_2024']),
                    row=1, col=1)
        fig_asia.add_trace(go.Pie(labels=pop_lte_100m_df['country'], values=pop_lte_100m_df['population_2024']),
                    row=1, col=2)
        fig_asia.update_layout(height=800, width=800, 
                               title_text='Asian population distribution',
                               showlegend=True)
        
        
        # European Chart
        fig_eu.add_trace(go.Pie(labels=pop_gt_10m_eu['country'], values=pop_gt_10m_eu['population_2024']),
                    row=1, col=1)
        fig_eu.add_trace(go.Pie(labels=pop_lte_10m_eu['country'], values=pop_lte_10m_eu['population_2024']),
                    row=1, col=2)
        fig_eu.update_layout(height=800, width=800,
                             title_text='Europe population distribution', 
                             showlegend=True)
        
        
        # Africa Chart
        fig_africa.add_trace(go.Pie(labels=pop_gt_35m_africa['country'], values=pop_gt_35m_africa['population_2024']),
                    row=1, col=1)
        fig_africa.add_trace(go.Pie(labels=pop_lte_35m_africa['country'], values=pop_lte_35m_africa['population_2024']),
                    row=1, col=2)
        fig_africa.update_layout(height=800, width=800,
                             title_text='Africa population distribution', 
                             showlegend=True)
        
        
        
        # North America Chart
        fig_nthamrica = px.pie(north_america_df, values='population_2024', names='country')
        fig_nthamrica.update_layout(height=500, width=500,
                             title_text='North America population distribution', 
                             showlegend=True)
        
        
        # South America Chart
        fig_sthamrica = px.pie(south_america_df, values='population_2024', names='country')
        fig_sthamrica.update_layout(height=500, width=500,
                             title_text='South America population distribution', 
                             showlegend=True)
        
        
        st.plotly_chart(fig_asia)
        st.plotly_chart(fig_eu)
        st.plotly_chart(fig_africa)
        st.plotly_chart(fig_nthamrica)
        st.plotly_chart(fig_sthamrica)