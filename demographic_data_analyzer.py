import pandas as pd

# Load the dataset (Assuming the file is named 'census_data.csv')
def load_data():
    # Read the CSV into a DataFrame
    df = pd.read_csv("census_data.csv")
    return df

# 1. How many people of each race are represented in this dataset? (Pandas Series with race names as index labels)
def race_count(df):
    return df['race'].value_counts()

# 2. What is the average age of men?
def average_age_men(df):
    men_df = df[df['sex'] == 'Male']
    return round(men_df['age'].mean(), 1)

# 3. What is the percentage of people who have a Bachelor's degree?
def percentage_bachelors(df):
    bachelors_df = df[df['education'] == 'Bachelors']
    return round((len(bachelors_df) / len(df)) * 100, 1)

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
def percentage_high_salary_with_education(df):
    advanced_education_df = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_salary_advanced_education_df = advanced_education_df[advanced_education_df['salary'] == '>50K']
    return round((len(high_salary_advanced_education_df) / len(advanced_education_df)) * 100, 1)

# 5. What percentage of people without advanced education make more than 50K?
def percentage_high_salary_without_education(df):
    no_advanced_education_df = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_salary_no_education_df = no_advanced_education_df[no_advanced_education_df['salary'] == '>50K']
    return round((len(high_salary_no_education_df) / len(no_advanced_education_df)) * 100, 1)

# 6. What is the minimum number of hours a person works per week?
def min_work_hours(df):
    return df['hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
def percentage_of_min_workers_with_high_salary(df):
    min_hours = df['hours-per-week'].min()
    min_hours_df = df[df['hours-per-week'] == min_hours]
    high_salary_min_hours_df = min_hours_df[min_hours_df['salary'] == '>50K']
    return round((len(high_salary_min_hours_df) / len(min_hours_df)) * 100, 1)

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
def country_with_highest_salary_percentage(df):
    countries = df['native-country'].unique()
    highest_percentage = 0
    highest_country = ''
    
    for country in countries:
        country_df = df[df['native-country'] == country]
        high_salary_country_df = country_df[country_df['salary'] == '>50K']
        percentage = (len(high_salary_country_df) / len(country_df)) * 100
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_country = country
    
    return highest_country, round(highest_percentage, 1)

# 9. Identify the most popular occupation for those who earn >50K in India.
def top_in_india(df):
    india_df = df[df['native-country'] == 'India']
    high_salary_india_df = india_df[india_df['salary'] == '>50K']
    top_occupation = high_salary_india_df['occupation'].mode()[0]
    return top_occupation

def main():
    # Load data
    df = load_data()

    # Answer all questions
    print("Race count:")
    print(race_count(df))
    print("\nAverage age of men:", average_age_men(df))
    print("\nPercentage with Bachelors degree:", percentage_bachelors(df))
    print("\nPercentage of people with advanced education earning >50K:", percentage_high_salary_with_education(df))
    print("\nPercentage of people without advanced education earning >50K:", percentage_high_salary_without_education(df))
    print("\nMinimum work hours:", min_work_hours(df))
    print("\nPercentage of people working minimum hours with salary >50K:", percentage_of_min_workers_with_high_salary(df))
    print("\nCountry with highest percentage of high earners:", country_with_highest_salary_percentage(df))
    print("\nMost popular occupation for those earning >50K in India:", top_in_india(df))

if __name__ == "__main__":
    main()
