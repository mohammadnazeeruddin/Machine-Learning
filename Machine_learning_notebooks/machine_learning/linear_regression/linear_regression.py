import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

house  = pd.read_csv('home_data.csv')
x = house[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','condition','sqft_above','sqft_basement','sqft_lot15','sqft_living15','zipcode']]
y = house['price']
x.shape
y.shape

X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.3,random_state = 7 )
model = LinearRegression()
model.fit(X_train,y_train)
prediction = model.predict(X_test)

print("prediction data:",prediction)
house1 = house[house['id'] == 6414100192]
print("actual_price",house1['price']) 
print("prediction price",prediction[1])
plt.scatter(y_test,prediction)

model.coef_
data_frame = pd.DataFrame(model.coef_,x.columns, columns=['coeff values'])
mean_sq_err = metrics.mean_squared_error(y_test,prediction)
RMSE=np.sqrt(mean_sq_err)
print("RMSError",RMSE)


# house = house.head()
# house.tail()
# house = house.info()
# house = house.describe()
# house  = house.columns


# matplotli
# plt.figure(figsize=(10,6))
# plt.scatter(house.sqft_living,house.price)
# plt.xlabel("sqft of house")
# plt.ylabel("price of house")
# plt.show()

#seaborn
# sns.lmplot('sqft_living','price' ,data = house)
# sns.heatmap(house.corr())

# print(x_test.shape,y_test.shape)
# print(x_train.shape,y_train.shape)