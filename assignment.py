import json
import collections
import pandas as pd
import matplotlib.pyplot as plt
import requests

f = open('data.json')

data = json.load(f)

rates = (data['rates'])

od = collections.OrderedDict(sorted(rates.items()))
datelist = list(od.keys())

val = list(rates.values())

df = pd.DataFrame(val, index=datelist)

#####################################################
############# Task 1 T-1 ############################
#####################################################

inr = (df.loc[:, 'INR'])
inrval = (list(inr))

plt.plot(datelist[:30], inrval[:30])

plt.xlabel('Dates')
plt.ylabel('Exchange rates EUR to INR')

plt.show()

#####################################################
############# Task 2 T-2 ############################
#####################################################

gbp = df.loc[:, 'GBP']
gbpval = list(gbp)

plt.plot(datelist[:30], gbpval[:30])

plt.xlabel('Dates')
plt.ylabel('Exchange rates EUR to INR')


plt.show()

#####################################################
############# Task 3 T-3 ############################
#####################################################

response = requests.get("https://api.exchangeratesapi.io/latest")
data = response.json()
latest = dict(data)
rates = latest['rates']
gbp = rates['GBP']
inr = rates['INR']

plt.plot(datelist[:30], inrval[:30])
plt.plot(datelist[:30], gbpval[:30])
plt.xlabel('Dates')
plt.ylabel('Exchange rates EUR to INR')
str1 = "Current value of EUR to INR is " + str(inr)
str2 = "Current value of EUR to GBP is " + str(gbp)
plt.text(3, 8, str1)
plt.text(3, 13, str2)
plt.show()
