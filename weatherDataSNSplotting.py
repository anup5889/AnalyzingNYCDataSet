__author__ = 'anupdudani'

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
WeatherDF=pd.read_csv("/Users/anupdudani/Documents/UdacityWork/NYCProject/improved-dataset/turnstile_weather_v2.csv")


plt.figure()
ax=sns.barplot(x=WeatherDF["weekday"],y=WeatherDF['ENTRIESn_hourly'],hue=WeatherDF["conds"])
ax.set(xlabel="Weekend-0, Weekday-1", ylabel="Hourly Entries")
sns.plt.title('Entries on Weekday vs Weekend based on different weather conds')
#sns.factorplot(x=WeatherDF["hour"], y=WeatherDF['ENTRIESn_hourly'], hue=WeatherDF["rain"], kind="bar", palette="muted")
plt.show()