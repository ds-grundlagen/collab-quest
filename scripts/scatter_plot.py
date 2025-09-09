import random 
import matplotlib.pyplot as plt

x,y=[],[]
for i in range(100):
    x.append(random.randint(0, 10))
    y.append(random.randint(0, 10))


plt.scatter(x,y,c='magenta')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.savefig('scatter_plot.png')