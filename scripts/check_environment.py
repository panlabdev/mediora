import platform

import matplotlib
import numpy
import pandas
import pydantic
import scipy
import sklearn

print("Python:", platform.python_version())
print("Architecture:", platform.machine())

for module in [numpy, pandas, scipy, sklearn, matplotlib, pydantic]:
    print(f"{module.__name__}: {module.__version__}")

print("Research environment imports succeeded.")
print("No clinical model is implemented.")
