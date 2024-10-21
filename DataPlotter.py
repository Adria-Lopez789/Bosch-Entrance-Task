import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_data(data_path_accelerometer, data_path_gyroscope):
    accelerometer_data = pd.read_csv(data_path_accelerometer)
    accelerometer_data_dict = dict([("t",accelerometer_data['Time (s)']),("x",accelerometer_data['Acceleration x (m/s^2)']),("y",accelerometer_data['Acceleration x (m/s^2)']),("z",accelerometer_data['Acceleration x (m/s^2)'])])

    samples_per_second = int(1 / (accelerometer_data_dict['t'][1] - accelerometer_data_dict['t'][0]))
    for axis in accelerometer_data_dict.keys():
        if(axis != 't'):
            plt.plot(accelerometer_data_dict["t"][samples_per_second:-samples_per_second], accelerometer_data_dict[axis][samples_per_second:-samples_per_second], label='Acceleration over time', marker='o')
            plt.xlabel('Time (s)')
            plt.ylabel('Acceleration on ' + axis + ' axis (m/s^2)')
            plt.title('Acceleration on ' + axis + ' axis over time')
            plt.show()


            accelerometer_histogram, accelerometer_intervals = np.histogram(accelerometer_data_dict[axis], bins=100, density=True)
            accelerometer_interval_centers = 0.5 * (accelerometer_intervals[1:] + accelerometer_intervals[:-1])
            plt.bar(accelerometer_interval_centers, accelerometer_histogram, width=np.diff(accelerometer_intervals), align='center', edgecolor='black')
            plt.title('Probability density of ' + axis + ' axis acceleration')
            plt.subplots_adjust(bottom=0.2)
            plt.figtext(0.5,0.05,'Standard Deviation: ' + str(round(accelerometer_data_dict[axis].std(),3)) + '\n' + 'Mean: ' + str(round(accelerometer_data_dict[axis].mean(),3)), ha='center', fontsize=10)
            plt.grid(axis='y')
            plt.show()

    gyroscope_data = pd.read_csv(data_path_gyroscope)
    gyroscope_data_dict = dict([("t",gyroscope_data['Time (s)']),("x",gyroscope_data['Gyroscope x (rad/s)']),("y",gyroscope_data['Gyroscope x (rad/s)']),("z",gyroscope_data['Gyroscope x (rad/s)'])])

    samples_per_second = int(1 / (gyroscope_data_dict['t'][1] - gyroscope_data_dict['t'][0]))
    for axis in gyroscope_data_dict.keys():
        if(axis != 't'):
            plt.plot(gyroscope_data_dict["t"][samples_per_second:-samples_per_second], gyroscope_data_dict[axis][samples_per_second:-samples_per_second], label='Angular momentum over time', marker='o')
            plt.xlabel('Time (s)')
            plt.ylabel('Angular momentum on ' + axis + ' axis (m/s^2)')
            plt.title('Angular momentum on ' + axis + ' axis over time')
            plt.show()

            gyroscope_histogram, gyroscope_intervals = np.histogram(gyroscope_data_dict[axis], bins=100, density=True)
            gyroscope_interval_centers = 0.5 * (gyroscope_intervals[1:] + gyroscope_intervals[:-1])
            plt.bar(gyroscope_interval_centers, gyroscope_histogram, width=np.diff(gyroscope_intervals), align='center', edgecolor='black')
            plt.title('Probability density of ' + axis + ' axis angular momentum')
            plt.subplots_adjust(bottom=0.2)
            plt.figtext(0.5,0.05,'Standard Deviation: ' + str(round(gyroscope_data_dict[axis].std(),3)) + '\n' + 'Mean: ' + str(round(gyroscope_data_dict[axis].mean(),3)), ha='center', fontsize=10)
            plt.grid(axis='y')
            plt.show()

base_path = 'Data/Still_Quiet/'
plot_data(data_path_accelerometer=base_path + 'Accelerometer.csv', data_path_gyroscope=base_path + 'Gyroscope.csv')