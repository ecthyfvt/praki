import matplotlib.pyplot as plt
import numpy as np

# Titration of H3PO4 with NaOH

# todo: add minor ticks and grid lines 

dV = 0.25 # ml

pH_values = [2.5,
             2.5,
             2.52,
             2.54,
             2.57,
             2.63,
             2.64,
             2.68,
             2.71,
             2.77,
             2.80,
             2.84,
             2.92,
             3.01,
             3.08,
             3.21,
             3.41,
             3.73,
             5.01,
             5.81,
             6.08,
             6.21,
             6.40,
             6.50,
             6.61,
             6.71,
             6.8,
             6.87,
             6.95,
             7.03,
             7.14,
             7.24,
             7.34,
             7.46,
             7.60,
             7.81,
             8.08,
             8.65,
             9.68,
             10.21,
             10.49,
             10.66,
             10.77,
             10.88,
             10.95,
             11.01,
             11.05,
             11.12,
             11.17,
             11.20,
             11.23,
             11.27,
             11.31,
             11.34,
             11.36,
             11.38,
             11.42,
             11.45,
             11.46,
             11.48,
             11.49,
             11.52,
             11.53,
             11.56,
             11.58,
             11.59,
             11.60,
             11.63,
             11.63,
             11.65,
             11.66,
             11.67,
             11.69,
             11.7,
             11.73,
             11.74,
             11.74,
             11.75,
             11.76,
             11.77,
             11.78,
             11.79,
             11.79,
             11.81]
             

# x-axis values

X = [dV*i for i in range(len(pH_values))]


plt.plot(X, pH_values, label='pH')

# Adding labels and title
plt.title('')
plt.xlabel('Объем 0.1М NaOH, мл', fontsize = 24)
plt.ylabel('pH раствора', fontsize = 24)

plt.xticks(np.arange(0, 22, 1), fontsize = 17)
plt.yticks(np.arange(2, 12.5, 1), fontsize = 17)



plt.show()