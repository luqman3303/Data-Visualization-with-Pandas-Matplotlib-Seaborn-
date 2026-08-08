from cProfile import label
from turtle import color
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 
ad=pd.read_csv("book.csv")
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# plt.plot(ad ["Year"] , ad ["Laptops"], color="red" , label="Laptops")
# plt.plot(ad ["Year"] , ad ["Mobiles"], color="pink" , label="Mobiles")
# plt.plot(ad ["Year"] , ad ["Car"] , color="yellow" , label="Car")
# # print(ad)
# plt.title("Sale Data")
# plt.ylabel("MCC")
# plt.xlabel("Years")
# plt.legend()
# plt.show()
# total=ad[["Laptops" ,"Mobiles" ,"Car"]].sum()
# print(total)
# plt.pie(total, labels=total.index , explode=(0.02,0.03,0.04), autopct="%1.1f%%")
# ad.plot(kind="bar" , x="Year")
sns.scatterplot(data=ad , x="Year" , y="Car")
plt.show()