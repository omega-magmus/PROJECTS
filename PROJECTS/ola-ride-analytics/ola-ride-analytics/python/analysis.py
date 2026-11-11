"""Exploratory analysis + charts for the Ola Bengaluru bookings dataset.

Answers the 10 Power BI questions from the project brief with matplotlib
charts saved to images/, and prints headline KPIs.

Usage (from repo root):  python python/analysis.py
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "images"
IMG.mkdir(exist_ok=True)

YELLOW, DARK, GREY = "#F5C518", "#1B1B1B", "#8C8C8C"
PALETTE = [DARK, YELLOW, "#E4572E", "#17BEBB", GREY, "#76B041", "#6C4AB6"]
plt.rcParams.update({
    "figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titleweight": "bold", "axes.titlesize": 13,
})

df = pd.read_csv(ROOT / "data" / "bookings.csv", parse_dates=["Date"])
ok = df[df["Booking_Status"] == "Success"]


def save(name):
    plt.tight_layout()
    plt.savefig(IMG / name, bbox_inches="tight")
    plt.close()


# ---------- KPIs ----------
total = len(df)
kpi = {
    "Total bookings": total,
    "Success rate %": round(100 * len(ok) / total, 2),
    "Cancelled by customer %": round(100 * (df.Booking_Status == "Canceled by Customer").mean(), 2),
    "Cancelled by driver %": round(100 * (df.Booking_Status == "Canceled by Driver").mean(), 2),
    "Driver not found %": round(100 * (df.Booking_Status == "Driver Not Found").mean(), 2),
    "Incomplete rides % (of all)": round(100 * (df.Incomplete_Rides == "Yes").sum() / total, 2),
    "Total booking value (all) INR": int(df.Booking_Value.sum()),
    "Booking value (success) INR": int(ok.Booking_Value.sum()),
    "Avg ride distance km (success)": round(ok.Ride_Distance.mean(), 2),
    "Avg driver rating": round(ok.Driver_Ratings.mean(), 2),
    "Avg customer rating": round(ok.Customer_Rating.mean(), 2),
}
for k, v in kpi.items():
    print(f"{k:35s} {v:>14,}" if isinstance(v, int) else f"{k:35s} {v:>14}")

# 1. Ride volume over time
daily = df.groupby("Date").size()
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(daily.index, daily.values, color=DARK, lw=2, marker="o", ms=4)
ax.fill_between(daily.index, daily.values, color=YELLOW, alpha=.4)
ax.set(title="1. Ride Volume Over Time (July 2024)", ylabel="Bookings per day")
save("01_ride_volume_over_time.png")

# 2. Booking status breakdown
st = df.Booking_Status.value_counts()
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(st, labels=st.index, autopct="%1.1f%%", startangle=90, colors=PALETTE,
       wedgeprops=dict(width=.45, edgecolor="white"))
ax.set_title("2. Booking Status Breakdown")
save("02_booking_status_breakdown.png")

# 3. Top vehicle types by ride distance
vd = ok.groupby("Vehicle_Type").Ride_Distance.sum().sort_values().tail(5)
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(vd.index, vd.values, color=YELLOW, edgecolor=DARK)
ax.set(title="3. Top 5 Vehicle Types by Total Ride Distance (km)")
save("03_top_vehicle_types_by_distance.png")

# 4. Avg customer rating by vehicle type
cr = ok.groupby("Vehicle_Type").Customer_Rating.mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(cr.index, cr.values, color=DARK)
ax.set(title="4. Average Customer Rating by Vehicle Type", ylim=(cr.min() - .1, cr.max() + .05))
plt.xticks(rotation=25)
save("04_avg_customer_rating_by_vehicle.png")

# 5. Cancellation reasons
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
df["Canceled_Rides_by_Customer"].value_counts().sort_values().plot.barh(ax=axes[0], color=YELLOW, edgecolor=DARK)
axes[0].set(title="5a. Cancellation Reasons - Customers", ylabel="")
df["Canceled_Rides_by_Driver"].value_counts().sort_values().plot.barh(ax=axes[1], color=DARK)
axes[1].set(title="5b. Cancellation Reasons - Drivers", ylabel="")
save("05_cancellation_reasons.png")

# 6. Revenue by payment method
pm = ok.groupby("Payment_Method").Booking_Value.sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(pm.index, pm.values / 1e6, color=PALETTE[:len(pm)])
ax.set(title="6. Revenue by Payment Method (success, INR million)")
save("06_revenue_by_payment_method.png")

# 7. Top 5 customers by booking value
tc = ok.groupby("Customer_ID").Booking_Value.sum().sort_values().tail(5)
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(tc.index, tc.values, color=YELLOW, edgecolor=DARK)
ax.set(title="7. Top 5 Customers by Total Booking Value (INR)")
save("07_top5_customers_by_value.png")

# 8. Ride distance per day
dd = ok.groupby("Date").Ride_Distance.sum()
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(dd.index, dd.values, color=DARK)
ax.set(title="8. Total Ride Distance per Day (km, successful rides)")
save("08_ride_distance_per_day.png")

# 9. Driver rating distribution by vehicle type
order = ok.groupby("Vehicle_Type").Driver_Ratings.median().sort_values().index
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.boxplot([ok.loc[ok.Vehicle_Type == v, "Driver_Ratings"] for v in order],
           tick_labels=order, patch_artist=True,
           boxprops=dict(facecolor=YELLOW), medianprops=dict(color=DARK))
ax.set(title="9. Driver Rating Distribution by Vehicle Type")
plt.xticks(rotation=25)
save("09_driver_rating_distribution.png")

# 10. Customer vs driver rating
hm = pd.crosstab(ok.Driver_Ratings.round(0), ok.Customer_Rating.round(0))
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(hm.values, cmap="YlOrBr", origin="lower", aspect="auto")
ax.set_xticks(range(len(hm.columns)), hm.columns)
ax.set_yticks(range(len(hm.index)), hm.index)
ax.set(title="10. Customer vs Driver Rating (ride count)", xlabel="Customer rating", ylabel="Driver rating")
fig.colorbar(im)
print("\nCorrelation customer vs driver rating:", round(ok.Customer_Rating.corr(ok.Driver_Ratings), 3))
save("10_customer_vs_driver_ratings.png")

# Weekend vs weekday
df["is_weekend"] = df.Date.dt.dayofweek >= 5
wk = df.groupby("is_weekend").agg(days=("Date", "nunique"), rides=("Booking_ID", "count"),
                                    avg_value=("Booking_Value", "mean"))
wk["rides_per_day"] = wk.rides / wk.days
print("\nWeekend vs weekday:\n", wk.round(1))
