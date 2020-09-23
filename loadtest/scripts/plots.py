import fire
import pandas as pd
import seaborn as sns


sns.set_theme(style="darkgrid")


def plot_rps_per_user(data: pd.DataFrame):
    df = data.copy(deep=True)
    df["application"] = df["app"] + "-" + df["container"]
    plot = sns.lineplot(
        x="users",
        y="rps",
        hue="application",
        data=df,
        markers=True,
    )
    plot.get_figure().savefig("rps_per_user.png")
    plot.clear()


def run(aggfile):
    data = pd.read_csv(aggfile)
    plot_rps_per_user(data)


if __name__ == "__main__":
    fire.Fire(run)
