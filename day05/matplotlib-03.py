import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams["font.family"] = "Malgun Gothic"

labels = ["딸기","수박","메론","참외","체리"]
sizes = [10,20,30,40,30]

plt.pie(sizes, labels = labels, autopct="%1.1f%%",startangle=0)
plt.axis("equal")
plt.title('과일메뉴')
plt.show()