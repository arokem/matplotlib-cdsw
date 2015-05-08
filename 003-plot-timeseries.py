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
ax.plot(hp.columns['timestamp'],  hp.columns['size'])
ax.set_xlabel('Time')
ax.set_ylabel('Size of the edit')

plt.show()


# Challenge: plot the relationship between edit size. Use 

## Hint 1: 

#delta_time1 = hp.columns['timestamp'][1] - hp.columns['timestamp'][0]

## Hint 2: 

# You can give `plt.plot` more arguments to control the shape/size/color 
# of the markers used. For example, try: 

# ax.plot([1,2,3], [2,4,8], '.')
# ax.plot([1,2,3], [2,4,8], 'r.')
