import os
import random


class Config:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        userspath = os.getenv("USERS_FILE", f"{dirname}/../../user_ids.txt")
        namespath = os.getenv("NAMES_FILE", f"{dirname}/../../user_names.txt")
        self.users = self._read_text_file(userspath)
        self.names = self._read_text_file(namespath)

    def _read_text_file(self, filepath):
        with open(filepath, "r") as fr:
            return [l.strip() for l in fr]

    def get_user(self):
        return random.choice(self.users)

    def get_name(self):
        return random.choice(self.names)