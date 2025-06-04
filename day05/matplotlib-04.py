import random
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams["font.family"] = "Malgun Gothic"

x= [random.randint(0,100) for _ in range(30)]
y= [random.randint(0,100) for _ in range(30)]

plt.scatter(x,y,s=5,c="#ff0000")
plt.title('산점도')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()