import numpy as np





#rewrite the function so that it returns all timestamps for a given target name not just the first one
def get_timestamps(target_name, timestamps):
    timestamps= np.loadtxt('superflares_2.txt', dtype='str', usecols=11)
    target_names= np.loadtxt('superflares_2.txt', dtype='str', usecols=0)
    timestamps_list= []
    for i in range(len(target_names)):
        if target_name == target_names[i]:
            timestamps_list.append(timestamps[i])
    return timestamps_list



#write a function that only takes the target name and outputs the rotation period from the superflares text file
def get_rotation_period(target_name, input_file):
    #load the text file
    target_names= np.loadtxt(input_file, usecols=0, dtype=str)
    rotation_period= np.loadtxt(input_file, usecols=6, dtype=float)
    #find the index of the target name
    index= np.where(target_names==target_name)
    #return the rotation period
    return np.unique(rotation_period[index])