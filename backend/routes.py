from flask import Flask
from flask_restful import Resource, Api

from buildings_sheet_backend import Buildings
from templates_sheet_backend import Templates
from users_sheet_backend import Users
from tasks_sheet_backend import Tasks

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

    def get(self, bldg_name):
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

    def get(self, temp_name):
        return self.t1.getOneTemplateByName(temp_name)

    def put(self, temp_name):
        self.t1.addTemplate(temp_name)

    def delete(self, temp_name):
        self.t1.removeTemplate(temp_name)


class OneTemplateByIDRoute(Resource):
    def __init__(self):
        self.t1 = Templates()

    def get(self, temp_id):
        return self.t1.getOneTemplateByID(temp_id)


class ALLAdminsRoute(Resource):
    def __init__(self):
        self.a1 = Users()

    def get(self):
        return self.a1.get_admins()


class AdminsRoute(Resource):
    def __init__(self):
        self.user = Users()

    def put(self, target):
        return self.user.add_admin(target)

    def delete(self, target):
        return self.user.remove_admin(target)

    def get(self, target):
        return self.user.search_admins(target)


class ALLOperatorsRoute(Resource):
    def __init__(self):
        self.user = Users()

    def get(self):
        return self.user.get_operators()


class OperatorsRoute(Resource):
    def __init__(self):
        self.user = Users()

    def put(self, target):
        return self.user.add_operator(target)

    def delete(self, target):
        return self.user.remove_operator(target)

    def get(self, target):
        return self.user.search_operators(target)


class ALLTasksRoute(Resource):
    def __init__(self):
        self.tasks = Tasks()

    def get(self):
        return self.tasks.get_all_tasks()


class TasksRoute(Resource):
    def __init__(self):
        self.tasks = Tasks()

    def delete(self, task_id):
        return self.tasks.delete_task(task_id)

    def get(self, task_id):
        return self.tasks.get_task(task_id)


class UpdateTaskRoute(Resource):
    def __init__(self):
        self.tasks = Tasks()

    def update(self, task_info):
        return self.tasks.update_task(task_info)


class BatchUpdateTaskRoute(Resource):
    def __init__(self):
        self.tasks = Tasks()

    def update(self, task_list):
        return self.tasks.batch_update_tasks(task_list)


api.add_resource(AllBuildingsRoute, '/bldgs/all')
api.add_resource(AllRoomsRoute, '/rooms/all')
api.add_resource(AllTemplatesRoute, '/temps/all')
api.add_resource(OneBuildingRoute, '/bldgs/<string:bldg_name>')
api.add_resource(OneRoomRoute, '/rooms/<string:bldg_name>/room_<string:room_name>')
api.add_resource(OneTemplateRoute, '/temps/<string:temp_name>')
api.add_resource(OneTemplateByIDRoute, '/temps/id_<string:temp_id>')

api.add_resource(ALLAdminsRoute, '/admins/all')
api.add_resource(AdminsRoute, '/admins/<string:target>')

api.add_resource(ALLOperatorsRoute, '/operators/all')
api.add_resource(OperatorsRoute, '/operators/<string:target>')

api.add_resource(ALLTasksRoute, '/tasks/all')
api.add_resource(TasksRoute, '/tasks/taskID_<int:task_id>')
api.add_resource(UpdateTaskRoute, '/tasks/taskInfo_<string:task_info>')
api.add_resource(BatchUpdateTaskRoute, '/tasks/taskList_<string:task_list>')

if __name__ == '__main__':
    app.run(debug=True)
