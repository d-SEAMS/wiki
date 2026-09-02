# Kinetic features

`pydseams.features.IceFeaturizer` walks a trajectory and returns one
feature vector per frame plus one integer state per molecule. The
arrays are plain NumPy.

## IceFeaturizer

```python
from pydseams import Trajectory
from pydseams.features import IceFeaturizer

traj = Trajectory("nucleation.lammpstrj", frame=1, atom_type=2, cutoff=3.5)
feat = IceFeaturizer(traj, ring_adjacent=True)
X, S = feat.transform()
print(feat.feature_names)
```

`Trajectory` is an alias of `Frame`. `IceFeaturizer` calls
`Frame.seeded_affiliation` on each frame. Ring-adjacent completion is
the featurizer default. `Frame.cages` and `Frame.seeded_affiliation`
leave that flag off unless you pass it.

`X` lists cage counts (`n_ice`, `n_ic`, `n_ih`, `n_mixed`), the
largest connected cage cluster `n_max`, the cluster count, the
cubicity, the `chill_plus` counts on the cutoff graph, the largest
`chill_plus` bulk cluster, and the six-ring count. `S` lists
`STATE_WATER`, `STATE_IC`, `STATE_IH`, or `STATE_MIXED` per molecule.

The same feature vector feeds a kinetic model.

## deeptime and PyEMMA

```python
from pydseams.features import discretize_nmax, to_deeptime

dtrajs = discretize_nmax(X[:, 1], edges=[10, 50, 150, 400])
msm = to_deeptime(X, lagtime=5)
```

`to_deeptime` fits a time-lagged independent component analysis on
the full vector and returns the fitted model.

```python
from pydseams.features import to_pyemma_featurizer

featurizer = to_pyemma_featurizer(feat, topology="nucleation.pdb")
```

The per-frame vector registers as a custom feature. PyEMMA is
unmaintained; deeptime succeeds it.

## Ions on the feature vector

```python
from pydseams import Trajectory
from pydseams.features import ION_ICE, IceFeaturizer, ion_environment

traj = Trajectory("brine.lammpstrj", frame=1, atom_type=1, all_atoms=True)
feat = IceFeaturizer(traj, ion_types=(3, 4))
x, states = feat.frame_features()
ions, shell, fraction, ion_states = ion_environment(traj, states, (3, 4))
trapped = ions[ion_states == ION_ICE]
```

`ion_types` adds `n_ion_ice`, `n_ion_front`, `n_ion_liquid`, and the
mean shell ice fraction to the feature vector.

Howto: [features](https://d-seams.github.io/PydSEAMSlib/howto/features.html).
