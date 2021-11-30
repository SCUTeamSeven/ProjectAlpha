import gspread as gs


class Tasks:
    def __init__(self):
        self.gc = gs.service_account(filename="test_bot.json")
        self.database_file = self.gc.open_by_url('https://docs.google.com/spreadsheets/d/1L-x43qhRBlNMnydyp'
                                                 '-MZkqsXVXq4DhvvC9JsyjYziBs/edit#gid=73952533')
        self.tasks = self.database_file.worksheet('database')
        self.header = self.tasks.row_values(1)[:7]
        self.last = self.tasks.find("LAST", in_column=1)

    def find_task(self, target):
        return self.tasks.find(str(target), in_column=1)

    def get_task(self, task_id):
        task_id_cell = self.find_task(task_id)
        if task_id_cell is not None:
            target_row = self.tasks.row_values(task_id_cell.row)[:7]
            return dict(zip(self.header, target_row))
        else:
            print("Error: TaskID(" + task_id + ") not found.")

    def get_all_tasks(self):
        return self.tasks.get_all_records()[:-1]

    def update_task(self, task_info):
        target_cell = self.find_task(task_info[0])

        if target_cell is None:
            self.tasks.update_cell(self.last.row + 1, 1, "LAST")
            cell_list = self.tasks.range("A" + str(self.last.row) + ":G" + str(self.last.row))
            for i in range(len(cell_list)):
                cell_list[i].value = task_info[i]
            self.tasks.update_cells(cell_list)
            self.last = self.find_task("LAST")
        else:
            cell_list = self.tasks.range("A" + str(target_cell.row) + ":G" + str(target_cell.row))
            for i in range(len(cell_list)):
                cell_list[i].value = task_info[i]
            self.tasks.update_cells(cell_list)

    def batch_update_tasks(self, task_list):
        for task in task_list:
            self.update_task(task)

    def delete_task(self, task_id):
        task_cell = self.find_task(task_id)
        if task_cell is not None:
            self.tasks.delete_rows(task_cell.row)
        else:
            print("Task(" + str(task_id) + ") does not exist.")


test = Tasks()
# print(test.get_task("1"))
# test.get_task("101")
# print(test.get_all_tasks())
test.delete_task(6)
test.delete_task(7)
test.delete_task(8)
# new_info = [[6, "O'Connor", "207", "11/30/21", "Axel", "Payload Info", "active"],
#             [7, "O'Connor", "207", "11/30/21", "Axel", "Payload Info", "active"],
#             [8, "O'Connor", "207", "11/30/21", "Axel", "Payload Info", "active"]]
# test.batch_update_tasks(new_info)
