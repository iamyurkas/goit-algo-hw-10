import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

# limits
a = 0
b = 2

# drawing
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integral f(x)=x² from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

# Monte Carlo estimate
N = 100000
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

points_under_curve = y_random < f(x_random)

rectangle_area = (b - a) * f(b)

monte_carlo_integral = rectangle_area * np.sum(points_under_curve) / N

result, error = spi.quad(f, a, b)

print(f"Monte Carlo estimated integral: {monte_carlo_integral}")
print(f"Analytical integral result: {result} (absolute error: {error})")
print(f"Monte Carlo absolute error: {abs(monte_carlo_integral - result)}")
