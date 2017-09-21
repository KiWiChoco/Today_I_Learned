import matplotlib.pyplot as plt
import numpy as np
from sklearn import  datasets,linear_model

diabetes = datasets.load_diabetes()

# print(datasets)

diabetes_x = diabetes.data[:, np.newaxis, 2]
# print(diabetes_x)

diabetes_x_train = diabetes_x[:-20]
diabetes_x_test = diabetes_x[-20:]

diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression(copy_X=0)

regr.fit(diabetes_x_train,diabetes_y_train)

print("Coefficients : ", regr.coef_)
print("Intercept : ", regr.intercept_)
print("Mean squared error : %.2f" %np.mean((regr.predict(diabetes_x_test) - diabetes_y_test) ** 2))
print("Variance score : %.2f " %regr.score(diabetes_x_test,diabetes_y_test))

plt.scatter(diabetes_x_test,diabetes_y_test,color = 'black')
plt.plot(diabetes_x_test,regr.predict(diabetes_x_test),color = 'blue')

# plt.xticks()
# plt.yticks()  <-이 두개는 x축y축의 구분선(범위선)을 없애준다.

plt.show()