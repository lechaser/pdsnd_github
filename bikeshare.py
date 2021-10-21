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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # ask the user for input
    city = input("Please type the city name you want to get results:\n").lower()

    # our list of cities
    cities = ['chicago', 'new york city', 'washington']

    # try again while input value is not in our list
    while city not in cities:
        city = input("Your city wasn't found in our inventory. Please try another city:\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    # ask the user for input
    month = input("Please type the month you want to get results: (use all for all)\n").lower()

    # our list of months
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    # try again while input value is not in our list
    while month not in months:
        month = input("the month typed is not correct. Please, try again!\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    # ask the user for input
    day = input("Please type the day of the week you want to get results: (use all for all)\n").lower()

    # our list of days
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # try again while input value is not in our list
    while month not in month_list:
        day = input("the day typed is not correct. Please, try again!\n").lower()

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

    # loading the data for the selected city
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # creating a new column for month values
    df['Month'] = pd.DatetimeIndex(df['Start Time']).month

    # creating a new column for week day values
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Week Day'] = df['Start Time'].dt.day_name().str.lower()

    # we are going to filter first by the selected month
    # get rows by month
    if month != 'all':
        # format the input month to int
        month_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_list.index(month) + 1

        # returning our df filtered by the selected month
        df = df.loc[df['Month'] == month,:]

    # we are going to filter now by the selected week day
    # get rows by week day
    if day != 'all':
        # returning our df filtered by the selected week day
        df = df.loc[df['Week Day'] == day,:]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # get the most common month as int
    most_c_month = int(df['Month'].mode().values[0])

    # convert our int into a month name
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    month = month_list[most_c_month-1]

    # show the result
    print("The most common month was", month, '\n')

    # TO DO: display the most common day of week

    # show the result after getting the string of most common day
    print("The", str(df['Week Day'].mode().values[0]), "was the most common day of the week\n")

    # TO DO: display the most common start hour

    # creating new column with hour value 'Start Time'
    df['Start Hour'] = df['Start Time'].dt.hour
    print("At", str(df['Start Hour'].mode().values[0]), "was the most common start hour\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode().values[0], "was the most common start station\n")

    # TO DO: display most commonly used end station
    print(df['End Station'].mode().values[0], "was the most common end station\n")

    # TO DO: display most frequent combination of start station and end station trip

    # creating new column with combination of start and end as route string
    df['Route'] = "From " + df['Start Station']+ " to " + df['End Station']

    # display the most frequent route
    print(df['Route'].mode().values[0], "is the most frequent route\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # users total travel time
    total_trip = df['Trip Duration'].sum()

    # converting into days, hours, minutes and seconds
    d = int(total_trip/86400)
    h = int((total_trip-(d*86400))/3600)
    m = int((total_trip-(d*86400)-(h*3600))/60)
    s = total_trip-(d*86400)-(h*3600)-(m*60)

    # display the total time formated
    print("Time spent by our users is", d, "days", h, "hours", m, "minutes", s, "seconds.\n")


    # TO DO: display mean travel time

    # users mean travel time
    mean_trip = df['Trip Duration'].mean()

    # converting into minutes and seconds
    m = int(mean_trip/60)
    s = mean_trip-(m*60)

    # display the mean time formated
    print("The mean time of a journey is", m, "minutes", s, "seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts = df['User Type'].value_counts()

    # Display the data
    print("These are counts of our user types:\n", counts.to_string(), '\n')

    # TO DO: Display counts of gender

    # Whashintong doesn´t have 'Gender' attribute, so it won't show its data
    if city != 'washington':

        counts = df['Gender'].value_counts()

        # Display the data
        print("These are counts of our user gender:\n", counts.to_string(), '\n')

    # TO DO: Display earliest, most recent, and most common year of birth

    # Neither Whashintong has 'Birth Year' as atribute

        # Display earliest birth year
        print("The earliest birth year is", int(df['Birth Year'].min()), '\n')

        # Display most recent birth year
        print("The most recent birth year is", int(df['Birth Year'].max()), '\n')

        # Display most recent birth year
        print("The most common birth year is", int(df['Birth Year'].mode()), '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Please create a new function here, for example, called display_data. You need to ask the user whether he
    wants to see 5 rows of data. We will show all parts of the analysis then we will ask this question: Do you
    want to see 5 rows of data. But it is not only the first 5 data but as much as the user wants.

    """

    # innitial display input message
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    answer = ['yes', 'no']

    while view_data not in answer:
        view_data = input('\nWrong Answer!.Please, Enter yes or no\n').lower()

    # counter
    start_loc = 0

    # loop
    if view_data == 'yes':
        while start_loc <= df.shape[0] - 1:
            print(df.iloc[start_loc:start_loc+5,:])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
            while view_data not in answer:
                view_data = input('\nWrong Answer!.Please, Enter yes or no\n').lower()

            if view_data == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
