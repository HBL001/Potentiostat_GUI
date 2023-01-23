# Copyright (c) 2023 Kyle Lopin (Naresuan University) <kylel@nu.ac.th>

"""

"""

__author__ = "Kyle Vitautas Lopin"

# installed libraries
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data1 = [2198, 1998, 2193, 1993, 2188, 1988, 2183, 1983, 2178, 1978, 2173, 1973,
         2168, 1968, 2163, 1963, 2158, 1958, 2153, 1953, 2148, 1948, 2143, 1943,
         2138, 1938, 2133, 1933, 2128, 1928, 2123, 1923, 2118, 1918, 2113, 1913,
         2108, 1908, 2103, 1903, 2098, 1898, 2093, 2093, 1893, 2098, 1898, 2103,
         1903, 2108, 1908, 2113, 1913, 2118, 1918, 2123, 1923, 2128, 1928, 2133,
         1933, 2138, 1938, 2143, 1943, 2148, 1948, 2153, 1953, 2158, 1958, 2163,
         1963, 2168, 1968, 2173, 1973, 2178, 1978, 2183, 1983, 2188, 1988, 2193,
         1993, 2198, 1998, 2098]
DAC_GROUND = 2048
data = data1
data_line = []
for pt in data:
    data_line.extend([pt-2048, pt-2048])

plt.plot(data_line)
plt.show()
