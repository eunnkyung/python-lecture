import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams["font.family"] = "Malgun Gothic"

df = pd.read_excel("day05/data.xlsx")
labels = df["항목"]
values = df["값"]
colors = ["#336cc2","#6fbd9f","#d483d4","#a8196d","#DDE666"]

explodes = (0,0,0.1,0,0)

# plt.bar(labels, values, color = "#336cc2")
plt.pie(values, labels=labels, autopct = "%1.1f%%", startangle=90, colors =colors, explode=explodes)
plt.title('파이그래프')
# plt.xlabel('과일종류')
# plt.ylabel('수량')
# plt.grid(True)
plt.show()