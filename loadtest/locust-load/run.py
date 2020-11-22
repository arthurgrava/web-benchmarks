import os
from typing import List

import fire


COMMAND = (
    "locust -f app/calls.py --config app/base.cfg --skip-log-setup "
    "--host {host} --users {users} --spawn-rate {users} "
    "--run-time {step_time} --csv {outfile} DBCall CalculationCall"
)


def run_all_tests(users: int, step: int, step_time: str, app: str, host: str) -> List[str]:
    amount_of_runs = int(users / step)
    runs = 0
    files = []
    while runs < amount_of_runs:
        current_users = (runs + 1) * step
        outfile = f"{app}-{current_users}u-{step_time}"
        cmd = COMMAND.format(
            host=host,
            users=current_users,
            step_time=step_time,
            outfile=outfile,
        )
        print(f"Running round for {current_users} users for {step_time}")
        os.system(cmd)
        files.append(f"{outfile}_stats_history.csv")
        runs += 1
    return files


def merge_history_files(outfiles: List[str], app: str) -> None:
    with open(f"{app}_results.whoops", "w") as fw:
        first_file = True
        for outfile in outfiles:
            with open(outfile) as fr:
                first_line = True
                for line in fr:
                    if first_file and first_line:
                        fw.write(line)
                        first_file = False
                        first_line = False
                    elif first_line and not first_file:
                        first_line = False
                    else:
                        fw.write(line)

    os.system("rm *.csv")
    os.rename(f"{app}_results.whoops", f"{app}_results.csv")


def run(users: int, step: int, step_time: str, app: str, host: str) -> None:
    outfiles = run_all_tests(users, step, step_time, app, host)
    merge_history_files(outfiles, app)


if __name__ == "__main__":
    fire.Fire(run)
