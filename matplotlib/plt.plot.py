import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# figure1
plt.figure()
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# set axis limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set axis label
plt.xlabel('I am x')
plt.ylabel('I am y')

# figure2
plt.figure(num=3, figsize=(8, 5),)
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# figure3
plt.figure()
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
plt.legend(loc='upper right')

plt.show()
