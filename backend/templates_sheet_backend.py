import gspread as gs
import json as js
from helpers import *

class Templates:
    def __init__(self):
        self.gc = gs.service_account(filename = 'user_creds.json')
        self.master_file = self.gc.open_by_url('https://docs.google.com/spreadsheets/d/1gXJndJl3IdzUVs8q79H0CgwZUUhGR5BUX5TfueV1tnw/edit#gid=73952533')
        self.database_sheet = self.master_file.worksheet("database")
        self.templates_count = 0
        self.start_cell = [1,9]
        self.max_attributes = 10 # set at 10 but value is arbitrary

    def getTemplateCount(self): # done
        range_size = len(self.database_sheet.col_values(self.start_cell[1]))
        return (range_size // 2) + 1

    def getOneTemplateByName(self, target): # done
        target_cell = self.database_sheet.find(target, in_column = self.start_cell[1])
        if(target_cell == None):
            #print("Target not in worksheet.")
            return {}

        attribute_list = []

        range = f"{coords2A1String(target_cell.row, target_cell.col + 1)}:{coords2A1String(target_cell.row, target_cell.col + self.max_attributes + 1)}"
        atts = self.database_sheet.get(range)
        atts = atts[0]

        for a in atts:
            att = js.loads(a)
            attribute_list.append(att)


        return {"name": target_cell.value, "attributes" : attribute_list}

    def getOneTemplateByID(self, target): # done
        target_cell = self.database_sheet.find(target, in_column = self.start_cell[1])
        if(target_cell == None):
            #print("Target not in worksheet.")
            return {}

        attribute_list = []

        range = f"{coords2A1String(target_cell.row-1, target_cell.col + 1)}:{coords2A1String(target_cell.row-1, target_cell.col + self.max_attributes)}"
        atts = self.database_sheet.get(range)
        atts = atts[0]

        for a in atts:
            att = js.loads(a)
            attribute_list.append(att)

        return {"name": target_cell.value, "attributes" : attribute_list}


    def getTemplateNames(self): #TODO add attributes

        end_cell = [self.start_cell[0] + len(self.database_sheet.col_values(self.start_cell[1])), self.start_cell[1]]
        range = f"{coords2A1String(self.start_cell[0], self.start_cell[1])}:{coords2A1String(end_cell[0], end_cell[1])}"
        task_types = self.database_sheet.get(range)

        i = 0
        task_list = []
        task_len = len(task_types)
        #print(f"{task_len} is the length")
        while (i < task_len):
            #print(f"currently at i = {i}\n")
            task_list.append({"name" : task_types[i][0], "id": task_types[i+1][0]})
            i += 2

        return(task_list)

    def getTemplates(self):
        col_size = len(self.database_sheet.col_values(self.start_cell[1]))
        end_cell = [self.start_cell[0] + col_size, self.start_cell[1]]

        templates = []
        i = 1
        while (i < col_size):
            range = f"{coords2A1String(i, self.start_cell[1])}:{coords2A1String(i+1, self.start_cell[1] + self.max_attributes + 1)}"
            template_info = self.database_sheet.get(range)
            attributes = []

            task_name = template_info[0].pop(0)
            task_id = template_info[1].pop()
            for att in template_info[0]:
                att = js.loads(att)
                attributes.append(att)

            templates.append({"name": task_name,"id" : task_id, "attributes" : attributes})
            i += 2

        return templates


    def addTemplate(self, newTemplateName, attributes): #TODO: add IDs
        if (self.database_sheet.find(target, in_column = self.start_cell[1]) is not None):
            return

        col_size = len(self.database_sheet.col_values(self.start_cell[1]))
        range = f"{coords2A1String(col_size, self.start_cell[1])}:{coords2A1String(col_size, self.start_cell[1])}"
        last_id = int(self.database_sheet.get(range)[0].pop(0))

        new_template_start_row = col_size + 1 # placing new info two rows below
        self.database_sheet.update_cell(new_template_start_row, self.start_cell[1], newTemplateName)
        self.database_sheet.update_cell(new_template_start_row+1, self.start_cell[1], last_id+1)

        attributes = js.loads(attributes)
        attributes_list = attributes['attributes']
        col_amount = len(attributes_list)
        col_num = 1

        for att in attributes_list:
            att_info = js.dumps(att)
            self.database_sheet.update_cell(new_template_start_row, self.start_cell[1] + col_num, att_info) # can be edited as packet attributes are finalized
            col_num += 1

    def removeTemplate(self, target): # target will hold target id #done
        target_cell = self.database_sheet.find(target, in_column = self.start_cell[1]) # holds [row,col,value]

        if(target_cell == None):
            return

        # copies templates below target and pastes them in place of target, filling blanks in database
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

    def editTemplateName(self,newName):
        pass
