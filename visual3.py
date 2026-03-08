import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np

df = pd.read_csv(r"D:\User1\sleep_cycle\clean_data.csv")

X = df["Stress Level"]
y = df["Total Sleep Hours"]

with open(r"D:\User1\sleep_cycle\sleepcyclemodel.pkl", "rb") as f:
    model = pickle.load(f)

avg_sleep = df.groupby("Stress Level")["Total Sleep Hours"].mean()

x_line = np.linspace(1, 10, 100)
y_line = model.predict(x_line.reshape(-1, 1))

plt.scatter(avg_sleep.index, avg_sleep.values, color="blue", s=100, label="Avg Sleep")
plt.plot(x_line, y_line, color="red", linewidth=2, label="Regression Line")
plt.xlabel("Stress Level")
plt.ylabel("Sleep Hours")
plt.title("Stress vs Sleep with Regression Line")
plt.legend()
plt.show()

plt.ylim(6.8, 7.1)
plt.grid(True, alpha=0.3)