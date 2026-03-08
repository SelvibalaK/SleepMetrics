import pickle
import pandas as pd

with open(r"D:\User1\sleep_cycle\sleepcyclemodel.pkl", "rb") as f:
    model = pickle.load(f)

stress = int(input("Enter your stress level (1-10): "))

input_data = pd.DataFrame([[stress]], columns=["Stress Level"])
predicted_sleep = float(model.predict(input_data).item())

print(f"You should sleep around {predicted_sleep:.2f} hours tonight!")