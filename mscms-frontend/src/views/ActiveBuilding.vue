<template>
  <div class="activeBuilding">
    <h1>{{currentBuilding.name}}<button @click="backToBuildings()">Back to Buildings</button></h1>
    <RoomsTable :rooms="rooms" @roomSelected="roomSelected"/>
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
    currentBuilding: Object
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
      console.log(this.activeRoom)
    }
  }
}
</script>
