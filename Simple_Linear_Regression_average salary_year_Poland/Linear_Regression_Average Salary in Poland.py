import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv('C:\\Users\\Monika Wolska\\Desktop\\Coding\\Python\\Simple_Linear_Regression_average salary_year_Poland\\Data.csv')

#checking if everything is imported correctly
print(data.head())

#checking how data looks on chart
plt.scatter(data['Year'], data['Average Salary'])
plt.show()

#there is aplitude, because in Poland there was hyperinflation in 90s so I don't want to take it to linear regression as data
#I check max value of salaty and focus on data since then 

print(max(data['Average Salary']))
print(data.Year[data['Average Salary'] == max(data['Average Salary'])])

# Poland had the highest salary before denomination in 1994 so I start my model in 1995
final_data = data.loc[data['Year'] > 1994]
print(final_data)

y = final_data['Average Salary'].values
x = final_data['Year'].values

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

#training model
model = linear_model.LinearRegression()
model.fit(x,y)

#we can see values a and b from our model y = ax +b
model.coef_
model.intercept_

#now we want to check prediction for the future, we create
data_prediction = pd.read_csv('C:\\Users\\Monika Wolska\\Desktop\\Coding\\Python\\Simple_Linear_Regression_average salary_year_Poland\\prediction.csv')
c = data_prediction['years'].values
c = c.reshape(-1, 1)
result = model.predict(c)

plt.xlabel('year')
plt.ylabel('average salary in Poland')
plt.scatter(c,result,color='red',marker='+')
plt.show()

data_prediction['prediction average salary'] = result
data_prediction.to_csv('C:\\Users\\Monika Wolska\\Desktop\\Coding\\Python\\Simple_Linear_Regression_average salary_year_Poland\\prediction.csv')