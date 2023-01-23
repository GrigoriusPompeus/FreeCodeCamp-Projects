import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(10,10))
    plt.scatter(x, y)


    # Create first line of best fit
    # This lane uses more data than the second one (from 1880)
    predicted_line = linregress(x,y)
    x_pred = pd.Series([i for i in range(1880, 2055)])
    y_pred = predicted_line.slope*x_pred + predicted_line.intercept
    plt.plot(x_pred, y_pred, 'r',label = "Line of best fit using data from 1880")

  
    # Create second line of best fit
    # this line uses less data(from 1930)
    worse_prediction = df.loc[df['Year'] >= 1930]
    x_worse = worse_prediction['Year']
    y_worse = worse_prediction['CSIRO Adjusted Sea Level']

    second_line = linregress(x_worse,y_worse)
    x2_pred = pd.Series([i for i in range(1880, 2055)])
    y2_pred = second_line.slope *x2_pred + second_line.intercept
    plt.plot(x2_pred, y2_pred, 'b',label = "Line of best fit using data from 1930")

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year', fontsize = 13)
    ax.set_ylabel('Sea Level (inches)', fontsize = 13)
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()