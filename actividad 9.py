import pandas as pd
import numpy as np

df=pd.read_csv("StudentsPerformance")

df.sort_values("math score")

df.sort_values(["math score"], ascending=False)
