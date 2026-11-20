import matplotlib.pyplot as plt
days=["mon","tues","wed"]
temp=[1000,2,9990]
plt.plot(days,temp,linestyle="-")
plt.title("temp")
plt.xlabel("days")
plt.ylabel("temp")
plt.show()