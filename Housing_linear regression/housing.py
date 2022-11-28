import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error


boston = load_boston()

df_x = pd.DataFrame(boston.data, columns=boston.feature_names)
df_y = pd.DataFrame(boston.target)

print(df_x.describe())

reg = linear_model.LinearRegression()

#splitting data
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.33, random_state=42)

#training data
reg.fit(x_train, y_train)

#the coefecients/weights for each feature/column of our model
print(reg.coef_)

#predictions on test data
y_pred = reg.predict(x_test)
print(y_pred)
#actual values
print(y_test)

#checking model performance
print(np.mean((y_pred - y_test)**2))
#checking model performance using Mean Squared Error (MSE) and sklearn.metrics
print(mean_squared_error(y_test, y_pred))
