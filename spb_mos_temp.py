
import csv
from matplotlib import pyplot as plt
from datetime import datetime
import io

import funcs

# dates_temp = funcs.days_generator()

# ##############-ПИТЕР-##########################
dates_1, highs_1 = funcs.reprint('archives/2013.csv')
dates_2, highs_2 = funcs.reprint('archives/2014.csv')
dates_3, highs_3 = funcs.reprint('archives/2015.csv')
dates_4, highs_4 = funcs.reprint('archives/2016.csv')
dates_5, highs_5 = funcs.reprint('archives/2017.csv')
dates_6, highs_6 = funcs.reprint('archives/2018.csv')
dates_7, highs_7 = funcs.reprint('archives/2012.csv')
dates_8, highs_8 = funcs.reprint('archives/2011.csv')
dates_9, highs_9 = funcs.reprint('archives/2010.csv')
dates_10, highs_10 = funcs.reprint('archives/2009.csv')

highs_all = []
for i in range(2920):
    ha = 0
    ha += (highs_1[i] + highs_2[i] + highs_3[i])
    ha += (highs_4[i] + highs_5[i] + highs_6[i])
    ha += (highs_7[i] + highs_8[i] + highs_9[i] + highs_10[i])
    ha = (ha / 10)
    highs_all.append(ha)

################################################


# ##############-MOSCOW-##########################
dates_dic = funcs.reprint_2('archives/mos_all.csv')
dates = []
highs = []
i = 0.0

for a, b in dates_dic.items():
    dates.append(a)
    i = 0.0
    for x in b:
        i += float(x)
    # print(i, len(b), )
    i = round((i / len(b)), 1)
    highs.append(i)

# for a, b in dates_dic.items():
#     print(b)

# for i in range(0, len(highs) + 1, 7):
#     print(dates[i], ' ', highs[i])

# ###############################################


fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates_1, highs_all, c='red', alpha=0.9, linewidth=1)
plt.plot(dates, highs, c='blue', alpha=0.6, linewidth=1)

plt.title('Average daily temp. in St.-Petersburg 2009 - 2018', fontsize=14)
plt.xlabel('', fontsize=9)
fig.autofmt_xdate()
plt.ylabel('Max temp', fontsize=9)
plt.tick_params(axis='both', which='minor', labelsize=9)
plt.show()





