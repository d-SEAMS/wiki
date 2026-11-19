# Other tools

Several codes name water structure. They do not compute the same object.

**CHILL+ in a viewer.** OVITO ships a Chill+ modifier. It paints the local label, the same family as `seams chill-plus`. It does not search primitive rings, prism blocks, or a hydrate face census. The label column this wiki exports is the one a viewer colours. See [Export labels](../howto/export.md).

**Bond-order libraries.** A Steinhardt implementation (freud, MDAnalysis, and the PLUMED `Q6` family) returns q6 or q6-bar for a neighbour shell. That is the number in [CHILL+ and q6](../tutorials/order-parameters.md). It does not decide hexagonal-cage membership.

**Ring statistics.** A ring code such as R.I.N.G.S. histograms closed walks. d-SEAMS keeps the primitive rings of [Franzblau](rings.md) and then builds prisms and cages from them. The histogram alone is `seams rings`. The cage score is the further step in [Prisms and cages](cages.md).

**A collective-variable engine.** PLUMED integrates along a trajectory and can print or commit on a scalar. `DSEAMS_CAGES` is an action in that engine. It reports the cage and CHILL+ counts. The counts have no derivatives. [On the fly with PLUMED](../tutorials/plumed.md) shows the input and the numbers it names.

**This engine.** One classification, called from Python, Julia, Rust, or `seams`, so the same frame gives the same census. The books are linked from the [home page](../index.md). [linkcell](linkcell.md) is the neighbour-list library the cutoff and mutual graphs are in the family of. It is a separate project.
