import pandas as pd
from tabulate import tabulate

data = pd.read_csv("analysis_data",sep=',')
print(data)
print(data.describe())


print()