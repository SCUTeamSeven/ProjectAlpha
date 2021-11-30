<template>
  <div class="main-view">
    <Header @headerAuth="onAuth" @currentPage="updatePage"></Header>
    <aTasks v-if="currentPage === 'Tasks' && isAdmin" :buildings="buildings" :taskTypes="taskTypes"
    @updateTaskTypes="updateTaskTypes"
    @assignTasks="assignTasks"
    />
    <Buildings v-if="currentPage === 'Buildings' && isAdmin" :buildings="buildings" :tasks="tasks" @updateBuildings="updateBuildings"></Buildings>
    <Employees v-if="currentPage === 'Employees' && isAdmin"></Employees>
    <div v-if="currentPage === 'Home' && isAuthed">
      <h1> Search Tasks </h1>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import aTasks from '@/views/aTasks.vue'
import Buildings from '@/views/Buildings.vue'
import Employees from '@/views/Employees.vue'

export default {
  name: 'Home',
  components: {
    Header,
    aTasks,
    Buildings,
    Employees
  },
  data () {
    return {
      user: {},
      isAuthed: false,
      isAdmin: false,
      currentPage: 'Home',
      buildings: {},
      tasks: {},
      taskTypes: {}
    }
  },
  methods: {
    onAuth (e) {
      if (e) {
        this.user = e
        this.isAuthed = true
        this.isAdmin = this.user.isAdmin
      } else {
        this.isAuthed = false
        alert('User has not been authenticated.')
      }
    },
    updatePage (e) {
      this.currentPage = e
    },
    updateTaskTypes (e) {
      this.taskTypes = e
    },
    updateBuildings (e) {
      this.buildings = e
      console.log(this.buildings)
    },
    assignTasks (e) {
      var id = 0
      if (this.tasks.length !== 0) {
        id = this.tasks[this.tasks.length - 1].taskID + 1
      }
      for (var i in e[1]) {
        var task = {
          taskID: id++,
          building: e[1][i].building,
          room: e[1][i].room,
          date: new Date().toLocaleDateString(),
          operator: '',
          payload: [],
          status: 'unassigned'
        }
        for (var j in e[0].attributes) {
          task.payload.push({ id: e[0].attributes[j].id, value: '' })
        }
        this.tasks.push(task)
      }
      console.log(this.tasks)
    }
  },
  beforeMount () {
    // API call to run getAllBuildings() here
    this.tasks = [
      {
        taskID: 0,
        building: 'building 1',
        room: 'room 3',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 1,
        building: 'building 1',
        room: 'room 1',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 2,
        building: 'building 1',
        room: 'room 2',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 3,
        building: 'building 1',
        room: 'room 3',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 4,
        building: 'building 1',
        room: 'room 4',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 5,
        building: 'building 1',
        room: 'room 5',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 6,
        building: 'test',
        room: '124',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 7,
        building: 'test',
        room: '1203',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 8,
        building: 'test',
        room: '125',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 9,
        building: 'building 1',
        room: 'room 1',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 10,
        building: 'building 1',
        room: 'room 2',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 11,
        building: 'building 1',
        room: 'room 3',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 12,
        building: 'building 1',
        room: 'room 4',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 13,
        building: 'building 1',
        room: 'room 5',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 14,
        building: 'building 2',
        room: 'room 4',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 15,
        building: 'building 2',
        room: 'room 1',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 16,
        building: 'building 3',
        room: 'room 4',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 17,
        building: 'building 4',
        room: 'room 1',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 18,
        building: 'building 4',
        room: 'room 2',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 19,
        building: 'building 4',
        room: 'room 3',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 20,
        building: 'building 4',
        room: 'room 4',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 21,
        building: 'building 4',
        room: 'room 5',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 22,
        building: 'building 5',
        room: 'room 2',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 23,
        building: 'building 5',
        room: 'room 1',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 24,
        building: 'building 5',
        room: 'room 3',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 25,
        building: 'building 5',
        room: 'room 4',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 26,
        building: 'building 5',
        room: 'room 5',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 27,
        building: 'building 6',
        room: 'room 5',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          },
          {
            id: 4,
            value: ''
          },
          {
            id: 5,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 28,
        building: 'test',
        room: '124',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 29,
        building: 'building 6',
        room: 'room 4',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 30,
        building: 'building 6',
        room: 'room 2',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 31,
        building: 'building 5',
        room: 'room 2',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 32,
        building: 'building 5',
        room: 'room 1',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 33,
        building: 'building 5',
        room: 'room 3',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 34,
        building: 'building 5',
        room: 'room 4',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          }
        ],
        status: 'unassigned'
      },
      {
        taskID: 35,
        building: 'building 5',
        room: 'room 5',
        date: '11/29/2021',
        operator: '',
        payload: [
          {
            id: 0,
            value: ''
          },
          {
            id: 1,
            value: ''
          },
          {
            id: 2,
            value: ''
          },
          {
            id: 3,
            value: ''
          }
        ],
        status: 'unassigned'
      }
    ]
    this.taskTypes = [
      {
        name: 'Task Type 1',
        attributes: [
          {
            name: 'Task Attribute 1',
            id: 0,
            type: 'Small Text Field'
          },
          {
            name: 'Task Attribute 2',
            id: 1,
            type: 'Checkbox'
          },
          {
            name: 'Task Attribute 3',
            id: 2,
            type: 'Checkbox'
          },
          {
            name: 'Task Attribute 4',
            id: 3,
            type: 'Large Text Field'
          }
        ]
      },
      {
        name: 'Task Type 2',
        attributes: [
          {
            name: 'Task Attribute 1',
            id: 0,
            type: 'Small Text Field'
          },
          {
            name: 'Task Attribute 2',
            id: 1,
            type: 'Checkbox'
          },
          {
            name: 'Task Attribute 4',
            id: 2,
            type: 'Large Text Field'
          }
        ]
      },
      {
        name: 'Task Type 3',
        attributes: [
          {
            name: 'Task Attribute 1',
            id: 0,
            type: 'checkbox'
          },
          {
            name: 'Task Attribute 2',
            id: 1,
            type: 'Checkbox'
          },
          {
            name: 'Task Attribute 3',
            id: 2,
            type: 'Checkbox'
          },
          {
            name: 'Task Attribute 4',
            id: 3,
            type: 'Large Text Field'
          },
          {
            name: 'Task Attribute 5',
            id: 4,
            type: 'Checkbox'
          },
          {
            name: 'Task Attribute 6',
            id: 5,
            type: 'Checkbox'
          }
        ]
      },
      {
        name: 'Task Type 4',
        attributes: [
          {
            name: 'Task Attribute 1',
            id: 0,
            type: 'Small Text Field'
          },
          {
            name: 'Task Attribute 2',
            id: 1,
            type: 'Checkbox'
          },
          {
            name: 'Task Attribute 3',
            id: 2,
            type: 'Checkbox'
          },
          {
            name: 'Task Attribute 4',
            id: 3,
            type: 'Large Text Field'
          }
        ]
      }
    ]
    this.buildings = [
      { name: 'building 1', rooms: ['room 1', 'room 2', 'room 3', 'room 4', 'room 5'] },
      { name: 'building 2', rooms: ['room 1', 'room 2', 'room 3', 'room 4', 'room 5'] },
      { name: 'building 3', rooms: ['room 1', 'room 2', 'room 3', 'room 4', 'room 5'] },
      { name: 'building 4', rooms: ['room 1', 'room 2', 'room 3', 'room 4', 'room 5'] },
      { name: 'building 5', rooms: ['room 1', 'room 2', 'room 3', 'room 4', 'room 5'] },
      { name: 'building 6', rooms: ['room 1', 'room 2', 'room 3', 'room 4', 'room 5'] },
      { name: 'test', rooms: ['124', '1203', '125'] }
    ]
    console.log(this.tasks, this.buildings, this.taskTypes)
  }
}
</script>

<style>
 h1 {
   padding:30px 20px;
   font-size: 3em;
   margin: 0;
   background-color:#e6ebee;
 }
</style>
