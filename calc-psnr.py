#! /usr/bin/env python3
""".

usage: calc-psnr.py [-hV]

options:
    -h, --help                  Show this screen.
    -V, --version               Show version.
"""
if __name__ == "__main__" and __doc__:
    from docopt import docopt
    from typing import Dict, Union

    Arg = Union[bool, str]
    args: Dict[str, Arg] = docopt(__doc__, version="v0.0.1")
    import numpy as np
    import os
    from glob import glob

    for fname in glob("tmp/logs/*/*/*.log"):
        print(
            os.path.join(*fname.split("/")[2:]).split("_")[0],
            " ".join(
                map(
                    str,
                    map(lambda x: round(x, 2), np.loadtxt(fname).mean(0)[1:]),
                )
            ),
        )
