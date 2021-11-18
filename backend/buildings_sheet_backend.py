import gspread as gs
from helpers import *


class Buildings:
    def __init__(self):
        self.gc = gs.service_account(filename = 'user_creds.json')
        self.buildings_file = self.gc.open_by_url('https://docs.google.com/spreadsheets/d/1gXJndJl3IdzUVs8q79H0CgwZUUhGR5BUX5TfueV1tnw/edit')
        self.buildings = self.buildings_file.worksheet('buildings')
        self.buildings_count = len(self.buildings.col_values(1))-1 # minus 1 to exclude the header
        self.start_cell = [2,1]
        self.last_cell = [2,1] # row, col

    def buildingExists(self, target): #done
        idx = self.buildings.find(target.lower())
        if(idx == None):
            return False
        return idx


    def getBuildings(self): # done
        bldg_list = self.buildings.col_values(1)
        bldg_list.pop(0) #removes header from list
        return(bldg_list) #returns list

    def getOneBuilding(self, target): #done
        scan = self.buildingExists(target)
        if(scan == False):
            return {}

        target = target.lower()
        #target_idx = self.buildings.find(target, in_row = 1)
        room_list = self.buildings.col_values(scan.col)
        bldg_name = room_list.pop(0)

        return {"name" : bldg_name, "rooms" : room_list}

    def getAllRooms(self): #done
        bldg_list = self.getBuildings()

        room_dict = []

        for b in bldg_list:
            one_bldg = self.getOneBuilding(b)
            room_dict.append(one_bldg)

        return room_dict


    def getBuildingCount(self): #done
        self.buildings_count = len(self.buildings.col_values(1))-1 # minus 1 to exclude the header
        return self.buildings_count


    def addBuilding(self,newBuildingName): # TODO: return error or somethibn
        if(self.buildingExists(newBuildingName) != False):
            return
        if(self.getBuildingCount() == 0):
            self.last_cell = self.start_cell
        else:
            self.last_cell[0] = self.start_cell[0] + self.buildings_count #moves row

        newBuildingName = newBuildingName.lower()
        self.buildings.update_cell(self.last_cell[0], self.last_cell[1], newBuildingName)
        self.buildings.update_cell(1, 2 + self.buildings_count, newBuildingName)

        self.buildings_count = len(self.buildings.col_values(1))-1 # minus 1 to exclude the header

    def removeBuilding(self, target): # TODO: return error or something
        cells = self.buildings.findall(target.lower()) # holds [[row,col,value]]
        if(not cells):
            #print("Target not in worksheet.")
            return
        target_column_idx = cells[0]

        if(target_column_idx.col == 1 + self.buildings_count): # if erasing the last columns
            target_col_length = len(self.buildings.col_values(target_column_idx.col))-1
            target_range = cell2Range(target_column_idx,len(self.buildings.col_values(target_column_idx.col))-1)
            self.buildings.batch_clear([target_range])

            target_entry = cells[1]
            target_range = cell2Range(target_entry, 0)
            self.buildings.batch_clear([target_range])
        else:
            #clears out column for deletion and swaps it out with column at last index to prevent empty spaces
            last_column_content = self.buildings.col_values(1 + self.buildings_count)
            last_column_range = col2Range(1 + self.buildings_count, 200)
            target_range = cell2Range(target_column_idx,200)
            self.buildings.batch_clear([target_range])

            i = target_column_idx.row
            while(last_column_content):
                self.buildings.update_cell(i, target_column_idx.col, last_column_content.pop(0))
                i+=1

            self.buildings.batch_clear([last_column_range])

            #clears out building cell and swaps out with bottom building cell
            target_entry = cells[1]
            last_building = self.buildings.cell(1 + self.buildings_count,1).value
            target_range = cell2Range(target_entry, 0)
            self.buildings.batch_clear([target_range])
            last_entry_range = coords2Range(1 + self.buildings_count, 1, 0)
            self.buildings.batch_clear([last_entry_range])
            self.buildings.update_cell(target_entry.row, target_entry.col,last_building)


        self.buildings_count -= 1 # minus 1 to exclude the header


    def addRoom(self, buildingName, newRoomName): # done
        building_col_idx = self.buildingExists(buildingName)# will return building from row 1
        if(building_col_idx == False):
            return

        if(self.buildings.find(newRoomName, in_column = building_col_idx.col) == None):
            row_length = len(self.buildings.col_values(building_col_idx.col))
            self.buildings.update_cell(building_col_idx.row + row_length, building_col_idx.col, newRoomName)

    def removeRoom(self, buildingName, newRoomName): #done
        building_col_idx = self.buildingExists(buildingName)
        if(building_col_idx == False):
            #print("Building not in database")
            return
        buildingName = buildingName.lower()
        newRoomName = newRoomName.lower()

        target_idx = self.buildings.find(newRoomName, in_column = building_col_idx.col)

        if(target_idx == None):
            #print("Room not in building")
            return

        room_count = len(self.buildings.col_values(building_col_idx.col))

        last_room_range = coords2Range(room_count,building_col_idx.col,0)
        last_room_name = self.buildings.cell(room_count,building_col_idx.col).value
        self.buildings.update_cell(target_idx.row, target_idx.col, last_room_name)
        self.buildings.batch_clear([last_room_range])
