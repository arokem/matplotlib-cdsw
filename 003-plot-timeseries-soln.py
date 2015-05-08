""" 
003-plot-timeseries.py 

Plot data from the Harry Potter data-set as a time-series

""" 


import matplotlib.pyplot as plt 
import load_hp_data as hp

# We can play with styles:
#plt.style.use('bmh')
plt.style.use('ggplot') 
# To see available styles, type: 
#plt.style.available

fig, ax = plt.subplots(1)

delta = []
for x in range(len(hp.columns['timestamp']) - 1):
    t1 = hp.columns['timestamp'][x]
    t2 = hp.columns['timestamp'][x + 1]
    delta.append((t2-t1).total_seconds())

ax.plot(delta, hp.columns['size'][1:] , '.')
ax.loglog()
plt.show()
