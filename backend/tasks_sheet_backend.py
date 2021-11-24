import gspread as gs
import pandas as pd


class Tasks:
    def __init__(self):
        self.gc = gs.service_account(filename="test_bot.json")
        self.database_file = self.gc.open_by_url('https://docs.google.com/spreadsheets/d/1L-x43qhRBlNMnydyp'
                                                 '-MZkqsXVXq4DhvvC9JsyjYziBs/edit#gid=73952533')
        self.tasks = self.database_file.worksheet('database')
        self.header = self.tasks.row_values(1)[:7]
        self.last = self.tasks.find("LAST", in_column=1)

    def find_task(self, target):
        return self.tasks.find(target, in_column=1)

    def get_task(self, target):
        target_cell = self.find_task(target)
        if target_cell is not None:
            target_row = self.tasks.row_values(target_cell.row)[:7]
            return dict(zip(self.header, target_row))
        else:
            print("Error: TaskID(" + target + ") not found.")

    def create_task(self, task_info):
        pass

    def complete_task(self, target):
        pass


test = Tasks()
print(test.get_task("1"))
test.get_task("101")
