"""
004-plot-histogram.py 

Plot a histogram of edit sizes 

"""

import matplotlib.pyplot as plt 
import load_hp_data as hp

plt.style.use('ggplot')

fig, ax = plt.subplots(1)

## Challenge : Find the 5 users with the largest number of edits and plot a 
# bar chart with the maximal edit size for each one of them

user_dict = {}

for row in hp.rows:
    user = row['user']
    if user in user_dict.keys():
        user_dict[user].append(row['size']) 
    else:
        user_dict[user]= [row['size']]

mega_users = []
for user in user_dict:
    if len(user_dict[user]) > 1000:
        mega_users.append(max(user_dict[user]))

ax.bar(range(len(mega_users)), mega_users)

plt.show()
