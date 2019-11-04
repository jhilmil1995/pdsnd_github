import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    list_of_cities = ['chicago', 'new york city', 'washington']
    while city not in list_of_cities:
        city = input('Enter name of the city to analyze:\n')

    # get user input for month (all, january, february, ... , june)
    month = ''
    list_of_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 
            'august', 'september', 'october', 'november', 'december']
    while month not in list_of_months:
        month = input('Enter month to filter by, or "all" to apply no month filter:\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = -1
    while day < 0 or day > 7:
        try:
            day = int(input('Enter an integer to represent day of week to filter by, or "0" to apply no day filter:\n'))
        except:
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv('./{}.csv'.format(city.lower().replace(" ", "_")))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # get month and day of week 
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day'] = df['Start Time'].dt.dayofweek

    if month != 'all': 
        # apply month filter
         df = df[df['month'] == month]
    if day != 'all': 
        # apply day filter
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most Commonly Month:\n', df['month'].mode()[0])

    # display the most common day of week
    print('Most Commonly Day of Week:\n', df['day'].mode()[0])

    # display the most common start hour
    start_hour = df['Start Time'].dt.hour
    print('Most Commonly Start hour:\n', start_hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

        
    # display most commonly used start station
    start_station = df['Start Station']
    print('Most Commonly Used Start Station:\n', start_station.mode()[0])

    # display most commonly used end station
    end_station = df['End Station']
    print('Most Commonly Used End Station:\n', end_station.mode()[0])

    df['Station Combinations'] = start_station +  ' and ' + end_station
    # display most frequent combination of start station and end station trip
    print('Most Frequent Combination of Start Station and End Station Trip:\n', df['Station Combinations'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Travel Time'] = df['End Time'] -  df['Start Time']
    print('Total Travel Time:\n', df['Travel Time'].sum())

    # display mean travel time
    print('Mean Travel Time:\n', df['Travel Time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of User Type:\n',  user_types)

    # Display counts of gender
    if ('Gender' in df):
        gender = df.groupby(['Gender']).size()
        print('Count of gender:\n', gender)

    # Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df):
        birth_year = df['Birth Year']
        print('Earliest Birth Year:\n', birth_year.min())
        print('Most Recent Birth Year:\n', birth_year.max())
        print('Most Common Birth Year:\n', birth_year.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
