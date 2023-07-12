import matplotlib.pyplot as plt
import math
import numpy as np



position = np.array([1, 2, 3, 4, 5])
time = np.array([1, 2, 3, 4, 5])


def plotposition(position,time,plottype = 1):

    if plottype is None:
        plottype = 1

    num_positions = len(position)
    cols = math.ceil(math.sqrt(num_positions))  # coloums are root of the number in num_position. ceil rounds it up
    rows = math.ceil(num_positions/cols)        # rows are num_position/cols. then ceil round the numbers up.

    fig = plt.figure()


    for i in range(num_positions):

        ax = fig.add_subplot(rows,cols, i+1) ## creating number of subplots in rowxXcols

        if plottype == 1:
            pos_data = position[i]
            ax.plot(pos_data[:, 0], pos_data[:, 1])
            ax.axis('equal')
        elif plottype == 2:
            time_data = time[i]
            pos_data = position[i]
            ax.plot(time_data, pos_data)
        if i == num_positions - 1:
            ax.legend(['x', 'y'])
        else:
            raise ValueError('Unknown plot type')

plt.show()





        



    # print ('num_positions',num_positions)
    # print ('cols',cols)
    # print ('rows',rows)

plotposition(position)
