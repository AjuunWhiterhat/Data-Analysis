import pandas as pd
import plotly.express as px
import csv 

data = pd.read_csv("data.csv")


mean = data.groupby(["student_id","level"],as_index=False)["attempt"].mean()

#*graph = px.scatter(data,x="data",y="backup")

graph = px.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")

graph.show()

