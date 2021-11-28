from flask import Flask, request
from flask_restful import Resource, Api
from buildings_sheet_backend import Buildings
from templates_sheet_backend import Templates

app = Flask(__name__)
api = Api(app)

class AllBuildingsRoute(Resource):
    def __init__(self):
        self.b1 = Buildings()

    def get(self):
        return self.b1.getBuildings()

class AllRoomsRoute(Resource):
    def __init__(self):
        self.b1 = Buildings()

    def get(self):
        return self.b1.getAllRooms()

class OneBuildingRoute(Resource):
    def __init__(self):
        self.b1 = Buildings()

    def get(self,bldg_name):
        return self.b1.getOneBuilding(bldg_name)

    def put(self, bldg_name):
        self.b1.addBuilding(bldg_name)

    def delete(self, bldg_name):
        self.b1.removeBuilding(bldg_name)

class OneRoomRoute(Resource):
    def __init__(self):
        self.b1 = Buildings()

    def put(self, bldg_name, room_name):
        self.b1.addRoom(bldg_name, room_name)

    def delete(self, bldg_name, room_name):
        self.b1.removeRoom(bldg_name, room_name)

class AllTemplatesRoute(Resource):
    def __init__(self):
        self.t1 = Templates()

    def get(self):
        return self.t1.getTemplates()

class OneTemplateRoute(Resource):
    def __init__(self):
        self.t1 = Templates()

    def get(self,temp_name):
        return self.t1.getOneTemplateByName(temp_name)

    def put(self, temp_name):
        self.t1.addTemplate(temp_name)

    def delete(self, temp_name):
        self.t1.removeTemplate(temp_name)

class OneTemplateByIDRoute(Resource):
    def __init__(self):
        self.t1 = Templates()

    def get(self,temp_name):
        return self.t1.getOneTemplateID(temp_ID)


api.add_resource(AllBuildingsRoute,'/bldgs/all')
api.add_resource(AllRoomsRoute,'/rooms/all')
api.add_resource(AllTemplatesRoute,'/temps/all')

api.add_resource(OneBuildingRoute, '/bldgs/<string:bldg_name>')
api.add_resource(OneRoomRoute, '/rooms/<string:bldg_name>/room_<string:room_name>')
api.add_resource(OneTemplateRoute, '/temps/<string:temp_name>')
api.add_resource(OneTemplateByIDRoute, '/temps/id_<string:temp_ID>')



if __name__ == '__main__':
    app.run(debug=True)
