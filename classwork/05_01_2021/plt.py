import matplotlib.pyplot as plt
import pandas as pd

x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]

plt.plot(x, y)
plt.show()

plt.bar(x, y)
plt.show()

plt.hist(x)
plt.show()

df = pd.DataFrame({'x': x, 'y': y})
df.plot('x', 'y', kind="scatter")
plt.show()
