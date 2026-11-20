import matplotlib.pyplot as plt
days=["sun","mon"]
temp=[12,23]
plt.barh(days,temp)
plt.xlabel("temp")
plt.ylabel("days")
plt.show()