<template>
  <div class="buildings">
    <div v-if="!ready">
      <h1>View/Edit Buildings</h1>
      <BuildingsTable :buildings="buildings" @buildingSelected="buildingSelected" @updateBuildings="updateBuildings" @deleteTasks="deleteTasks" :taskNumbers="taskNumbers"/>
    </div>
    <ActiveBuilding v-if="ready" :buildings="buildings" :currentBuilding="activeBuilding" :roomNumbers="roomNumbers" @addNewRoom="addNewRoom" @removeRooms="removeRooms" @r="buildingSelected({name: '', rooms: []})"/>
  </div>
</template>

<script>
import BuildingsTable from '@/components/BuildingsTable.vue'
import ActiveBuilding from '@/views/ActiveBuilding.vue'

export default {
  name: 'Buildings',
  components: {
    BuildingsTable,
    ActiveBuilding
  },
  props: {
    buildings: Object,
    tasks: Object
  },
  data () {
    return {
      activeBuilding: { name: '', rooms: [] },
      roomNumbers: [],
      ready: false,
      taskNumbers: []
    }
  },
  methods: {
    buildingSelected (e) {
      if (e.name === '') {
        this.activeBuilding = e
        this.ready = false
      } else {
        this.activeBuilding = this.buildings.find(({ name }) => name === e)
      }
    },
    updateBuildings (e) {
      this.$emit('updateBuildings', e)
    },
    addNewRoom () {
      this.$emit('updateBuildings', this.buildings)
    },
    removeRooms (e) {
      this.$emit('removeRooms', e)
    },
    deleteTasks (e) {
      this.$emit('deleteTasks', e)
    },
    updateRoomNumbers () {
      var d
      this.roomNumbers = []
      for (var i in this.buildings) {
        if (this.activeBuilding === this.buildings[i]) {
          for (d in this.buildings[i].rooms) {
            this.roomNumbers.push([])
          }
          for (d in this.taskNumbers[i]) {
            for (var k in this.buildings[i].rooms) {
              if (this.taskNumbers[i][d].room === this.buildings[i].rooms[k]) {
                this.roomNumbers[k].push(this.taskNumbers[i][d])
              }
            }
          }
        }
      }
    },
    updateTaskNumbers () {
      var buildingTaskNumbers = []
      var i
      for (i in this.buildings) {
        buildingTaskNumbers.push([])
      }
      for (i in this.tasks) {
        for (var j in this.buildings) {
          if (this.tasks[i].building === this.buildings[j].name) {
            buildingTaskNumbers[j].push(this.tasks[i])
          }
        }
      }
      this.taskNumbers = buildingTaskNumbers
    }
  },
  watch: {
    activeBuilding () {
      if (this.activeBuilding.name !== '') {
        this.updateRoomNumbers()
        this.ready = true
      }
    }
  },
  created () {
    var buildingTaskNumbers = []
    var i
    for (i in this.buildings) {
      buildingTaskNumbers.push([])
    }
    for (i in this.tasks) {
      for (var j in this.buildings) {
        if (this.tasks[i].building === this.buildings[j].name) {
          buildingTaskNumbers[j].push(this.tasks[i])
        }
      }
    }
    this.taskNumbers = buildingTaskNumbers
  }
}
</script>
