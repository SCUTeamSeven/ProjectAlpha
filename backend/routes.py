from flask import Flask, request
from flask_restful import Resource, Api
from buildings_sheet_backend import Buildings

app = Flask(__name__)
api = Api(app)

class AllBuildingsRoute(Resource):
    def __init__(self):
        self.b1 = Buildings()

    def get(self):
        return self.b1.getAllRooms()

class OneBuildingsRoute(Resource):
    def __init__(self):
        self.b1 = Buildings()

    def get(self,bldg_name):
        return self.b1.getOneBuilding(bldg_name)

    def put(self, bldg_name):
        self.b1.addBuilding(bldg_name)

api.add_resource(AllBuildingsRoute,'/allbldgs')
api.add_resource(OneBuildingsRoute, '/one/<string:bldg_name>')

if __name__ == '__main__':
    app.run(debug=True)
