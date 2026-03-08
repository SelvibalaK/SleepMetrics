import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn. linear_model import LinearRegression

df = pd.read_csv(r"D:\User1\sleep_cycle\clean_data.csv")

X = df[["Stress Level"]]
Y = df[["Total Sleep Hours"]]

X_train , X_test , Y_train , Y_test = train_test_split ( X , Y , test_size=0.2 , random_state=42)

print ("Train Set Size :   ", len(X_train))
print ("Test Set Size :  ",len(X_test))

model = LinearRegression()
model.fit (X_train , Y_train)

print ("Model trained successfully")
print("Slope (m) :  " , model.coef_[0])
print("Intercept (b):  " , model.intercept_)

import pickle
with open (r"D:\User1\sleep_cycle\sleepcyclemodel.pkl", "wb") as f:
    pickle.dump ( model , f )

print( "Model saved as sleepcyclemodel.pkl !" )