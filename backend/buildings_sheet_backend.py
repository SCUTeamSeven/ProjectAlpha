import gspread as gs
from helpers import *



class Buildings:
    def __init__(self):
        self.gc = gs.service_account(filename = 'user_creds.json')
        self.buildings_file = self.gc.open_by_url('https://docs.google.com/spreadsheets/d/1gXJndJl3IdzUVs8q79H0CgwZUUhGR5BUX5TfueV1tnw/edit')
        self.buildings = self.buildings_file.worksheet('buildings')
        self.buildings_count = len(self.buildings.col_values(1))-1 # minus 1 to exclude the header

        self.IDCounter = 1
        self.start_cell = [2,1]
        self.last_cell = [2,1] # row, col

    def buildingExists(self, target):
        return (self.buildings.find(target.lower()) != None)

    def getBuildings(self):
        return(self.buildings.col_values(1)) # returns list

    def getBuildingCount(self):
        self.buildings_count = len(self.buildings.col_values(1))-1 # minus 1 to exclude the header
        return self.buildings_count

    def getUsers(self):
        return(self.buildings.row_values(1))

    def addBuilding(self,newBuildingName):
        newBuildingName = newBuildingName.lower()
        if(self.buildingExists(newBuildingName)):
            print("building already in system")
            return
        if(self.getBuildingCount() == 0):
            self.last_cell = self.start_cell
            self.IDCounter = 1
        else:
            self.last_cell[0] = self.start_cell[0] + self.buildings_count #moves row

        self.buildings.update_cell(self.last_cell[0], self.last_cell[1], newBuildingName)
        self.buildings.update_cell(1, 2 + self.buildings_count, newBuildingName)

        self.buildings_count = len(self.buildings.col_values(1))-1 # minus 1 to exclude the header
        print(f"there are {self.buildings_count} buildings ")

    def removeBuilding(self, target):
        cells = self.buildings.findall(target.lower()) # holds [[row,col,value]]
        if(not cells):
            print("Target not in worksheet.")
            return
        target_column_idx = cells[0]

        if(target_column_idx.col == 1 + self.buildings_count):
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
            self.buildings.update(target_range, [last_column_content])
            self.buildings.batch_clear([last_column_range])

            #clears out building cell and swaps out with bottom building cell
            target_entry = cells[1]
            print(target_entry)

            last_building = self.buildings.cell(1 + self.buildings_count,1).value
            print(f"last buidling : {last_building}")
            target_range = cell2Range(target_entry, 0)
            self.buildings.batch_clear([target_range])
            last_entry_range = coords2Range(1 + self.buildings_count, 1, 0)
            self.buildings.batch_clear([last_entry_range])
            self.buildings.update_cell(target_entry.row, target_entry.col,last_building)

        self.buildings_count -= 1 # minus 1 to exclude the header


    def addRoom(self, buildingName, newRoomName):
        building_col_idx = self.buildings.find(buildingName) # will return building from row 1
        row_length = len(self.buildings.col_values(col_idx.col))
        self.buildings.update_cell(col_idx.row + row_length, col_idx.col, newRoomName)

    def removeRoom(self, buildingName, newRoomName):
        if(not self.buildingExists(buildingName)):
            print("Building not in database")
            return
        buildingName = buildingName.lower()
        newRoomName = newRoomName.lower()

        building_col_idx = self.buildings.find(buildingName)
        target_idx = self.buildings.find(newRoomName, in_column = building_col_idx.col)

        if(target_idx == None):
            print("Room not in building")
            return

        room_count = len(self.buildings.col_values(building_col_idx.col))

        last_room_range = coords2Range(room_count,building_col_idx.col,0)
        last_room_name = self.buildings.cell(room_count,building_col_idx.col).value
        self.buildings.update_cell(target_idx.row, target_idx.col, last_room_name)
        self.buildings.batch_clear([last_room_range])

def main():
    b1 = Buildings()
    while(True):
        next = input("""What would you like to do?\n
        'ab' - add a buildings \n
        'rb' - Remove building\n
        'gb' - get all buildings \n
        'ar' - add a room \n
        'cb' - get building count \n
        'rr' - Delete room\n
        'q' - QUIT \n""")

        if(next == 'ab'):
            b1.addBuilding(input("What is your new building name?\n"))
        elif(next == 'rb'):
            b1.removeBuilding(input("What building would you like to remove?\n"))
        elif(next == 'gb'):
            print("\n")
            print(b1.getBuildings())
            print("\n")
        elif(next == 'cb'):
            print(f"Buildings in DB: {b1.getBuildingCount()}")
        elif(next == 'ar'):
            bldg_name = input("What building would you like to add to?\n")

            b1.addRoom(bldg_name, input("What is the new room number/name?\n"))

        elif(next == 'rr'):
            bldg_name = input("What building would you like to remove from?\n")
            if(b1.buildingExists(bldg_name)):
                b1.removeRoom(bldg_name, input("What room number/name to delete?\n"))
            else:
                print("building not in database")
        elif(next == 'q'):
            break
        else:
            print("Try another input")

main()
