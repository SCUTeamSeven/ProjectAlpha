import gspread as gs


class Users:
    def __init__(self):     # Initiates user object through gspread authentication
        self.gc = gs.service_account(filename="test_bot.json")
        self.database_file = self.gc.open_by_url('https://docs.google.com/spreadsheets/d'
                                                 '/13rNCLMxFNuuAJTTg9TeBIREOrr793I1PGwssldGqizA/edit#gid=73952533')
        self.users = self.database_file.worksheet("Users")
        self.operator_count = len(self.users.col_values(1)) - 1
        self.admin_count = len(self.users.col_values(2)) - 1

    def get_operators(self):    # Returns a list of operators
        return self.users.col_values(1)[1:-1]

    def get_admins(self):       # Returns a list of admins
        return self.users.col_values(2)[1:-1]

    def search_operators(self, target):     # Confirms operator membership of target
        return target in self.get_operators()

    def search_admins(self, target):        # Confirms admin membership of target
        return target in self.get_admins()

    def add_operator(self, new_operator):   # Adds an operator
        if not self.search_operators(new_operator):
            last = self.users.find("LAST", in_column=1)
            self.users.update_cell(last.row + 1, last.col, "LAST")
            self.users.update_cell(last.row, last.col, new_operator)
        else:
            print("Error: " + new_operator + " is already an operator.")

    def add_admin(self, new_admin):     # Adds an admin
        if not self.search_admins(new_admin):
            last = self.users.find("LAST", in_column=2)
            self.users.update_cell(last.row + 1, last.col, "LAST")
            self.users.update_cell(last.row, last.col, new_admin)
        else:
            print("Error: " + new_admin + " is already an admin.")

    def remove_operator(self, target):      # Removes operator
        if self.search_operators(target):
            last_pos = self.users.find("LAST", in_column=1).row + 1
            cell_list = self.users.range('A2:A' + str(last_pos))
            operators = self.users.col_values(1)[1:]
            operators.remove(target)
            operators += ["", ""]
            for i in range(len(cell_list)):
                cell_list[i].value = operators[i]
            self.users.update_cells(cell_list)
        else:
            print("Error: " + target + " is not an operator.")

    def remove_admin(self, target):     # Removes admin
        if self.search_admins(target):
            last_pos = self.users.find("LAST", in_column=2).row + 1
            cell_list = self.users.range('B2:B' + str(last_pos))
            admins = self.users.col_values(2)[1:]
            admins.remove(target)
            admins += ["", ""]
            for i in range(len(cell_list)):
                cell_list[i].value = admins[i]
            self.users.update_cells(cell_list)
        else:
            print("Error: " + target + " is not an admin.")


test = Users()
print(test.get_operators())
print(test.get_admins())
test.add_admin("axel@scu.edu")
print(test.search_admins("axel@scu.edu"))
print(test.search_operators("test@scu.edu"))
print(test.search_admins("dummy"))
test.add_admin("Test")
test.remove_admin("Test")
test.add_operator("Test")
test.remove_operator("Test")
