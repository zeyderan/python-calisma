import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3

figure = plt.figure()

axes = figure.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,'b')
axes.set_xlabel('X Axis')
axes.set_ylabel('Y Axis')
plt.show()