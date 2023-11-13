import pandas
from pandas import DataFrame
from matplotlib import pyplot as pyplot
from sklearn.linear_model import LinearRegression

# data = pandas.read_csv("cost_revenue_clean.csv")
# dataFrame[["Production Budget ($)", "Worldwide Gross ($", "Domestic Gross ($)"]] = (
#    dataFrame[["Production Budget ($)", "Worldwide Gross ($)", "Domestic Gross ($)"]].apply(pandas.to_numeric))
# print(data.describe())
# x = DataFrame(data, columns=["production_budget_usd"])
# y = DataFrame(data, columns=["worldwide_gross_usd"])
data = pandas.read_csv("cost_revenue_dirty.csv")
x = DataFrame(data, columns=["Production Budget ($)"])
y = DataFrame(data, columns=["Worldwide Gross ($)"])

regression = LinearRegression()
regression.fit(x, y)

pyplot.figure(figsize=(10, 6))
pyplot.scatter(x, y, alpha=0.5)  # alpha in this function adjusts the transparency value of the data point on the chart
pyplot.plot(x, regression.predict(x), color="red", linewidth=2)
pyplot.title("Movie Cost vs Global Revenue")
pyplot.xlabel("Production Budget ($)")
pyplot.ylabel("Worldwide Gross ($)")
pyplot.xlim(0, 500000000)
pyplot.ylim(0, 3000000000)
pyplot.show()

print(f"slope: {regression.coef_}, starting coefficient: {regression.intercept_}, goodness of fit: {regression.score(x, y)}")
# https://en.wikipedia.org/wiki/Goodness_of_fit
