import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(
        'adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

   # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    # 1. selects bachelors degrees
    bach_select = df[df['education'] == 'Bachelors']
    num_bach = len(bach_select)  # 2. counts bachelors degrees
    total_people = len(df)  # 3. count total people
    percentage_bachelors = (num_bach / total_people) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate'
    # WITH
    high_ed = df[df['education'].isin(['Bachelors', 'Doctorate', 'Masters'])]
    num_high_ed = len(high_ed)

    high_ed_over50 = df[df['education'].isin(
        ['Bachelors', 'Doctorate', 'Masters']) & (df['salary'] == '>50K')]
    num_high_ed_over50 = len(high_ed_over50)

    # WITHOUT
    low_ed = df[~df['education'].isin(['Bachelors', 'Doctorate', 'Masters'])]
    num_low_ed = len(low_ed)
    low_ed_over50 = df[~df['education'].isin(
        ['Bachelors', 'Doctorate', 'Masters']) & (df['salary'] == '>50K')]
    num_low_ed_over50 = len(low_ed_over50)

    # percentage with salary >50K
    higher_education_rich = (num_high_ed_over50 / num_high_ed) * 100
    lower_education_rich = (num_low_ed_over50 / num_low_ed) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = df['hours-per-week'].min()  # find min hours worked

    # select and count workers who worked min hours
    min_hours_group = df[df['hours-per-week'] == min_hours]
    num_min_workers = len(min_hours_group)

    # count how many min hour workers made over 50K
    min_hours_over50K = (min_hours_group['salary'] == '>50K').sum()

    # calculate percentage
    rich_percentage = (min_hours_over50K / num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    NSgrouped = df.groupby(
        'native-country')['salary'].value_counts().unstack(fill_value=0)
    NSgrouped['Percent_over50'] = (
        NSgrouped['>50K'] / NSgrouped.sum(axis=1))*100

    highest_earning_country = NSgrouped['Percent_over50'].idxmax()
    highest_earning_country_percentage = NSgrouped['Percent_over50'].max()

    # Identify the most popular occupation for those who earn >50K in India.
    filter_df = df[(df['salary'] == '>50K') & (
        df['native-country'] == 'India')]

    count_occupation = filter_df['occupation'].value_counts()

    top_IN_occupation = count_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()
