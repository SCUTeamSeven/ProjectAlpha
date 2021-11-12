import gspread as gs
from helpers import *

class Templates:
    def __init__(self):
        self.gc = gs.service_account(filename = 'user_creds.json')
        self.master_sheet = self.gc.open_by_url('https://docs.google.com/spreadsheets/d/1gXJndJl3IdzUVs8q79H0CgwZUUhGR5BUX5TfueV1tnw/edit#gid=73952533')
        self.database_sheet = self.master_sheet.worksheet("database")
        self.templates_count = 0
        self.start_cell = [1,8]
        self.last_cell = [1,8] # row, col

    def getTemplates(self):
        range = f"{coords2A1String(self.start_cell[0], self.start_cell[1])}:M17"
        print(range)
        return(self.database_sheet.get(range))

    def addTemplate(self, newTemplateName, attributes):
        col_amount = len(attributes)
        col_num = 1
        for a in attributes:
            new_sheet.update_cell(start_cell[0], start_cell[1] + col_num, a["name"]) # can be edited as packet attributes are finalized
            col_num+=1

    def removeTemplate(self, target): # target will hold target id
        target_cell = self.database_sheet.find(target, in_column = self.start_cell[1]) # holds [row,col,value]

        if(target_cell == None):
            print("Target not in worksheet.")
            return

        target_range_endcell = [target_cell.row + 1, target_cell.col + 11] #establishes range to extend to next row and 11 cols (10 attributes max) over
        target_info_range = f"{cell2A1String(target_cell)}:{coords2A1String(target_range_endcell[0], target_range_endcell[1])}"

        #print(f"there are {len(self.database_sheet.col_values(target_cell.col)) - self.start_cell[0]} task IDs")
        remaining_template_start = [target_cell.row + 2, target_cell.col]
        remaining_template_end = [len(self.database_sheet.col_values(target_cell.col))+1,remaining_template_start[1] + 11]
        remaining_template_range = f"{coords2A1String(remaining_template_start[0],remaining_template_start[1])}:{coords2A1String(remaining_template_end[0],remaining_template_end[1])}"

        template_length = remaining_template_end[0] - remaining_template_start[1]
        new_range = [target_cell.row + template_length, target_range_endcell[1]]
        
        print(f"target: {target_info_range}")
        print(f"last: {remaining_template_range}")

        remaining_template_info = self.database_sheet.get(remaining_template_range)
        self.database_sheet.batch_clear([target_info_range, remaining_template_range])

        self.database_sheet.update(target_info_range, remaining_template_info)
        #print(self.database_sheet.get(target_info_range))


def main():
    t1 = Templates()
    while(True):
        next = input("""What would you like to do?\n
        'gt' - get all templates \n
        'at' - add a templates \n
        'rt' - remove template \n
        'q' - QUIT \n""")
        if(next == 'gt'):
            print(t1.getTemplates())
        elif(next == 'rt'):
            t1.removeTemplate(input("Which template ID would you like removed?\n"))
        elif(next == 'q'):
            break
        else:
            print("try different input")

main()
