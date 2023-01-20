import numpy
import matplotlib.pyplot as mtp

salary = numpy.random.normal(4000, 500, 1000)
numpy.mean(salary)

# histogram->hist, 50 bar
mtp.hist(salary, 1000)
mtp.show()
