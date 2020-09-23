import fire
import pandas as pd


user_count_col = "User Count"
name_col = "Name"
app_col = "app"
container_col = "container"
columns = [
    app_col, container_col, "users", "requests", "failures", "percentage_failure", "rps", "p50", "p75", "p90", "p95", "p100",
]


def filter_information_from_df(df: pd.DataFrame):
    cols = df.columns
    if user_count_col in cols:
        df = df[df[user_count_col] > 0]
        df = df[df[user_count_col] % 10 == 0]
    if name_col in cols:
        df = df[df[name_col] == "Aggregated"]
    return df


def group_by_and_keep_last(df: pd.DataFrame):
    group = df.sort_values(
        "Timestamp", ascending=True,
    ).groupby([user_count_col], sort=False)
    data = pd.DataFrame({
        "requests": group["Total Request Count"].last(),
        "failures": group["Total Failure Count"].last(),
        "percentage_failure": (group["Total Failure Count"].last() * 100) / group["Total Request Count"].last(),
        "rps": group["Requests/s"].last(),
        "p50": group["50%"].last(),
        "p75": group["75%"].last(),
        "p90": group["90%"].last(),
        "p95": group["95%"].last(),
        "p100": group["100%"].last(),
    }).reset_index()
    data = data[data["rps"] != 0.0]
    return data.rename(columns={"User Count": "users"})


def append_column_to_df(data, app, wsgi_container) -> pd.DataFrame:
    data[app_col] = app
    data[container_col] = wsgi_container
    return data.reindex(columns, axis=1)


def run(inputfile, app, wsgi_container):
    data = pd.read_csv(inputfile)
    df = filter_information_from_df(data)
    df = group_by_and_keep_last(df)
    res = append_column_to_df(df, app, wsgi_container)
    res.to_csv(f"agg_{app}_{wsgi_container}.csv", index=False)


if __name__ == "__main__":
    fire.Fire(run)
