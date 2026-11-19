# Large systems

`--jobs` is the number of frame workers. One worker walks the frames in order. Two workers split the frames. The printed histogram of each frame is the same either way.

The file is `examples/inputs/nucleation_three.lammpstrj`, three frames of 4096 sites. The scientific reading of this file, the largest ice cluster, is [Nucleation](../tutorials/nucleation.md).

```bash
# example
set -euo pipefail
seams chill-plus examples/inputs/nucleation_three.lammpstrj --type 1 --frame 1 --last 3 --jobs 1 > /tmp/jobs1.txt
seams chill-plus examples/inputs/nucleation_three.lammpstrj --type 1 --frame 1 --last 3 --jobs 2 > /tmp/jobs2.txt
diff -u /tmp/jobs1.txt /tmp/jobs2.txt
```

`diff` exits non-zero when the files differ, so this block fails if the two worker counts disagree. The default follows the machine.

The same flag applies to the other `seams` subcommands that classify a frame range. It does not change cutoffs, graphs, or which molecules are ice.
