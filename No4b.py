from pylab import *
from scipy.integrate import quad

def fourier(fun, n_max):
  a = []
  b = []
  for n in range(0, 1+n_max):
    res, err = quad(lambda x:fun(x)*cos((2*pi*n*x)/(2*pi)), -pi, pi)
    a.append(res/pi)
    res, err = quad(lambda x:fun(x)*sin((2*pi*n*x)/(2*pi)), -pi, pi)
    b.append(res/pi)
  def fn(x):
    sum = a[0] / 2
    for n in range(1, 1+n_max):
      sum += a[n]*cos((2*pi*n*x)/(2*pi)) + b[n]*sin((2*pi*n*x)/(2*pi))
    return sum
  return fn

def f(t):
    -pi/2 < t and t < pi/2
    return t * 2/(2*pi)


x_min = -5
x_max = 5
y_min = -2
y_max = 2
axis([x_min, x_max, y_min, y_max])

f_fn = fourier(f, 30)
xs = linspace(x_min, x_max, 256)
plot(xs, amap(f, xs), 'b:', lw=1)
plot(xs, amap(f_fn, xs), 'r-', lw=1)
show()
