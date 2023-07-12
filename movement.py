import os
import re
import numpy as np
from scipy.signal import filtfilt, butter

class movement:

    def __init__(self) -> None:

        pass

    def loaddata(dirname):
        files = os.listdir(dirname)
        csv_files = [f for f in files if f.endswith('.csv')]
        
        if not csv_files:
            raise ValueError('Must specify a directory to load the csv files from')
        
        blocks = []
        trials = []
        filenames = []
        for filename in csv_files:
            filenames.append(filename)
            match = re.search(r'tb_.*block(\d*)_trial(\d*).csv', filename)
            block = int(match.group(1))
            trial = int(match.group(2))
            blocks.append(block)
            trials.append(trial)
        
        max_block = max(blocks)
        max_trial = max(trials)
        
        position = {}
        velocity = {}
        time = {}
        
        for b in range(1, max_block + 1):
            for t in range(1, max_trial + 1):
                trial_index = [i for i, (block, trial) in enumerate(zip(blocks, trials)) if block == b and trial == t]
                if not trial_index:
                    continue
                trial_num = (b - 1) * max_trial + t
                data = np.loadtxt(os.path.join(dirname, csv_files[trial_index[0]]), delimiter=',')
                pressure = data[:, 3]
                position[trial_num] = data[pressure > 0, :2] / 1000
                time[trial_num] = data[pressure > 0, 4] / 1000  # seconds
                time[trial_num] = time[trial_num] - time[trial_num][0]
                dt = np.median(np.diff(time[trial_num]))
                b, a = butter(2, 5 / ((1 / dt) / 2))
                position_filtered = filtfilt(b, a, position[trial_num], axis=0)
                velocity[trial_num] = np.vstack([[0, 0], np.diff(position_filtered, axis=0) / dt])
        
        return position_filtered, velocity, time
