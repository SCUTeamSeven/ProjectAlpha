<template>
  <div class="main-view">
    <Header @headerAuth="onAuth" @currentPage="updatePage"></Header>
    <aTasks v-if="currentPage === 'Tasks' && isAdmin" :buildings="buildings" :taskTypes="taskTypes" @updateTaskTypes="updateTaskTypes"></aTasks>
    <Buildings v-if="currentPage === 'Buildings' && isAdmin" :buildings="buildings"></Buildings>
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
    }
  },
  beforeMount () {
    // API call to run getAllBuildings() here
    var task = {
      taskID: 0,
      building: 'building1',
      room: 'room1',
      date: '11/19/21',
      operator: 'chris',
      payload: {
        type: 'Task Type 1',
        attributes: [
          {
            id: 0,
            value: 'text value'
          },
          {
            id: 1,
            value: 'true'
          },
          {
            id: 2,
            value: 'false'
          },
          {
            id: 3,
            value: 'large text value'
          }
        ]
      },
      status: 'inactive'
    }
    this.tasks = [task, task, task, task, task, task]
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
