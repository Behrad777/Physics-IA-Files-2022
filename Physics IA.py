import matplotlib.pyplot as plt

# x axis values
x = []
# corresponding y axis values
y = []

m = 0.1
g = 9.81
rho = 1.225

AC = 0.8*0.1

h = 0

v = 0

t = 0

dt = 0.0001

x.append(0)
y.append(0)


while h > -3.0:
    F = -m*g+0.5*rho*AC*v**2
    a = F/m
    h = h+v*dt
    v = v+a*dt
    t = t+dt

    x.append(t)
    y.append(-v)

plt.plot(x, y)

plt.xlabel('Time (seconds)')
plt.ylabel('velocity (m/s)')

plt.title('Time and velocity during drop')

plt.show()
