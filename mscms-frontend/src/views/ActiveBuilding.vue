<template>
  <div class="activeBuilding">
    <h1>{{currentBuilding.name}}<button @click="backToBuildings()">Back to Buildings</button></h1>
    <RoomsTable :rooms="rooms" :roomNumbers="roomNumbers" @roomSelected="roomSelected" @addNewRoom="addNewRoom" @removeRooms="removeRooms"/>
  </div>
</template>

<script>
import RoomsTable from '@/components/RoomsTable.vue'

export default {
  name: 'Rooms',
  components: {
    RoomsTable
  },
  props: {
    currentBuilding: Object,
    roomNumbers: Object,
    buildings: Object
  },
  data () {
    return {
      activeRoom: null
    }
  },
  computed: {
    rooms () {
      return this.currentBuilding.rooms
    }
  },
  methods: {
    backToBuildings () {
      this.$emit('r')
    },
    roomSelected (e) {
      if (e === null) {
        this.activeRoom = null
      } else {
        this.activeRoom = e
      }
    },
    addNewRoom () {
      this.$emit('addNewRoom')
    },
    removeRooms (e) {
      this.$emit('removeRooms', [this.currentBuilding, e])
    }
  }
}
</script>
