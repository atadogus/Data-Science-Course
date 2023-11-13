import matplotlib.pyplot as pyplot
import numpy


def f(x):
    """
    This is a method for a 2nd degree polynomial function which takes in an x value and then returns
    a corresponding result depending on the value intake
    :param x:
    :return x**2 + x + 1:
    """
    return x**2 + x + 1


def df(x):
    return 2*x + 1


def gradient_descent(initial_x, step_multiplier, precision):
    x_list = []
    slope_list = []
    previous_x = initial_x

    for n in range(500):
        gradient = df(previous_x)
        new_x = previous_x - step_multiplier * gradient

        x_list.append(previous_x)
        slope_list.append(gradient)

        step_size = abs(previous_x - new_x)

        if step_size < precision:
            break

        previous_x = new_x

    return x_list, slope_list


x_1 = numpy.linspace(start=-3, stop=3, num=102)
list_x, list_slope = gradient_descent(3, 0.05, precision=0.0001)

pyplot.figure(figsize=(12, 6))

pyplot.subplot(1, 2, 1)
pyplot.scatter(list_x, f(numpy.array(list_x)), color="red", alpha=0.5)
pyplot.plot(x_1, f(x_1))
pyplot.xlabel("x")
pyplot.ylabel("f(x) = x^2 + x + 1")
pyplot.xlim(-3.5, 3.5)
pyplot.ylim(0, 15)

pyplot.subplot(1, 2, 2)
pyplot.scatter(list_x, list_slope, color="red", alpha=0.5)
pyplot.plot(x_1, df(x_1))
pyplot.xlabel("x")
pyplot.ylabel("df(x) = 2x + 1")
pyplot.show()
