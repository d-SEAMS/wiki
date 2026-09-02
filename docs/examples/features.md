# Ice features for kinetic models

`IceFeaturizer` walks a trajectory and returns one feature vector per
frame and one integer state per molecule per frame. The arrays are
plain NumPy.

`Trajectory` is an alias of `Frame`. Ring-adjacent completion is the
featurizer default.

```python
from pydseams import Trajectory
from pydseams.features import IceFeaturizer

traj = Trajectory("nucleation.lammpstrj", frame=1, atom_type=2, cutoff=3.5)
feat = IceFeaturizer(traj, ring_adjacent=True)
X, S = feat.transform()
print(feat.feature_names)
```

`X` follows `feat.feature_names`: `n_ice`, `n_max`, `n_clusters`,
`n_ic`, `n_ih`, `n_mixed`, cubicity, the `chill_plus` counts on the
cutoff graph, the largest `chill_plus` bulk cluster, and the six-ring
count. `X[:, 1]` is `n_max`. `S` lists `STATE_WATER`, `STATE_IC`,
`STATE_IH`, or `STATE_MIXED` per molecule.

Pass `ion_types` to append `n_ion_ice`, `n_ion_front`, `n_ion_liquid`
and the mean shell ice fraction.

## deeptime

```python
from pydseams.features import discretize_nmax, to_deeptime

dtrajs = discretize_nmax(X[:, 1], edges=[10, 50, 150, 400])
msm = to_deeptime(X, lagtime=5)
```

`to_deeptime` fits a time-lagged independent component analysis
on the full vector and returns the fitted model. Call
`model.transform(X)` for the projection.

## PyEMMA

```python
from pydseams.features import to_pyemma_featurizer

featurizer = to_pyemma_featurizer(feat, topology="nucleation.pdb")
```

The per-frame vector registers as a custom feature. PyEMMA is
unmaintained; deeptime succeeds it.

Book: [features how-to](https://d-seams.github.io/PydSEAMSlib/howto/features.html).
