import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams["font.family"] = "Malgun Gothic"

x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.title('라인그래프')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.show()
