from vibes import vibes
# from pyibex import *
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def is_strict_interior_subset(X0, X):
  if X[0][0] > X0[0][0] and  X[1][0] > X0[1][0]: return True
  if X[0][1] < X0[0][1] and  X[1][1] < X0[1][1]: return True
  return False

def drawDiffBox_(X0, X, color, **kwargs):
  if is_strict_interior_subset(X0, X):
    vibes.drawBox(X0[0][0], X0[0][1], X0[1][0], X0[1][1], color)
    vibes.drawBox(X[0][0], X[0][1], X[1][0], X[1][1], "[w]")
  elif (X0[0][0] == X[0][0] and X0[0][1] == X[0][1]):
      if X0[1][0] != X[1][0]:
        vibes.drawBox(X0[0][0], X0[0][1], X0[1][0], X[1][0], color, **kwargs)
      if X0[1][1] != X[1][1]:
        vibes.drawBox(X0[0][0], X0[0][1], X[1][1], X0[1][1], color, **kwargs)
  elif (X0[1][0] == X[1][0] and X0[1][1] == X[1][1]):
      if X0[0][0] != X[0][0]:
        vibes.drawBox(X0[0][0], X[0][0], X0[1][0], X0[1][1], color, **kwargs)
      if X0[0][1] != X[0][1]:
        vibes.drawBox(X[0][1], X0[0][1], X0[1][0], X0[1][1], color, **kwargs)
  else:
    P = diffBox2poly(X0, X)
    vibes.drawPolygon(P, color, **kwargs)


def diffBox2poly(X0, X):
    # print(X0, X)

    LX = [Point(X[0][0], X[1][0]),
           Point(X[0][0], X[1][1]),
           Point(X[0][1], X[1][1]),
           Point(X[0][1], X[1][0])
           ]
    LX0 = [ Point(X0[0][0], X0[1][0]),
             Point(X0[0][0], X0[1][1]),
             Point(X0[0][1], X0[1][1]),
             Point(X0[0][1], X0[1][0])
    ]

    L = []
    # compute all face of the polygon
    for i in range(len(LX)):
        p1, p2 = LX[i], LX[(i+1)%4]
        p01, p02 = LX0[i], LX0[(i+1)%4]

        if (i%2)==0: # vertical line
            if (p01.x != p1.x):
                L.extend([[ p01, p02 ], [ p1, p2 ]])
            else:
                if p01.y != p1.y: L.append([ p01, p1 ])
                if p02.y != p2.y: L.append([ p2, p02  ])
        else: # horizontal line
            if (p01.y != p1.y):
                L.extend([[ p01, p02 ], [ p1, p2 ]])
            else:
              if p01.x != p1.x: L.append([ p01, p1 ])
              if p02.x != p2.x: L.append([ p2, p02  ])



    # print(LX, LX0)
    # for i,l in enumerate(L): print(i,l)

    P = [*L.pop(0) ]
    # print(P)
    while len(L) > 0:
      last_P = P[-1]
      # print(last_P)
      for i in range(len(L)):
        # print(L[i])
        p0, p1 = L[i]
        if last_P == p0:
          P.append(p1)
          L.pop(i)
          break
        if last_P == p1:
          P.append(p0)
          L.pop(i)
          break
    # print(P)
    return [ [p.x, p.y] for p in P]


#
#
# vibes.beginDrawing()
# vibes.newFigure("Test")
# vibes.setFigureSize(500,500)
# X0 = IntervalVector(2, [0, 4])
# X = IntervalVector([[0, 3], [0, 3]])
# vibes.drawBox(X0[0][0],X0[0][1], X0[1][0],X0[1][1])
# P = drawDiffBox(X0, X)
# vibes.drawPolygon(P, '[y]')
#
#
#
#
#
#
#
# vibes.endDrawing()
