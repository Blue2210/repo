import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Step 1: Load the data
def load_data():
    # Load the data from the CSV file
    df = pd.read_csv('epa-sea-level.csv')
    return df

# Step 2: Create the scatter plot
def create_scatter_plot(df):
    # Create the scatter plot using the Year and CSIRO Adjusted Sea Level columns
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')
    
# Step 3: Create the first line of best fit (using all data)
def create_line_of_best_fit(df):
    # Perform linear regression on the data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Plot the line of best fit (from the data)
    years_extended = range(df['Year'].min(), 2051)  # To extend to year 2050
    sea_level_fit = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_level_fit, label='Best Fit Line (1880-2014)', color='red')

# Step 4: Create the second line of best fit (using data from 2000 onward)
def create_recent_line_of_best_fit(df):
    # Filter data from the year 2000 onward
    df_recent = df[df['Year'] >= 2000]
    
    # Perform linear regression on the recent data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Plot the second line of best fit (from 2000 onward)
    sea_level_fit_recent = [slope_recent * year + intercept_recent for year in range(2000, 2051)]
    plt.plot(range(2000, 2051), sea_level_fit_recent, label='Best Fit Line (2000-2014)', color='green')

# Step 5: Finalize the plot
def finalize_plot():
    # Set title and labels
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Add legend to the plot
    plt.legend()
    
    # Save the plot
    plt.savefig('sea_level_predictor.png')
    plt.show()

# Main function to run all tasks
def main():
    # Load the data
    df = load_data()
    
    # Create the scatter plot
    create_scatter_plot(df)
    
    # Create both lines of best fit
    create_line_of_best_fit(df)
    create_recent_line_of_best_fit(df)
    
    # Finalize and display the plot
    finalize_plot()

# Run the main function
if __name__ == "__main__":
    main()
