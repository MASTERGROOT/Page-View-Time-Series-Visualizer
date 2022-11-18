import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
import datetime

df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date',parse_dates=['date'])

df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    df_line = df.copy()
    fig , ax = plt.subplots(figsize=(20,10))
    graph = sb.lineplot(data=df_line, x='date', y='value', color='red')
    graph.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    graph.set_xlabel('Date')
    graph.set_ylabel('Page Views')
    fig.savefig('line_plot')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar.rename(columns={'value' : 'Average Page Views'}, inplace = True)
    df_bar['Months'] = df_bar.index.month_name()
    df_bar['Years'] = df_bar.index.year

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig , ax = plt.subplots(figsize=(20,10))
    sb.barplot(data=df_bar,x='Years',y='Average Page Views',hue='Months',palette="tab10",errorbar=None,hue_order=months)
    plt.legend(loc='upper left', title='Months')

    fig.savefig('bar_plot')
    return fig

def draw_box_plot():
    df_box = df.copy()
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box.rename(columns={'value' : 'Page Views'}, inplace = True)
    df_box['Month'] = df.index.month_name().str.slice(stop=3)
    
    df_box['Year'] = df.index.year
    fig , ax = plt.subplots(nrows=1,ncols=2,figsize=(20,10))
    sb.boxplot(data=df_box,x='Year', y='Page Views', ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    
    sb.boxplot(data=df_box,x='Month', y='Page Views', ax=ax[1], order=months)
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    
    fig.savefig('box_plot')
    return fig


