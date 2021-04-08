import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['1yr', '2yr', '3yr', '4yr','5yr']
Boys = [30, 35, 40, 44, 47]
Girls = [28.5, 33, 38, 40, 46]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Boys, width, label='Boys')
rects2 = ax.bar(x + width/2, Girls, width, label='Girls')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Height')
ax.set_title('Height by age group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

# SAVE the graph locally
plt.savefig("/home/student/mycode/graphing/boysvsgirls.png")
    # Save to "~/static"
plt.savefig("/home/student/static/boysvsgirls.png")
print("Graph generted")
