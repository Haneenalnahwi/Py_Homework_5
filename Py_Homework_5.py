import pandas as pd
import matplotlib.pyplot as plt

Covid19_Cases = pd.read_csv("Covid19_Cases.csv")

Covid19_Cases['date'] = pd.to_datetime(Covid19_Cases['date'], infer_datetime_format=True)

Armenia_cases = Covid19_Cases[Covid19_Cases['country'] == 'Armenia']
Spain_cases = Covid19_Cases[Covid19_Cases['country'] == 'Spain']
Switzerland_cases = Covid19_Cases[Covid19_Cases['country'] == 'Switzerland']
UK_cases = Covid19_Cases[Covid19_Cases['country'] == 'United Kingdom']



plt.figure(figsize=(12, 7))
plt.plot(Armenia_cases["date"], Armenia_cases["total_cases"],linewidth=2, color='red')
plt.plot(Spain_cases["date"], Spain_cases["total_cases"],linewidth=2, color='green')
plt.plot(Switzerland_cases["date"], Switzerland_cases["total_cases"],linewidth=2, color='blue')
plt.plot(UK_cases["date"], UK_cases["total_cases"],linewidth=2, color='purple')
plt.title('Coronavirues cases in European Countries')
plt.legend(["Armenia", "Spain", "Switzerland", "UK"])
plt.xlabel('Month - Year')
plt.ylabel('Total Cases')
plt.show()

