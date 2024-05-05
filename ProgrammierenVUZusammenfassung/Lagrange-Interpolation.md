[source](https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html)
![[LagrangeInterpolatingPoly_900.svg]]
The Lagrange interpolating polynomial is the unique polynomial of lowest degree that interpolates a given set of data.

Given a data set of coordinate pairs $(x_j,y_j)$ with $0\leq j \leq k$, the $x_j$ are called nodes and the $y_j$ are called values. The Lagrange polynomial $L(x)$ has degree $\leq j$ and assumes each value at the corresponding node, $L(x_j) = y_j$.

```python
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import lagrange

x = [3, 4, 5, 6, 7]
y = [0.5, 1.2, -1.1, -1.3, 0]

poly = lagrange(x,y)
print(poly)

x_new = np.arange(2,8,0.1)
plt.scatter(x, y, label="Datenpunkte", color="red")
plt.plot(x_new, poly(x_new), label="Polynom")
plt.title("Lagrange Polynomial Interpolation")
plt.legend(loc="lower right")
plt.show()
		   
```
