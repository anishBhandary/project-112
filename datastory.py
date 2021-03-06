# -*- coding: utf-8 -*-
"""dataStory.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UdxxF5OGC44JVlnpC_j0KJSHzI176GI_
"""

import pandas as pd
import statistics
import plotly.express as px
import numpy as np

from google.colab import files

data_to_upload = files.upload()

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("data_store.csv")
fig = px.scatter(df,y = "quant_saved",color = "highschool_completed")
fig.show()

import csv
import plotly.graph_objects as go

with open("data_store.csv",newline = "")as f:
  reader = csv.reader(f)
  saving_data = list(reader)

saving_data.pop(0)

total_entries = len(saving_data)
people_completed_highschool = 0

for x in saving_data:
  if int(x[3])==1:
    people_completed_highschool +=1

fig = go.Figure(go.Bar(x =["highschool_completed","highschool_not_completed"],y = [people_completed_highschool,total_entries - people_completed_highschool]))
fig.show()

all_savings = []
for x in saving_data:
  all_savings.append(float(x[0]))

print("Mean of the All Savings",statistics.mean(all_savings))
print("Median of the All Savings",statistics.median(all_savings))
print("Mode of the All Savings",statistics.mode(all_savings))
print("Std_deviation of the All Savings",statistics.stdev(all_savings))

rem_savings = []
not_rem_savings = []

for x in saving_data:
  if int(x[3])==1:
    rem_savings.append(float(x[0]))
  else:
    not_rem_savings.append(float(x[0]))

print("Mean of the Remainder Savings",statistics.mean(rem_savings))
print("Median of the Remainder Savings",statistics.median(rem_savings))
print("Mode of the Remainder Savings",statistics.mode(rem_savings))
print("Std_deviation of the Remainder Savings",statistics.stdev(rem_savings))

print("Mean of the Non-Remainder Savings",statistics.mean(not_rem_savings))
print("Median of the Non-Remainder Savings",statistics.median(not_rem_savings))
print("Mode of the Non-Remainder Savings",statistics.mode(not_rem_savings))
print("Std_deviation of the Non-Remainder Savings",statistics.stdev(not_rem_savings))

import numpy as np


age = []
savings = []

for x in saving_data:
  age.append(float(x[0]))
  savings.append(float(x[0]))

Correlation = np.corrcoef(age,savings)
print("Correlation of highschool",Correlation[0,1])

import plotly.figure_factory as ff

fig = ff.create_distplot([df["quant_saved"].to_list()],["highschool_completed"],show_hist = False)
fig.show()

