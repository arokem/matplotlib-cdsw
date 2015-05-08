"""
004-plot-histogram.py 

Plot a histogram of edit sizes 

"""

import matplotlib.pyplot as plt 
import load_hp_data as hp

plt.style.use('ggplot')

fig, ax = plt.subplots(1)
ax.hist(hp.columns['size'], bins=1000)
ax.set_xlabel('Size of the edit')
ax.set_ylabel('')
ax.set_title('Edit size distribution')

# Maybe don't really need that axis to be so long:
# ax.set_xlim([0, 200000])

plt.show()
