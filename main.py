import requests
import matplotlib.pyplot as plt
import numpy as np

url = "https://corona.lmao.ninja/v2/historical/Bangladesh?lastdays=500"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

Date = []
newCases = []
temp = []
Date.clear()
newCases.clear()
temp.clear()
for i in data['timeline']['cases']:
    temp.append(data['timeline']['cases'][i])
    Date.append(i)

x = 0
for i in range(len(temp)):
    newCases.append(temp[i] - x)
    x = temp[i]

plt.bar(Date, newCases)
plt.xticks(rotation='vertical')
plt.xticks(np.arange(0, len(Date) + 1, 45))
plt.title('Corona Graph')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.grid()

plt.show()
