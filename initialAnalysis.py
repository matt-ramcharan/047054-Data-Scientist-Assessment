#Import data opening tools
import pandas as pd
from tabulate import tabulate

#Open Data file
data = pd.read_csv("analysis_data",sep=',')

#Print all data in tabular form
print(tabulate(data,headers='keys', tablefmt='psql'))

#Initial Description of data
print(data.describe())




print()