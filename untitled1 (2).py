# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xzcLT8Bykp36_PjrYvhs-Ds-Um6F5D7D
"""

# -*- coding: utf-8 -*-
"""Untitled13.ipynb
Automatically generated by Colab.
Original file is located at
    https://colab.research.google.com/drive/1O7SHUrR6SZ75GpErUsF6U_C9inC7gy7j
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sinus Funktsiyasi Grafiki')
plt.xlabel('X qiymatlari')
plt.ylabel('Sin(X)')
plt.show()

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='blue')
plt.title('Tasodifiy Nuqtalar Scatter Grafiki')
plt.xlabel('X qiymatlari')
plt.ylabel('Y qiymatlari')
plt.show()