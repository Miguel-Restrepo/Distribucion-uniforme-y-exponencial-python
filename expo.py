import numpy as np
import matplotlib.pyplot as plt
distribucion_exponencial = np.random.exponential(3.45, 10000)
distribucion_uniforme = np.random.uniform(0.0, 1.0, 10000)
count, bins, ignored = plt.hist(distribucion_uniforme, 14, density=True)
plt.show()
count, bins, ignored = plt.hist(distribucion_exponencial, 14, density=True)
plt.show()