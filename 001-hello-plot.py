""" 

hello_plot.py

A first plot with matplotlib

"""

import matplotlib.pyplot as plt 
figure = plt.figure()
axis = figure.add_subplot(111)
plt.plot([1,2,3], [1,2,3])
plt.show()
