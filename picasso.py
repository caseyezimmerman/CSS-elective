import matplotlib
import matplotlib.pyplot as plt
import time
import numpy as np
class Picasso:
    def __init__(self, file_name):
        self.file_name = file_name
        self.x_values = []
        self.y_values = []
        self.draw_best_fitting_line = False
        self.figure = plt.figure()
        self.plot = self.figure.add_subplot(111)
    def start(self, x_value):
        self.temp_x = x_value
        self.start_time = time.time()
    def end(self):
        if self.start_time is None:
            return
        self.end_time = time.time()
        time_difference = self.end_time - self.start_time
        self.add_point(self.temp_x, time_difference)
        self.temp_x = None
        self.start_time = None
        self.end_time = None
    def add_point(self, x, y):
        self.x_values.append(x)
        self.y_values.append(y)
    def export(self):
        x = np.asarray(self.x_values)
        y = np.asarray(self.y_values)
        self.plot.plot(self.x_values, self.y_values, '.', ms = 15, c='r')
        if self.draw_best_fitting_line:
            m, b = np.polyfit(x, y, 1)
            self.plot.plot(x, m*x + b, '-')
        self.figure.savefig('graph_' + self.file_name + '.png')
        time.sleep(.5)
        