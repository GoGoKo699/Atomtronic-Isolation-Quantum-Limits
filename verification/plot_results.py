"""Generate the scientific summary directly from the checked rate formulas."""
import os
from pathlib import Path
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir())/"atomtronic-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from check_rates import lower_bound, upper_bound, reduced_bound


def main():
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":11,
                         "axes.spines.top":False,"axes.spines.right":False,
                         "svg.fonttype":"none", "svg.hashsalt":"atomtronic-v1"})
    reverse=np.geomspace(1e-4,.24,350)
    low=np.array([lower_bound(r) for r in reverse])
    high=upper_bound(reverse)
    reduced=np.array([reduced_bound(1,r) for r in reverse])
    allowed=reverse/(1-np.sqrt(reverse))**2
    fig,axes=plt.subplots(1,2,figsize=(11.6,4.5),layout="constrained")
    ax=axes[0]
    ax.fill_between(reverse,low,high,color="#007c83",alpha=.16,
                    label=r"Ideal collection: bounded $Q_2$")
    ax.plot(reverse,high,color="#007c83",lw=2,label=r"Full-channel upper bound $U$")
    ax.plot(reverse,low,color="#007c83",lw=2,ls="-.",label=r"Mean-one probe lower bound $I_1$")
    ax.plot(reverse,reduced,color="#b56225",lw=2,ls="--",label=r"Reduced-channel upper envelope $F$")
    ax.set(xscale="log",yscale="log",xlabel=r"Reverse power $R$",
           ylabel="Bits or ebits per mode",xlim=(1e-4,.24),ylim=(5e-9,1))
    ax.set_title("A  |  Rate bounds at unity forward gain",loc="left",fontsize=12,fontweight="bold",pad=15)
    ax.legend(frameon=False,fontsize=8.5,loc="lower right")
    ax.grid(which="major",color="#d5dce0",lw=.6)
    ax=axes[1]
    ax.fill_between(reverse,1e-5,allowed,color="#4c67ad",alpha=.13)
    ax.plot(reverse,allowed,color="#4c67ad",lw=2)
    ax.set(xscale="log",yscale="log",xlabel=r"Reverse power $R$",
           ylabel=r"Uncollected fraction $1-\eta$",xlim=(1e-4,.24),ylim=(1e-5,1))
    ax.set_title("B  |  Collection-loss tolerance",loc="left",fontsize=12,fontweight="bold",pad=15)
    ax.text(.00022,.10,"Zero capacity\nAbove and on the curve",color="#35425b",fontsize=10)
    ax.text(.006,.00011,"Positive capacity\nStrictly below the curve",color="#35425b",fontsize=10)
    ax.plot([.01],[.01/.9**2],"o",color="#4c67ad",ms=5)
    ax.annotate("R = 0.01\nLoss < 1.235%",xy=(.01,.01/.9**2),xytext=(.026,.003),
                fontsize=9,arrowprops={"arrowstyle":"-","color":"#4c67ad"})
    ax.grid(which="major",color="#d5dce0",lw=.6)
    directory=Path(__file__).resolve().parents[1]/"figures"
    directory.mkdir(exist_ok=True)
    path=directory/"rates-and-collection.svg"
    fig.savefig(path,metadata={"Date":None,"Creator":"verification/plot_results.py"})
    # This PNG is a disposable local inspection copy, not a repository input.
    preview=Path(tempfile.gettempdir())/"atomtronic-rates-preview.png"
    fig.savefig(preview,dpi=150)
    print(path)
    print(preview)


if __name__ == "__main__":
    main()
