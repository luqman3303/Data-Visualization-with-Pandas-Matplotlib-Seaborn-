from statistics import stdev
from turtle import color
from numpy import std
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
st=pd.read_csv("Student.csv")
pd.set_option("display.max_rows" , None)
print(st)
plt.plot(st["gender"] , st["final_grade"] ,color="red")
plt.plot(st["gender"] , st["study_hours"] ,color="green")
plt.plot(st["gender"] , st["attendance"] ,color="purple")
plt.plot(st["gender"] , st["sleep_hours"] ,color="black")
st = st.dropna(subset=["gender", "parental_education"])
plt.plot(st["gender"] , st["parental_education"] ,color="darkred")
plt.plot(st["gender"] , st["internet"] ,color="yellow")
plt.plot(st["gender"] , st["extra_act"] ,color="pink")
plt.plot(st["gender"] , st["pt_job"] ,color="white")
plt.plot(st["gender"] , st["p_grade"] ,color="silver")
plt.plot(st["gender"] , st["F_score"] ,color="red")
fnf=st[["F_score" ,"p_grade" ,"attendance"]].aggregate(stdev)
plt.pie(fnf , labels=fnf.index , explode=(0.01,0.02,0.03) ,autopct="%1.1f%%")
print(fnf)
st.plot(kind="bar" , x="gender" , y="F_score")
sns.scatterplot(data=st ,x="gender" , y="F_score" )

plt.show()
