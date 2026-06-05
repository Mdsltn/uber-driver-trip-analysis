"""
generate_charts.py
Run this script in your project folder (where uberdrive-2.csv lives).
It will create an /images folder and save all charts used in the README.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
os.makedirs("images", exist_ok=True)
sns.set_theme(style="whitegrid", palette="muted")
BLUE = "#2563EB"
ACCENT = "#F59E0B"

df = pd.read_csv("uberdrive-2.csv")

# ── Clean ──────────────────────────────────────────────────────────────────────
df.columns = df.columns.str.strip()
df = df.dropna(subset=["START_DATE*", "MILES*"])
df["START_DATE*"] = pd.to_datetime(df["START_DATE*"], errors="coerce")
df = df.dropna(subset=["START_DATE*"])
df["MILES*"] = pd.to_numeric(df["MILES*"], errors="coerce")
df["CATEGORY*"] = df["CATEGORY*"].str.strip()
df["PURPOSE*"] = df["PURPOSE*"].str.strip() if "PURPOSE*" in df.columns else "Unknown"

df["month"]      = df["START_DATE*"].dt.month
df["month_name"] = df["START_DATE*"].dt.strftime("%b")
df["day_of_week"]= df["START_DATE*"].dt.day_name()
df["hour"]       = df["START_DATE*"].dt.hour

DOW_ORDER = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MONTH_ORDER = ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]

# ── Chart 1 : Business vs Personal trips ──────────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 6))
cat_counts = df["CATEGORY*"].value_counts()
colors = [BLUE, ACCENT]
wedges, texts, autotexts = ax.pie(
    cat_counts,
    labels=cat_counts.index,
    autopct="%1.1f%%",
    colors=colors,
    startangle=90,
    textprops={"fontsize": 13}
)
for at in autotexts:
    at.set_fontweight("bold")
ax.set_title("Trip Category Split\nBusiness vs Personal", fontsize=14, fontweight="bold", pad=20)
plt.tight_layout()
plt.savefig("images/01_category_split.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 1 saved")

# ── Chart 2 : Top trip purposes ───────────────────────────────────────────────
if "PURPOSE*" in df.columns:
    purpose_counts = (
        df[df["PURPOSE*"].notna() & (df["PURPOSE*"] != "")]
        ["PURPOSE*"].value_counts().head(10)
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(purpose_counts.index[::-1], purpose_counts.values[::-1], color=BLUE, edgecolor="white")
    ax.set_xlabel("Number of Trips", fontsize=11)
    ax.set_title("Top 10 Trip Purposes", fontsize=14, fontweight="bold")
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 2, bar.get_y() + bar.get_height()/2,
                str(int(w)), va="center", fontsize=10)
    ax.spines[["top","right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig("images/02_top_purposes.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("✓ Chart 2 saved")

# ── Chart 3 : Trips by day of week ────────────────────────────────────────────
dow_counts = df["day_of_week"].value_counts().reindex(DOW_ORDER, fill_value=0)
fig, ax = plt.subplots(figsize=(9, 4))
bar_colors = [ACCENT if d in ["Saturday","Sunday"] else BLUE for d in DOW_ORDER]
ax.bar(DOW_ORDER, dow_counts.values, color=bar_colors, edgecolor="white")
ax.set_ylabel("Number of Trips", fontsize=11)
ax.set_title("Trips by Day of Week  (orange = weekend)", fontsize=14, fontweight="bold")
ax.spines[["top","right"]].set_visible(False)
for i, v in enumerate(dow_counts.values):
    ax.text(i, v + 2, str(v), ha="center", fontsize=9)
plt.tight_layout()
plt.savefig("images/03_trips_by_dow.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 3 saved")

# ── Chart 4 : Monthly miles ───────────────────────────────────────────────────
monthly_miles = (
    df.groupby("month_name")["MILES*"].sum()
    .reindex([m for m in MONTH_ORDER if m in df["month_name"].unique()])
)
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(monthly_miles.index, monthly_miles.values, marker="o", color=BLUE, linewidth=2.5, markersize=7)
ax.fill_between(monthly_miles.index, monthly_miles.values, alpha=0.15, color=BLUE)
ax.set_ylabel("Total Miles", fontsize=11)
ax.set_title("Total Miles Driven per Month", fontsize=14, fontweight="bold")
ax.spines[["top","right"]].set_visible(False)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
plt.tight_layout()
plt.savefig("images/04_monthly_miles.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 4 saved")

# ── Chart 5 : Miles distribution ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(df["MILES*"].clip(upper=50), bins=40, color=BLUE, edgecolor="white", alpha=0.85)
ax.axvline(df["MILES*"].median(), color=ACCENT, linewidth=2, linestyle="--",
           label=f"Median: {df['MILES*'].median():.1f} mi")
ax.set_xlabel("Trip Distance (miles)", fontsize=11)
ax.set_ylabel("Frequency", fontsize=11)
ax.set_title("Distribution of Trip Distances (capped at 50 mi)", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)
ax.spines[["top","right"]].set_visible(False)
plt.tight_layout()
plt.savefig("images/05_distance_distribution.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓ Chart 5 saved")

# ── Summary stats (for README) ────────────────────────────────────────────────
print("\n── KEY STATS (paste into README if different from defaults) ──")
print(f"Total trips      : {len(df):,}")
print(f"Total miles      : {df['MILES*'].sum():,.1f}")
print(f"Avg trip distance: {df['MILES*'].mean():.1f} miles")
print(f"Median distance  : {df['MILES*'].median():.1f} miles")
print(f"Business trips % : {(df['CATEGORY*']=='Business').mean()*100:.1f}%")
print(f"Busiest day      : {df['day_of_week'].value_counts().idxmax()}")
print(f"Busiest month    : {df['month_name'].value_counts().idxmax()}")
if "PURPOSE*" in df.columns:
    print(f"Top purpose      : {df['PURPOSE*'].value_counts().idxmax()}")
print("\nAll 5 charts saved to /images folder.")
