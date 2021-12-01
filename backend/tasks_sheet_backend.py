import gspread as gs


class Tasks:
    def __init__(self):     # Initiates task object through gspread authentication
        self.gc = gs.service_account(filename="test_bot.json")
        self.database_file = self.gc.open_by_url('https://docs.google.com/spreadsheets/d'
                                                 '/13rNCLMxFNuuAJTTg9TeBIREOrr793I1PGwssldGqizA/edit#gid=73952533')
        self.tasks = self.database_file.worksheet('Tasks')
        self.header = self.tasks.row_values(1)[:7]          # Instantiates header descriptions
        self.last = self.tasks.find("LAST", in_column=1)    # Keeps track of last entry

    def find_task(self, target):    # Helper function to shorten gspread find functionality
        return self.tasks.find(str(target), in_column=1)

    def get_task(self, task_id):    # Returns individual task object if found
        task_id_cell = self.find_task(task_id)
        if task_id_cell is not None:
            target_row = self.tasks.row_values(task_id_cell.row)[:7]
            return dict(zip(self.header, target_row))
        else:
            print("Error: TaskID(" + task_id + ") not found.")

    def get_all_tasks(self):    # Returns all task objects in a list
        return self.tasks.get_all_records()[:-1]

    def update_task(self, task_info):   # Updates a task object. Overwrites existing information
        target_cell = self.find_task(task_info[0])

        if target_cell is None:     # If a new task, adds it to the end of the list
            self.tasks.update_cell(self.last.row + 1, 1, "LAST")
            cell_list = self.tasks.range("A" + str(self.last.row) + ":G" + str(self.last.row))
            for i in range(len(cell_list)):
                cell_list[i].value = task_info[i]
            self.tasks.update_cells(cell_list)
            self.last = self.find_task("LAST")
        else:                       # Updates existing task
            cell_list = self.tasks.range("A" + str(target_cell.row) + ":G" + str(target_cell.row))
            for i in range(len(cell_list)):
                cell_list[i].value = task_info[i]
            self.tasks.update_cells(cell_list)

    def batch_update_tasks(self, task_list):    # Batch update of tasks objects in a list
        for task in task_list:
            self.update_task(task)

    def delete_task(self, task_id):     # Deletes a task by deleting a row
        task_cell = self.find_task(task_id)
        if task_cell is not None:
            self.tasks.delete_rows(task_cell.row)
        else:
            print("Task(" + str(task_id) + ") does not exist.")


test = Tasks()
print(test.get_task("1"))
print("\n")
print(test.get_all_tasks())
print("\n")
update_info = [6, "O'Connor", "207", "11/30/21", "Axel", "Payload Info", "active"]
test.update_task(update_info)
batch_update_info = [[3, "Casa", "343", "11/30/21", "Test", "Payload Info", "unassigned"],
                     [7, "O'Connor", "207", "11/30/21", "Axel", "Payload Info", "active"],
                     [8, "O'Connor", "207", "11/30/21", "Axel", "Payload Info", "active"]]
test.batch_update_tasks(batch_update_info)
test.delete_task(7)
