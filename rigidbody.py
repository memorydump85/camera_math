import numpy as np
from numpy import cos, sin



def xyt_to_matrix(x, y, t):
    rotz = lambda t: \
        np.array([[ cos(t), -sin(t),  0. ],
                  [ sin(t),  cos(t),  0. ],
                  [     0.,      0.,  1. ]])

    translate = lambda x, y: \
        np.array([[ 1.,  0.,  x  ],
                  [ 0.,  1.,  y  ],
                  [ 0.,  0.,  1. ]])

    return reduce(np.dot,
        [ translate(x, y), rotz(t) ])


def matrix_to_xyt(M):
    tx = M[0,2]
    ty = M[1,2]
    rz = np.arctan2(M[1,0], M[0,0])
    return tx, ty, rz


def xyzrph_to_matrix(x, y, z, r, p, h):

    rotx = lambda t: \
        np.array([[  1.,      0.,      0.,  0. ],
                  [  0.,  cos(t), -sin(t),  0. ],
                  [  0.,  sin(t),  cos(t),  0. ],
                  [  0.,      0.,      0.,  1. ]])

    roty = lambda t: \
        np.array([[  cos(t),  0.,  sin(t),  0. ],
                  [    0.,    1.,    0.,    0. ],
                  [ -sin(t),  0.,  cos(t),  0. ],
                  [    0.,    0.,    0.,    1. ]])

    rotz = lambda t: \
        np.array([[ cos(t), -sin(t),  0.,   0. ],
                  [ sin(t),  cos(t),  0.,   0. ],
                  [     0.,      0.,  1.,   0. ],
                  [     0.,      0.,  0.,   1. ]])

    translate = lambda x, y, z: \
        np.array([[ 1.,  0.,  0.,  x  ],
                  [ 0.,  1.,  0.,  y  ],
                  [ 0.,  0.,  1.,  z  ],
                  [ 0.,  0.,  0.,  1. ]])

    return reduce(np.dot,
        [ translate(x, y, z), rotz(h), roty(p), rotx(r) ])


def matrix_to_xyzrph(M):
    tx = M[0,3]
    ty = M[1,3]
    tz = M[2,3]
    rx = np.arctan2(M[2,1], M[2,2])
    ry = np.arctan2(-M[2,0], np.sqrt(M[0,0]*M[0,0] + M[1,0]*M[1,0]))
    rz = np.arctan2(M[1,0], M[0,0])
    return tx, ty, tz, rx, ry, rz
