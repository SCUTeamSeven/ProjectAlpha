import gspread as gs
from helpers import *

class Templates:
    def __init__(self):
        self.gc = gs.service_account(filename = 'user_creds.json')
        self.master_file = self.gc.open_by_url('https://docs.google.com/spreadsheets/d/1gXJndJl3IdzUVs8q79H0CgwZUUhGR5BUX5TfueV1tnw/edit#gid=73952533')
        self.database_sheet = self.master_file.worksheet("database")
        self.templates_count = 0
        self.start_cell = [1,9]
        self.last_cell = [1,9] # row, col
        self.max_attributes = 10 # set at 10 but value is arbitrary

    def getTemplateCount(self): # done
        range_size = len(self.database_sheet.col_values(self.start_cell[1]))
        return (range_size // 2) + 1

    def getOneTemplate(self, target): # done

        target_cell = self.database_sheet.find(target, in_column = self.start_cell[1])
        if(target_cell == None):
            #print("Target not in worksheet.")
            return {}

        target_info_start = [target_cell.row, target_cell.col + 1]
        target_info_end = [target_cell.row + 1, target_cell.col + self.max_attributes + 1]
        range = f"{coords2A1String(target_info_start[0], target_info_start[1])}:{coords2A1String(target_info_end[0], target_info_end[1])}"
        template_info = self.database_sheet.get(range)

        attribute_dict = {}
        i = 0
        while(i < len(template_info[0])):
            attribute_dict[template_info[0][i]] = template_info[1][i]
            i+=1

        return {"name": target_cell.value, "attributes" : attribute_dict}


    def getTemplates(self): #TODO
        print(len(self.database_sheet.col_values(self.start_cell[1])))
        end_cell = [self.start_cell[0] + len(self.database_sheet.col_values(self.start_cell[1])), self.start_cell[1] + self.max_attributes + 1]

        i = 1

        while (i < end_cell[0]):
            #att_names =
            #att_types =
            pass

        range = f"{coords2A1String(self.start_cell[0], self.start_cell[1])}:{coords2A1String(end_cell[0], end_cell[1])}"
        print(range)
        #return(self.database_sheet.get(range))

    def addTemplate(self, newTemplateName, attributes):
        col_amount = len(attributes)
        col_num = 1

        new_template_start_row = len(self.database_sheet.col_values(self.start_cell[1])) + 2 # placing new info two rows below
        self.database_sheet.update_cell(new_template_start_row, self.start_cell[1], newTemplateName)

        for name in attributes:
            self.database_sheet.update_cell(new_template_start_row, self.start_cell[1] + col_num, name) # can be edited as packet attributes are finalized
            self.database_sheet.update_cell(new_template_start_row + 1, self.start_cell[1] + col_num, attributes[name]) # can be edited as packet attributes are finalized
            col_num += 1

    def removeTemplate(self, target): # target will hold target id #done
        target_cell = self.database_sheet.find(target, in_column = self.start_cell[1]) # holds [row,col,value]

        if(target_cell == None):
            #print("Target not in worksheet.")
            return

        target_range_endcell = [target_cell.row + 1, target_cell.col + self.max_attributes + 1] #establishes range to extend to next row and 11 cols (10 attributes max) over
        target_info_range = f"{cell2A1String(target_cell)}:{coords2A1String(target_range_endcell[0], target_range_endcell[1])}"

        remaining_template_start = [target_cell.row + 2, target_cell.col]
        remaining_template_end = [len(self.database_sheet.col_values(target_cell.col))+1,remaining_template_start[1] + self.max_attributes + 1]
        remaining_template_range = f"{coords2A1String(remaining_template_start[0],remaining_template_start[1])}:{coords2A1String(remaining_template_end[0],remaining_template_end[1])}"

        template_length = remaining_template_end[0] - remaining_template_start[0]
        new_range_end = [target_cell.row + template_length, target_range_endcell[1]]

        new_range = f"{cell2A1String(target_cell)}:{coords2A1String(new_range_end[0], new_range_end[1])}"

        remaining_template_info = self.database_sheet.get(remaining_template_range)
        self.database_sheet.batch_clear([target_info_range, remaining_template_range])
        self.database_sheet.update(new_range, remaining_template_info)
