import matplotlib.pyplot as plt
import pandas as pd

data = {"Exports": [300, 500, 700]}
df = pd.DataFrame(data, columns=["Exports"], index=["Corn", "Wheat", "Soy"])
df.plot.pie(y="Exports", figsize=(5, 5), autopct="%1.1f%%", startangle=90)

plt.show()