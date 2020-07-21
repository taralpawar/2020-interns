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
plt.title('Exchange rates EUR to INR')

plt.show()

#####################################################
############# Task 2 T-2 ############################
#####################################################

gbp = df.loc[:, 'GBP']
gbpval = list(gbp)

plt.plot(datelist[:30], gbpval[:30])

plt.xlabel('Dates')
plt.ylabel('Exchange rates EUR to GBP')
plt.title('Exchange rates EUR to GBP')


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

plt.plot(datelist[:30], inrval[:30], label="EURtoINR")
plt.plot(datelist[:30], gbpval[:30], label="EURtoGBP")
plt.xlabel('Dates')
plt.ylabel('Exchange rates EUR to INR')
plt.title('Exchange rates of EUR to INR and GBP')
plt.legend()

str1 = "Current value of EUR to INR is " + str(inr)
str2 = "Current value of EUR to GBP is " + str(gbp)
plt.text(3, 8, str1)
plt.text(3, 13, str2)
plt.show()

#####################################################
############# Task 4 T-4 ############################
#####################################################


response = requests.get(
    "https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-01-31")
data = dict(response.json())

rates = data['rates']
od = collections.OrderedDict(sorted(rates.items()))
datelist = list(od.keys())

val = list(rates.values())

df = pd.DataFrame(val, index=datelist)

inr = (df.loc[:, 'INR'])
inrval = (list(inr))

plt.plot(datelist, inrval)


plt.xlabel('Dates')
plt.ylabel('Exchange rates EUR to INR')
plt.title("Exchange rates from REST endpoint")
plt.show()

#####################################################
############# Feature F-1 ###########################
#####################################################


print("Enter the start date (yyyy/mm/dd)")
sdate = input()
print("Enter the end date (yyyy/mm/dd)")
edate = input()

response = requests.get(
    "https://api.exchangeratesapi.io/history?start_at={}&end_at={}".format(sdate, edate))
data = dict(response.json())

data = dict(response.json())

rates = data['rates']
od = collections.OrderedDict(sorted(rates.items()))
datelist = list(od.keys())

val = list(rates.values())

df = pd.DataFrame(val, index=datelist)

inr = (df.loc[:, 'INR'])
inrval = (list(inr))

plt.plot(datelist, inrval)

plt.title("Exchange rate of EUR to INR from {} to {}".format(sdate, edate))
plt.xlabel('Dates')
plt.ylabel('Exchange rates')

plt.show()

#####################################################
############# Feature F-2 ###########################
#####################################################


print("Enter the start date (yyyy/mm/dd)")
sdate = input()
print("Enter the end date (yyyy/mm/dd)")
edate = input()

print("Enter the currency symbol")
sym = input()

response = requests.get(
    "https://api.exchangeratesapi.io/history?start_at={}&end_at={}&symbols={}".format(sdate, edate, sym))

data = dict(response.json())

rates = data['rates']
od = collections.OrderedDict(sorted(rates.items()))
datelist = list(od.keys())

val = list(rates.values())

df = pd.DataFrame(val, index=datelist)

symval = df.loc[:, sym]

plt.plot(datelist, symval)

plt.title("Exchange rate of EUR to {} from {} to {}".format(sym, sdate, edate))
plt.xlabel('Dates')
plt.ylabel('Exchange rates')

plt.show()
