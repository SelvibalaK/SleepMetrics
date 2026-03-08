import pandas as pd

df = pd.read_csv(r"D:\User1\sleep_cycle\sleep_cycle_productivity.csv")

df = df [["Stress Level", "Total Sleep Hours"]]

print (df.isnull().sum())

print (df.shape)

print (df.duplicated().sum())
df = df.drop_duplicates()

print (df.shape)

df.to_csv(r"D:\User1\sleep_cycle\clean_data.csv", index=False)
print ("cleaned dataset shape :  ",(df.shape))