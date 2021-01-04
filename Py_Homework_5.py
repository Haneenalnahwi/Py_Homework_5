import pandas as pd
import matplotlib.pyplot as plt


Covid19_Cases = pd.read_csv("Covid19_Cases.csv")        #Reading the dataset of Covid19

Covid19_Cases['date'] = pd.to_datetime(Covid19_Cases['date'], infer_datetime_format=True)   #Converting date to real date in order to deal with it
                                                                                        #Finding weekends from dates
Covid19_Cases['Weekend'] = (Covid19_Cases['date'].dt.day_name() == 'Saturday') | \
                           (Covid19_Cases['date'].dt.day_name() == 'Sunday')

Armenia_cases = Covid19_Cases[Covid19_Cases['country'] == 'Armenia']                        #Taking data for each selected country
Spain_cases = Covid19_Cases[Covid19_Cases['country'] == 'Spain']
Switzerland_cases = Covid19_Cases[Covid19_Cases['country'] == 'Switzerland']
UK_cases = Covid19_Cases[Covid19_Cases['country'] == 'United Kingdom']


Countries_Cases = {'Armenia': Armenia_cases,                                #defining a dictionary to loop over countries
                   'Spain': Spain_cases,
                   'Switzerland': Switzerland_cases,
                   'United Kingdom': UK_cases
}
Cases_Mean = {}
for Country in Countries_Cases:                                              #Finding Cases in weekends and other days
    Weekend_Cases = Countries_Cases[Country]['new_cases'][Countries_Cases[Country]['Weekend'] == True]
    Days_Cases = Countries_Cases[Country]['new_cases'][Countries_Cases[Country]['Weekend'] == False]
    Weekend_mean = Weekend_Cases.mean()
    Days_mean = Days_Cases.mean()
    Cases_Mean[Country] = [Weekend_mean, Days_mean]

for Country in Cases_Mean:                                                 #Comparing between weekend cases and other days cases and printing the result
    if Cases_Mean[Country][0] > Cases_Mean[Country][1]:
        print('Cases in', Country, 'is increasing in Weekends')
    else:
        print('Cases in', Country, 'is decreasing in Weekends')

plt.figure(figsize=(12, 7))                                                                 #determining the size of the plot figure

plt.plot(Armenia_cases['date'], Armenia_cases['total_cases'],linewidth=2, color='red')      #plotting total covid19 cases for the 4 European Countries among several months
plt.plot(Spain_cases['date'], Spain_cases['total_cases'],linewidth=2, color='green')
plt.plot(Switzerland_cases['date'], Switzerland_cases['total_cases'],linewidth=2, color='blue')
plt.plot(UK_cases['date'], UK_cases['total_cases'],linewidth=2, color='purple')
plt.title('Coronavirues cases in European Countries')
plt.legend(['Armenia', 'Spain', 'Switzerland', 'UK'])
plt.xlabel('Month - Year')
plt.ylabel('Total Cases')

plt.show()
