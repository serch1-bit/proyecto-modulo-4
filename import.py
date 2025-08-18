# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(0)

# numeros = np.random.rand(10)

# print(numeros)

# plt.plot(numeros)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

datos = np.random.normal(0, 1.0, 1000)

plt.hist(datos)
plt.show()