import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams["font.family"] = "Malgun Gothic"

labels = ["A","B","C","D","F"]
values = [10,20,30,40,50]

plt.bar(labels, values)
plt.title('막대그래프')
plt.show()