<template>
  <div>
      <select v-model="selectedTask">
        <option selected :value="{name: 'All Tasks', attributes: [{name: 'Task Type',type: '' },{name: 'View Details',type: ''}]}">All Tasks</option>
        <option v-for="task in taskTemplates" :key="task" :value="task">
            {{ task.name }}
        </option>
      </select>
      <select v-model="selectedBuilding">
        <option selected :value="{name: 'All Buildings', rooms: []}">All Rooms</option>
        <option v-for="building in allBuildings" :key="building" :value="building">
            {{ building.name }}
        </option>
      </select>
      <select v-if="selectedBuilding.name !== 'All Buildings'" v-model="selectedRoom">
        <option selected value="All Rooms">All Rooms</option>
        <option v-for="room in selectedBuilding.room" :key="room" :value="room">
            {{ room }}
        </option>
      </select>
      <table>
        <tr>
            <th v-for="header in globalHeaders" v-bind:key="header"> {{ header }} </th>
            <th v-for="header in specificHeaders" v-bind:key="header"> {{ header }} </th>
        </tr>
      </table>
  </div>
</template>

<script>
export default {
  props: {
    taskType: String
  },
  data () {
    return {
      globalHeaders: [],
      dynamicHeaders: []
    }
  },
  methods: {
    getGlobalHeaders: function () {
      // api call to get global headers
      this.globalHeaders = ['Building', 'Room', 'Date Assigned', 'Operator']
    },
    getDynamicHeaders: function (TaskType) {
      if (TaskType === 'A') {
        this.dynamicHeaders = ['Task Attribute 5', 'Task Attribute 6']
      } else if (TaskType === 'B') {
        this.dynamicHeaders = ['Task Attribute 1', 'Task Attribute 2']
      } else if (TaskType === 'C') {
        this.dynamicHeaders = ['Task Attribute 3', 'Task Attribute 4']
      } else {
        this.dynamicHeaders = ['Task Type', 'View Details']
      }
    }
  },
  watch: {
    taskType: function () {
      this.getDynamicHeaders(this.taskType)
    }
  },
  beforeMount () {
    this.getGlobalHeaders(this.taskType)
    this.getDynamicHeaders(this.taskType)
  }
}
</script>

