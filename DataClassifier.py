import torch
import pandas as pd
import torch.nn.functional as F


def dataToTensor(combined_array):
    combined_array = [gyroscope_data_dict['x'], gyroscope_data_dict['y'], gyroscope_data_dict['z'],
                      accelerometer_data_dict['x'], accelerometer_data_dict['y'], accelerometer_data_dict['z']]

    # Neural networks deal better with numbers between 0 and 1, so we first normalise the arrays
    for i, array in enumerate(combined_array):
        combined_array[i] = array - (array.mean()) / array.std()

    input_to_classify = torch.tensor(combined_array, dtype=torch.float32)


base_path = 'Data/Still_Quiet/'
data_path_accelerometer=base_path + 'Accelerometer.csv'
data_path_gyroscope=base_path + 'Gyroscope.csv'

accelerometer_data = pd.read_csv(data_path_accelerometer)
accelerometer_data_dict = dict([("t",accelerometer_data['Time (s)']),("x",accelerometer_data['Acceleration x (m/s^2)']),("y",accelerometer_data['Acceleration x (m/s^2)']),("z",accelerometer_data['Acceleration x (m/s^2)'])])

gyroscope_data = pd.read_csv(data_path_gyroscope)
gyroscope_data_dict = dict([("t",gyroscope_data['Time (s)']),("x",gyroscope_data['Gyroscope x (rad/s)']),("y",gyroscope_data['Gyroscope x (rad/s)']),("z",gyroscope_data['Gyroscope x (rad/s)'])])

