import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Import data
def load_data():
    df = pd.read_csv('medical_examination.csv')
    return df

# 2. Add overweight column based on BMI
def add_overweight_column(df):
    # BMI = weight (kg) / (height (m))^2
    df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)  # Convert height to meters
    # 1 if overweight, 0 if not
    df['overweight'] = (df['BMI'] > 25).astype(int)
    return df

# 3. Normalize cholesterol and glucose columns
def normalize_data(df):
    # Normalize cholesterol and glucose: 0 for normal, 1 for above normal and well above normal
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
    return df

# 4. Draw the Categorical Plot (catplot)
def draw_cat_plot(df):
    # Create a DataFrame for categorical plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.rename(columns={'variable': 'features', 'value': 'value'})
    
    # Group the data by cardio and features, then count the occurrences
    df_cat = df_cat.groupby(['cardio', 'features', 'value']).size().reset_index(name='count')
    
    # Create the categorical plot
    fig = sns.catplot(data=df_cat, kind='bar', x='features', hue='value', col='cardio', 
                      height=5, aspect=1.5, ci=None)
    fig.set_axis_labels('Features', 'Count')
    fig.set_titles('Cardio = {col_name}')
    
    # Display the plot
    plt.show()
    return fig

# 5. Draw the Heatmap
def draw_heat_map(df):
    # Clean the data by filtering out incorrect data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = corr.where(pd.np.triu(pd.np.ones(corr.shape), k=1).astype(bool))
    
    # Set up the matplotlib figure
    plt.figure(figsize=(12, 10))
    
    # Plot the heatmap
    sns.heatmap(corr, annot=True, fmt='.1f', cmap='coolwarm', mask=mask, linewidths=0.5)
    
    # Display the heatmap
    plt.show()

# Main function to run the entire process
def main():
    # Load the data
    df = load_data()
    
    # Add overweight column based on BMI
    df = add_overweight_column(df)
    
    # Normalize the data
    df = normalize_data(df)
    
    # Draw the categorical plot
    draw_cat_plot(df)
    
    # Draw the heatmap
    draw_heat_map(df)

# Run the main function
if __name__ == "__main__":
    main()
