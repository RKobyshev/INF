import pandas as pd
import matplotlib.pyplot as plt
d = pd.read_csv('BTC_data.csv')
x = list(d['time'])
y = list(d['close'])
plt.plot(x, y, 'b--')
plt.xticks(x)
plt.title("CRY ABOUT IT")
plt.show()