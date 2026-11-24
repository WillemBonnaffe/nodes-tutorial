import argparse
from pathlib import Path

import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--deposit", type=Path)
parser.add_argument("--truth", type=Path)
parser.add_argument("--output", type=Path)
args = parser.parse_args()

true = pd.read_csv(args.truth, sep=";").set_index("t").sort_index()
results = []

for file in sorted(args.deposit.glob("*.csv")):
    if file.resolve() in (args.truth.resolve(), args.output.resolve()):
        continue
    try:
        pred = pd.read_csv(file, sep=";").set_index("t").sort_index()
        if not pred.index.equals(true.index):
            raise ValueError("incorrect time steps")

        error = (pred[["R", "G", "B"]].to_numpy(dtype=float)
                 - true[["R", "G", "B"]].to_numpy(dtype=float))
        mse = np.mean(error ** 2)

        if not np.isfinite(mse):
            raise ValueError("non-finite predictions")

        results.append((file.name, mse))
    except (ValueError, KeyError, pd.errors.ParserError) as exc:
        print(f"Skipping {file.name}: {exc}")

pd.DataFrame(results, columns=["forecast", "mse"]).sort_values(
    "mse"
).to_csv(args.output, index=False)

print(f"Saved {len(results)} scores to {args.output}")

