#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:40:23 2020

@author: boyichen
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp

data = pd.read_csv("time_series_covid19_confirmed_US.csv")
dates = data.columns[11:].tolist()
total = data.iloc[:,11:].sum().values.tolist()

diff = []
for i in range(len(total)-1):
    diff.append(total[i+1]-total[i])

max_diff = [max(diff)] * len(total)

fig, ax1 = plt.subplots()
cmap = plt.get_cmap("YlOrRd")
data_normalizer = mp.colors.Normalize()
color = cmap(data_normalizer(diff))
ax1.bar(dates, max_diff, align="edge", width=1, color=color, alpha=1, tick_label=None)
ax1.axes.yaxis.set_visible(False)

ax2 = ax1.twinx()
ax2.plot(dates, total)
ax2.set_ylabel("total confirmed cases")
ax2.yaxis.set_major_formatter(mp.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax2.yaxis.set_label_position("left")
ax2.yaxis.tick_left()

ax1.set_xticks(dates[::30])
ax1.tick_params(axis="x", labelrotation=30)

fig.tight_layout()
# plt.show()

filename = "US-{}.png".format(dates[-1]).replace("/", "-")
plt.savefig(filename)