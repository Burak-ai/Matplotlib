import numpy as np
import matplotlib.pyplot as plt
#             x              y
"""plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.ylabel("Some Numbers")
plt.show()"""


"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
plt.axis((0, 6, 0, 20))
plt.show()"""



""""
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()"""



"""
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()"""



"""
names = ["group_A", "group_B", "group_C"]
values = [50, 40, 60]

plt.figure(figsize=(10, 4))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)# x, y
plt.subplot(133)
plt.plot(names, values)
plt.suptitle("Categorical Plotting")
plt.show()"""


"""
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), "bo", t2, f(t2), "k")

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), " r^")
plt.show()"""


"""
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, density=True, facecolor="g", alpha = 0.75)

plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()"""


 
x = np.linspace(0, 10, 100)
y = np.sin(x)
"""
plt.plot(x, y, color="red", linewidth=2, linestyle="--")
plt.scatter(x, y, color="blue", marker="o", s=5)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Wave")
plt.grid(True)
plt.show()"""

#      Subplots
fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(x, y, color="red", linestyle="-.")
axs[0, 1].scatter(x, y, color="magenta", marker="4")
axs[1, 0].bar(x, y, color="indigo")
axs[1, 1].hist(y, edgecolor="black", facecolor="blue")
axs[2, 0].boxplot(y)
axs[2, 1].pie(x, y)
# .contourf(x, y, z)
# .axes(projection='3d')
plt.show()

