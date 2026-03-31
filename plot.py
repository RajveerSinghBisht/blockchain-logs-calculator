import pandas as pd
import matplotlib.pyplot as plt

# ── Load Data ──────────────────────────────────────────────────────────────────

df = pd.read_csv("results.csv")

# ── Cost Calculation ───────────────────────────────────────────────────────────
# Update ETH_PRICE_USD to actual rate on the day you ran the experiment

GAS_PRICE_GWEI = 20
ETH_PRICE_USD  = 1987.68  # UPDATE to actual ETH/USD rate on experiment date(as on 28-march)

df["cost_usd"] = df["total_gas"] * GAS_PRICE_GWEI * 1e-9 * ETH_PRICE_USD

# ── Average Duplicate Runs ─────────────────────────────────────────────────────

df = df.groupby("workload", as_index=False).mean()

# ── Shared Settings ────────────────────────────────────────────────────────────

X_TICKS  = [100, 1000, 10000, 50000]
X_LABELS = ["100", "1k", "10k", "50k"]

COLOR_TRADITIONAL = "#1f77b4"
COLOR_BLOCKCHAIN  = "#ff7f0e"

GRID_STYLE   = {"linestyle": "--", "alpha": 0.6}
MARKER_SIZE  = 6
ANNOT_OFFSET = 10   # vertical offset in points for annotations


# ── Annotation Helper ──────────────────────────────────────────────────────────

def annotate_points(x_data, y_data, fmt="{:.5f}", offset=ANNOT_OFFSET, color="black"):
    """
    Annotate each data point on the current axes with its y value.

    Args:
        x_data : iterable of x values
        y_data : iterable of y values
        fmt    : format string for the y value label
        offset : vertical offset in points above the marker
        color  : text color for annotation
    """
    ax = plt.gca()
    for x, y in zip(x_data, y_data):
        ax.annotate(
            fmt.format(y),
            xy=(x, y),
            xytext=(0, offset),
            textcoords="offset points",
            fontsize=7.5,
            ha='center',
            color=color
        )


# ── 1. Write Latency ───────────────────────────────────────────────────────────

plt.figure()

plt.plot(df["workload"], df["t_latency"],
         marker='o', markersize=MARKER_SIZE,
         color=COLOR_TRADITIONAL, label="Traditional")
annotate_points(df["workload"], df["t_latency"],
                fmt="{:.5f}", color=COLOR_TRADITIONAL)

plt.plot(df["workload"], df["b_latency"],
         marker='o', markersize=MARKER_SIZE,
         color=COLOR_BLOCKCHAIN, label="Blockchain")
annotate_points(df["workload"], df["b_latency"],
                fmt="{:.5f}", color=COLOR_BLOCKCHAIN)

plt.xscale("log")
plt.yscale("log")
plt.xticks(X_TICKS, X_LABELS)

plt.xlabel("Workload (log entries)")
plt.ylabel("Average Write Latency (seconds)")
plt.title("Write Latency Comparison: Blockchain vs Traditional Logging")
plt.legend()
plt.grid(True, **GRID_STYLE)
plt.tight_layout()

plt.savefig("latency.png", dpi=300)
plt.show()
print("Saved: latency.png")


# ── 2. Throughput ──────────────────────────────────────────────────────────────

plt.figure()

plt.plot(df["workload"], df["t_throughput"],
         marker='o', markersize=MARKER_SIZE,
         color=COLOR_TRADITIONAL, label="Traditional")
annotate_points(df["workload"], df["t_throughput"],
                fmt="{:.0f}", color=COLOR_TRADITIONAL)

plt.plot(df["workload"], df["b_throughput"],
         marker='o', markersize=MARKER_SIZE,
         color=COLOR_BLOCKCHAIN, label="Blockchain")
annotate_points(df["workload"], df["b_throughput"],
                fmt="{:.1f}", color=COLOR_BLOCKCHAIN)

plt.xscale("log")
plt.yscale("log")
plt.xticks(X_TICKS, X_LABELS)

plt.xlabel("Workload (log entries)")
plt.ylabel("Throughput (logs/sec)")
plt.title("Throughput Comparison: Blockchain vs Traditional Logging")
plt.legend()
plt.grid(True, **GRID_STYLE)
plt.tight_layout()

plt.savefig("throughput.png", dpi=300)
plt.show()
print("Saved: throughput.png")


# ── 3. Estimated Cost ──────────────────────────────────────────────────────────
# Linear y-scale intentional: shows cost explosion clearly at scale

plt.figure()

plt.plot(df["workload"], df["cost_usd"],
         marker='o', markersize=MARKER_SIZE,
         color=COLOR_BLOCKCHAIN, label="Blockchain")
annotate_points(df["workload"], df["cost_usd"],
                fmt="${:,.2f}", color=COLOR_BLOCKCHAIN)

plt.xscale("log")
plt.xticks(X_TICKS, X_LABELS)

plt.text(
    0.97, 0.05,
    f"Gas Price: {GAS_PRICE_GWEI} gwei\nETH Price: ${ETH_PRICE_USD:,} USD",
    transform=plt.gca().transAxes,
    fontsize=9,
    verticalalignment='bottom',
    horizontalalignment='right',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7)
)

plt.xlabel("Workload (log entries)")
plt.ylabel("Estimated Cost (USD)")
plt.title("Estimated Cost vs Workload (Blockchain Logging)")
plt.legend()
plt.grid(True, **GRID_STYLE)
plt.tight_layout()

plt.savefig("cost.png", dpi=300)
plt.show()
print("Saved: cost.png")


# ── 4. Verification Time ───────────────────────────────────────────────────────

plt.figure()

plt.plot(df["workload"], df["verification_time"],
         marker='o', markersize=MARKER_SIZE,
         color=COLOR_BLOCKCHAIN, label="Blockchain")
annotate_points(df["workload"], df["verification_time"],
                fmt="{:.5f}", color=COLOR_BLOCKCHAIN)

plt.xscale("log")
plt.yscale("log")
plt.xticks(X_TICKS, X_LABELS)

plt.xlabel("Workload (log entries)")
plt.ylabel("Verification Time (seconds)")
plt.title("Log Verification Time (Blockchain)")
plt.legend()
plt.grid(True, **GRID_STYLE)
plt.tight_layout()

plt.savefig("verification.png", dpi=300)
plt.show()
print("Saved: verification.png")


# ── Done ───────────────────────────────────────────────────────────────────────

print("\nAll graphs saved: latency.png | throughput.png | cost.png | verification.png")