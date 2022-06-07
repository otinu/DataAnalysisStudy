import matplotlib.pyplot as plt
import matplotlib.style

# パターン①===========================================
x = [1, 2, 3]
y = [2, 4, 9]

plt.plot(x, y)
plt.title("MATLAB-style")

plt.show()

# パターン②===========================================

fig, ax = plt.subplots()
ax.plot(x[0] + 1, y[0] - 1)
ax.set_title("OOP-style")
plt.show()