import pandas as pd
import matplotlib.pyplot as plt
data = list(pd.read_csv('iris_data.csv')['PetalLengthCm'])
s = len([x for x in data if x < 1.2])/len(data)
m = len([x for x in data if 1.2 <= x < 1.5])/len(data)
b = len([x for x in data if x >= 1.5])/len(data)
plt.pie([s, m, b], labels=["x<1.2", "1.2<=x<1.5", "x>=1.5"])
plt.title("IRIS is COMING...")
plt.show()
