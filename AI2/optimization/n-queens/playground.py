import numpy as np
import matplotlib.pyplot as plt

ns = [1,2,3,4]
ws = [1,2,3,4]
fs = [4,3,2,1]
width = .25
# plt.figure(1)
plt.bar(ns, ws, width, linewidth=2, label="Swaps")
# plt.figure(2)
plt.bar([x + width for x in ns], fs, width, linewidth=2, label="Shuffles")

plt.xticks(ns)
plt.show()