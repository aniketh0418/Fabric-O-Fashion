import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def create_bar_chart(data, x, y, title):
    """
    Creates a styled bar chart
    """
    fig = px.bar(
        data,
        x=x,
        y=y,
        title=title,
        template="plotly_dark"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#ffffff'
    )
    
    return fig

def create_pie_chart(data, values, names, title):
    """
    Creates a styled pie chart
    """
    fig = px.pie(
        data,
        values=values,
        names=names,
        title=title,
        template="plotly_dark"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#ffffff'
    )
    
    return fig

def create_line_chart(data, x, y, title):
    """
    Creates a styled line chart
    """
    fig = px.line(
        data,
        x=x,
        y=y,
        title=title,
        template="plotly_dark"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#ffffff'
    )
    
    return fig

def create_scatter_plot(data, x, y, color=None, size=None, title=""):
    """
    Creates a styled scatter plot
    """
    fig = px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        size=size,
        title=title,
        template="plotly_dark"
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#ffffff'
    )
    
    return fig