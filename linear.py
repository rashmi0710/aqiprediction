# IMPORTING DATASET
import pandas as pd
import pickle

df = pd.read_csv("C:\\Users\\dongr\\OneDrive\\Desktop\\air_quality_predi\\te.csv") 
x= df.iloc[:, 2:-2].values  
y= df.iloc[:, 9].values  

# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.3, random_state=0)  


from sklearn.linear_model import LinearRegression  
model= LinearRegression()  
model.fit(x_train, y_train)

#Predicting the Test set result;  
y_pred= model.predict(x_test)

pickle.dump(model, open('linear.pkl', 'wb'))