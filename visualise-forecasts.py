
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--deposit", type=Path)
parser.add_argument("--truth", type=Path)
parser.add_argument("--output", type=Path)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)

true = pd.read_csv(args.truth, sep=";").set_index("t").sort_index()

for file in sorted(args.deposit.glob("*.csv")):
    if file.resolve() == args.truth.resolve():
        continue
    try:
        pred = pd.read_csv(file, sep=";").set_index("t").sort_index()
        if not pred.index.equals(true.index):
            raise ValueError("incorrect time steps")

        fig, axes = plt.subplots(3, 1, figsize=(8, 7), sharex=True)
        for ax, species in zip(axes, ["R", "G", "B"]):
            ax.plot(true.index, true[species], label="Ground truth", color="black")
            ax.plot(pred.index, pred[species], label="Forecast", linestyle="--")
            ax.set_ylabel(species)
            ax.legend()

        axes[-1].set_xlabel("Time")
        fig.suptitle(file.stem)
        fig.tight_layout()
        fig.savefig(args.output / f"{file.stem}.png", dpi=150)
        plt.close(fig)
        print(f"Saved {file.stem}.png")

    except (ValueError, KeyError, pd.errors.ParserError) as exc:
        print(f"Skipping {file.name}: {exc}")

