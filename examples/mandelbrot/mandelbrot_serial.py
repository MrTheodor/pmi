import numpy as np
import time

def mandelbrot_func(x, y, maxit):
    c = x + y*1j
    z = 0 + 0j
    it = 0
    while abs(z) < 2 and it < maxit:
        z = z**2 + c
        it += 1
    return it

def mandelbrot(xxx_todo_changeme, xxx_todo_changeme1, xxx_todo_changeme2, maxit):
    (x1, y1) = xxx_todo_changeme
    (x2, y2) = xxx_todo_changeme1
    (w, h) = xxx_todo_changeme2
    before = time.time()

    dx = (x2 - x1) / w
    dy = (y2 - y1) / h

    # compute lines
    C = np.empty([h, w], dtype='i')
    for k in np.arange(h):
        y = y1 + k * dy
        for j in np.arange(w):
            x = x1 + j * dx
            C[k, j] = mandelbrot_func(x, y, maxit)

    after = time.time()
    print(('%f seconds for computation.'
          % (after-before)))

    return C
