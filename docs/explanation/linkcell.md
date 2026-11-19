# linkcell

[linkcell](https://linkcell.dseams.info/) is a periodic neighbour-search library. It is not a language front of d-SEAMS. d-SEAMS builds its own cutoff lists and mutual k-nearest lists. Those lists are the graphs the [rings](rings.md) and the [cages](cages.md) are searched on. linkcell is the same kind of search, as its own package, with its own book.

The smallest periodic check is two points in a cell of length 10. One sits at 0.2, the other at 9.4. The nearest image of each is the other, and the squared distance is 0.64.

```python
# example
import numpy as np
import linkcell

points = np.array([[0.2, 0.0, 0.0], [9.4, 0.0, 0.0]])
box = np.array([10.0, 10.0, 10.0])
index, distance = linkcell.knearest(points, box, k=1)
index = np.from_dlpack(index)
distance = np.from_dlpack(distance)
assert index.tolist() == [[1], [0]]
assert abs(float(distance[0, 0]) - 0.64) < 1e-9
print(index.tolist(), float(distance[0, 0]))
```

`knearest` returns DLPack buffers. The neighbour of point 0 is point 1, and the neighbour of point 1 is point 0. The squared distance is the periodic gap, 0.8 squared, not the naive gap of 9.2.

The book covers the rest of the interface. The cutoff that d-SEAMS then applies to a neighbour shell is [Choose a cutoff](../howto/cutoff.md).
