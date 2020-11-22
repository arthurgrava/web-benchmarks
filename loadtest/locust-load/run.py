import os

import fire


COMMAND = (
    "locust -f app/calls.py --config app/base.cfg --skip-log-setup "
    "--host {host} --users {users} --spawn-rate {users} "
    "--run-time {step_time} --csv {outfile} DBCall CalculationCall"
)


def run(users: int, step: int, step_time: str, app: str, host: str):
    amount_of_runs = int(users / step)
    runs = 0
    while runs < amount_of_runs:
        current_users = (runs + 1) * step
        cmd = COMMAND.format(
            host=host,
            users=current_users,
            step_time=step_time,
            outfile=f"{app}-{current_users}u-{step_time}",
        )
        print(f"Running round for {current_users} users for {step_time}")
        os.system(cmd)
        runs += 1


if __name__ == "__main__":
    fire.Fire(run)
