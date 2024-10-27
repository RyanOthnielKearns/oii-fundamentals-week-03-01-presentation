import calendar
import matplotlib.pyplot as plt
import pandas as pd

GREEN = "#32a852"
PURPLE = "#5d3eb3"


def plot_normalized_monthly_counts(
    counts_ser: pd.Series, title: str, color: str, axis: plt.Axes
):
    month_vals = counts_ser.dt.month.value_counts(normalize=True).sort_index()
    month_vals.index = [calendar.month_abbr[x] for x in month_vals.index]

    month_vals.plot(color=color, ax=axis)

    axis.set_title(f"{title} | normalized edits by month")
    axis.set_xlabel("Month")
    axis.set_ylabel("Percentage of Total Edits")
