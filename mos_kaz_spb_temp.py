
import csv
from matplotlib import pyplot as plt
from datetime import datetime
import io

import funcs

# dates_temp = funcs.days_generator()

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

# ################-SPB-###########################
dates_2_dic = funcs.reprint_2('archives/spb_all.csv')
dates_2 = []
highs_2 = []
i = 0.0

for a, b in dates_2_dic.items():
    dates_2.append(a)
    i = 0.0
    for x in b:
        i += float(x)
    # print(i, len(b), )
    i = round((i / len(b)), 1)
    highs_2.append(i)

# for a, b in dates_2_dic.items():
#     print(b)

# for i in range(0, len(highs_2) + 1, 7):
#     print(dates_2[i], ' ', highs_2[i])

# ###############################################

# ##############-KAZAN-##########################
dates_3_dic = funcs.reprint_2('archives/kaz_all.csv')
dates_3 = []
highs_3 = []
i = 0.0

for a, b in dates_3_dic.items():
    dates_3.append(a)
    i = 0.0
    for x in b:
        i += float(x)
    # print(i, len(b), )
    i = round((i / len(b)), 1)
    highs_3.append(i)

# for a, b in dates_3_dic.items():
#     print(b)

# for i in range(0, len(highs_3) + 1, 7):
#     print(dates_3[i], ' ', highs_3[i])

###############################################

fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs, c='red', alpha=1, linewidth=1)
plt.plot(dates_2, highs_2, c='blue', alpha=0.7, linewidth=1)
plt.plot(dates_3, highs_3, c='green', alpha=0.5, linewidth=1)

plt.title('Average temp.. red-mos, blue-spb, green-kaz, 36 years', fontsize=14)
plt.xlabel('', fontsize=9)
fig.autofmt_xdate()
plt.ylabel('Max temp', fontsize=9)
plt.tick_params(axis='both', which='minor', labelsize=9)
plt.show()





