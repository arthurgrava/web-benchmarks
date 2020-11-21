from datetime import datetime
from typing import List

import fire
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_theme(style="darkgrid")


def rename_and_drop_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Rename columns from locust output and drop some of the columns that will not be used in
    this script
    """
    local = data.copy(deep=True)
    cols = {}
    for col in local.columns:
        if "%" in col:
            cols[col] = ("p" + col.lower().replace("%", "")).strip()
    cols.update({
        "User Count": "concurrent_users",
        "Timestamp": "timestamp",
        "Total Min Response Time": "p00",
        "Requests/s": "rps",
        "Failures/s": "failures_ps",
    })
    local = local.rename(columns=cols)
    local["timestamp"] = local["timestamp"].apply(lambda v: datetime.fromtimestamp(v))
    local["rpm"] = local["rps"].apply(lambda v: v * 60.0)
    columns = sorted(list(cols.values()) + ["rpm"])
    return local[columns]


def transform_to_measure_file(data: pd.DataFrame, keep_columns: List[str]) -> pd.DataFrame:
    """
    Extracts the latency per percentile and transform each in a row also adding the required
    columns to keep, returning a Dataframe with columns `kept, measure, latency`
    """
    percentiles = [col for col in data.columns if col.startswith("p")]
    values = []
    for row in data.values:
        base = [row[data.columns.get_loc(c)] for c in keep_columns]
        for c in percentiles:
            values.append(base + [c, row[data.columns.get_loc(c)]])
    return pd.DataFrame(data=values, columns=keep_columns + ["measure", "latency"])


def plot_latencies(data: pd.DataFrame, latency: pd.DataFrame, outfile: str) -> None:
    """
    Creates a plot with 4 different graphs and saves it to the `outfile`:
    - Plot 1 : Latency percentiles (no max) through time
    - Plot 2 : Number of requests per second through time
    - Plot 3 : Number of concurrent users requesting the API through time
    - Plot 4 : Number of requests per minute through time
    """
    fig, axs = plt.subplots(nrows=4)
    fig.set_figheight(15)
    fig.set_figwidth(20)
    sns.lineplot(x="timestamp", y="latency", hue="measure", data=latency[latency["measure"] != "p100"], ax=axs[0])
    sns.lineplot(x="timestamp", y="rps", data=data, ax=axs[1])
    sns.lineplot(x="timestamp", y="concurrent_users", data=data, ax=axs[2])
    sns.lineplot(x="timestamp", y="rpm", data=data, ax=axs[3])
    fig.savefig(outfile, dpi=150)
    fig.clear()


def aggreate_by_concurrent_users(data: pd.DataFrame, framework: str, server: str, outfile: str) -> None:
    group = data.groupby(["concurrent_users"])
    agg = pd.DataFrame({
        "framework": framework,
        "server": server,
        "max_rps": group["rps"].max(),
        "min_rps": group["rps"].min(),
        "max_rpm": group["rpm"].max(),
        "min_rpm": group["rpm"].min(),
    }).reset_index()
    agg.to_csv(outfile)


def run(filename: str, outfile: str, framework: str, server: str) -> None:
    data = pd.read_csv(filename)
    local = rename_and_drop_columns(data[data["Name"] == "Aggregated"])
    latency = transform_to_measure_file(local, ["timestamp"])
    outfile = outfile.split(".")[0]
    plot_latencies(local, latency, f"{outfile}.png")
    aggreate_by_concurrent_users(local, framework, server, f"{outfile}.csv")


if __name__ == "__main__":
    fire.Fire(run)
