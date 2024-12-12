import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
def load_data():
    # Load data from CSV file
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    return df

# 2. Clean the data by filtering out the top and bottom 2.5% of the page views
def clean_data(df):
    # Calculate the 2.5% and 97.5% percentiles for the page views
    lower_percentile = df['page_views'].quantile(0.025)
    upper_percentile = df['page_views'].quantile(0.975)
    
    # Filter out the outliers
    df_cleaned = df[(df['page_views'] >= lower_percentile) & (df['page_views'] <= upper_percentile)]
    
    return df_cleaned

# 3. Draw the line plot for daily page views
def draw_line_plot(df):
    # Create a copy of the dataframe for plotting
    df_line = df.copy()

    # Plot the line chart
    plt.figure(figsize=(12, 6))
    plt.plot(df_line.index, df_line['page_views'], color='blue', lw=1)
    
    # Title and labels
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    # Save the plot as an image
    plt.savefig('line_plot.png')
    plt.show()

# 4. Draw the bar plot for average monthly page views by year
def draw_bar_plot(df):
    # Create a copy of the dataframe for plotting
    df_bar = df.copy()

    # Group by year and month, then calculate the average page views per month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    monthly_avg = df_bar.groupby(['year', 'month'])['page_views'].mean().unstack()

    # Plot the bar chart
    monthly_avg.plot(kind='bar', figsize=(12, 6), width=0.8)

    # Set the title and labels
    plt.title('Average Monthly Page Views by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Save the plot as an image
    plt.savefig('bar_plot.png')
    plt.show()

# 5. Draw the box plot for year-wise and month-wise distribution
def draw_box_plot(df):
    # Create a copy of the dataframe for plotting
    df_box = df.copy()

    # Add year and month columns
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month

    # Create a figure for the box plots
    plt.figure(figsize=(14, 7))

    # Plot the year-wise box plot (Trend)
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='page_views', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    # Plot the month-wise box plot (Seasonality)
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='page_views', data=df_box)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Save the plot as an image
    plt.tight_layout()
    plt.savefig('box_plot.png')
    plt.show()

# Main function to run all the visualizations
def main():
    # Load and clean the data
    df = load_data()
    df_cleaned = clean_data(df)
    
    # Draw the line plot
    draw_line_plot(df_cleaned)
    
    # Draw the bar plot
    draw_bar_plot(df_cleaned)
    
    # Draw the box plot
    draw_box_plot(df_cleaned)

# Run the main function
if __name__ == "__main__":
    main()
