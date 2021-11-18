<template>
  <div class="buildingTable">
    <table>
      <tr>
        <th><input type='checkbox' v-model="allChecked" @change="selectAllBuildings"></th>
        <th>Building</th>
        <th>Rooms</th>
        <th>Tasks</th>
      </tr>
      <tr v-for="building in buildings" :key="building.name">
        <td><input type='checkbox' v-model="selectedBuildings" :value="building.name"></td>
        <td><span> {{building.name}} </span></td>
        <td> {{building.rooms.length}} Rooms </td>
        <td> 0 Tasks </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'BuildingTable',
  components: {
  },
  props: {
    buildings: Object
  },
  data () {
    return {
      allChecked: false,
      selectedBuildings: []
    }
  },
  watch: {
    selectedBuildings () {
      if (this.selectedBuildings.length === this.buildings.length) {
        this.allChecked = true
      } else {
        this.allChecked = false
      }
    }
  },
  methods: {
    selectAllBuildings () {
      if (this.allChecked) {
        this.selectedBuildings = []
        for (var i = 0; i < this.buildings.length; i++) {
          this.selectedBuildings.push(this.buildings[i].name)
        }
      } else {
        this.selectedBuildings = []
      }
    }
  }
}
</script>
