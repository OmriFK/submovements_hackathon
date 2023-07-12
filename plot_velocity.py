#import numpy as np
#import matplotlib.pyplot as plt



def plotvelocity(velocity, time, plottype:int = 1):
    if plottype not in [1, 2]:
        raise ValueError('Unknown plot type') #Plot type 1 = time vs velocity_x/velocity_y. type 2 = time vs tangential velocity

    num_velocities = len(velocity)
    cols = int(np.ceil(np.sqrt(num_velocities)))
    rows = int(np.ceil(num_velocities / cols))

    fig, axs = plt.subplots(rows, cols)

    for k in range(num_velocities):
        if isinstance(axs, np.ndarray):
            ax = axs[k // cols, k % cols]
        else:
            ax = axs

        if plottype == 1:
            ax.plot(time[k], velocity[k])
            if k == num_velocities - 1:
                ax.legend(['v_x', 'v_y'])
        elif plottype == 2:
            tangvel = np.sqrt(np.sum(np.square(velocity[k]), axis=1))
            ax.plot(time[k], tangvel)

    plt.show()
