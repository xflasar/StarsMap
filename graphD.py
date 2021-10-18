import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
fig_size = plt.rcParams["figure.figsize"]
cm = 1/2.54
fig_size[0] = 25*cm
fig_size[1] = 17*cm
plt.rcParams["figure.figsize"] = fig_size
def gitRadius(mag):
    return np.log((mag)**4 + 1)
def gitTitleNum(mag):
    if(mag >= 6.76 and mag <= 7.25):
        return 1
    elif (mag >= 6.26 and mag <= 6.75):
        return 2
    elif (mag >= 5.76 and mag <= 6.25):
        return 3
    elif (mag >= 5.26 and mag <= 5.75):
        return 4
    elif (mag >= 4.76 and mag <= 5.25):
        return 5
    elif (mag >= 4.26 and mag <= 4.75):
        return 6
    elif (mag >= 3.76 and mag <= 4.25):
        return 7
    elif (mag >= 3.26 and mag <= 3.75):
        return 8
    elif (mag >= 2.76 and mag <= 3.25):
        return 9
circles = [
    {'r':gitRadius(5.45), 'points': [-13488,87442], 'magnitude': 5.45},
    {'r':gitRadius(3.7), 'points': [-13493,86808], 'magnitude': 3.7},
    {'r':gitRadius(5.65), 'points': [-13510,89421], 'magnitude': 5.65},
    {'r':gitRadius(4.3), 'points': [-13512,88082], 'magnitude': 4.3},
    {'r':gitRadius(6.85), 'points': [-13549,83328], 'magnitude': 6.85},
    {'r':gitRadius(3.88), 'points': [-13550,87724], 'magnitude': 3.88},
    {'r':gitRadius(5.76), 'points': [-13554,88397], 'magnitude': 5.76},
    {'r':gitRadius(6.42), 'points': [-13563,88300], 'magnitude': 6.42},
    {'r':gitRadius(4.18), 'points': [-13580,86217], 'magnitude': 4.18},
    {'r':gitRadius(6.81), 'points': [-13619,88273], 'magnitude': 6.81},
    {'r':gitRadius(6.99), 'points': [-13641,85693], 'magnitude': 6.99},
    {'r':gitRadius(6.3), 'points': [-13641,86818], 'magnitude': 6.3},
    {'r':gitRadius(2.87), 'points': [-13649,86778], 'magnitude': 2.87},
    {'r':gitRadius(6.81), 'points': [-13649,87439], 'magnitude': 6.81},
    {'r':gitRadius(6.46), 'points': [-13687,89959], 'magnitude': 6.46},
    {'r':gitRadius(5.44), 'points': [-13701,84316], 'magnitude': 5.44},
    {'r':gitRadius(6.94), 'points': [-13710,87643], 'magnitude': 6.94},
    {'r':gitRadius(6.6), 'points': [-13737,85886], 'magnitude': 6.6},
    {'r':gitRadius(3.63), 'points': [-13750,86592], 'magnitude': 3.63},
    {'r':gitRadius(5.1), 'points': [-13751,86892], 'magnitude': 5.1},
    {'r':gitRadius(6.62), 'points': [-13762,87770], 'magnitude': 6.62},
    {'r':gitRadius(6.16), 'points': [-13784,85362], 'magnitude': 6.16},
    {'r':gitRadius(6.74), 'points': [-13798,85855], 'magnitude': 6.74},
    {'r':gitRadius(6.93), 'points': [-13852,86263], 'magnitude': 6.93},
]
fig,ax = plt.subplots(figsize=(25*cm,17*cm))
fig.canvas.draw()
ax.invert_xaxis()
for circle in circles:
    ax.plot(-circle['points'][0], circle['points'][1], marker = 'o', markersize = circle['r'], alpha = 0.7)
    ax.annotate(gitTitleNum(circle['magnitude']), (-circle['points'][0] -2, circle['points'][1]))
plt.xlabel('α Rektascenze [ h m s]')
plt.ylabel('δ Deklinace [° \' "]')

labels = [item.get_text() for item in ax.get_xticklabels()]
labels[1] = '3h 45m 00s'
labels[2] = '3h 45m 50s'
labels[3] = '3h 46m 40s'
labels[4] = '3h 47m 30s'
labels[5] = '3h 48m 20s'
labels[6] = '3h 49m 10s'
labels[7] = '3h 50m 00s'
labels[8] = '3h 50m 50s'
ax.set_xticklabels(labels)

labelsY = [item.get_text() for item in ax.get_yticklabels()]
labelsY[1] = "23° 03' 20\""
labelsY[2] = "23° 20' 00\""
labelsY[3] = "23° 36' 40\""
labelsY[4] = "23° 53' 20\""
labelsY[5] = "24° 10' 00\""
labelsY[6] = "24° 26' 40\""
labelsY[7] = "24° 43' 20\""
labelsY[8] = "25° 00' 00\""
ax.set_yticklabels(labelsY)

plt.show()