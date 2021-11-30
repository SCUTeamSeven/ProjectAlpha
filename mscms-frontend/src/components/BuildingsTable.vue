<template>
  <div class="outerOuter">
    <div class="tableOuter">
      <table class="buildingTable">
        <tr>
          <th><input type='checkbox' v-model="allChecked" @change="selectAllBuildings"></th>
          <th>Building</th>
          <th>Rooms</th>
          <th>Tasks</th>
        </tr>
        <tr v-for="building in buildingsCopy" :key="building">
          <td><input type='checkbox' v-model="selectedBuildings" :value="building.name"></td>
          <td><a @click="$emit('buildingSelected', building.name)">{{building.name}}</a></td>
          <td>{{building.rooms.length}} Rooms</td>
          <td>{{numbers[findBuildingIndex(building)].length}} Task<span v-if="buildingsCopy.findIndex(x => x === building) !== 1">s</span></td>
        </tr>
        <tr v-if="addNewBuilding">
          <td></td>
          <td><input style="margin-left:30px;" v-model="newBuildingName" placeholder="New Building Name"></td>
          <td></td>
          <td></td>
        </tr>
      </table>
    </div>
    <div style='width:80%; padding:30px 0'>
      <button v-if="!addNewBuilding" @click="addNewBuilding = true">Add New Building</button>
      <button v-else @click="addNewBuilding = false">Cancel</button>
      <button v-if="addNewBuilding && newBuildingName !== ''" @click="saveNewBuilding">Save New Building</button></div>
  </div>
</template>

<script>
export default {
  name: 'BuildingsTable',
  components: {
  },
  props: {
    buildings: Object,
    taskNumbers: Array
  },
  data () {
    return {
      allChecked: false,
      selectedBuildings: [],
      newBuildingName: '',
      addNewBuilding: false,
      buildingsCopy: [],
      numbers: [],
      displayNumbers: []
    }
  },
  watch: {
    selectedBuildings () {
      // check if all the buildings are selected, if so mark allChecked
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
        // if allChecked, add all buildings to the selected array
        this.selectedBuildings = []
        for (var i = 0; i < this.buildingsCopy.length; i++) {
          this.selectedBuildings.push(this.buildingsCopy[i].name)
        }
      } else {
        // otherwise, remove everything from selected array
        this.selectedBuildings = []
      }
    },
    saveNewBuilding () {
      if (this.validateNewName(this.newBuildingName)) {
        this.buildingsCopy.push({ name: this.newBuildingName, rooms: [] })
        this.numbers.push([])
        this.addNewBuilding = false
        this.newBuildingName = ''
        this.$emit('updateBuildings', this.buildingsCopy)
      }
    },
    validateNewName: function (name) {
      var validated = 1
      for (var i in this.buildingsCopy) {
        if (name === this.buildingsCopy[i].name) {
          validated = 0
          alert('That building already exists.')
        }
      }
      return validated
    },
    findBuildingIndex (building) {
      var x = this.buildingsCopy.findIndex(x => x === building)
      if (x < 0) {
        return 0
      } else {
        return x
      }
    }
  },
  created () {
    for (var i in this.buildingsCopy) {
      this.numbers.push([])
    }
    for (i in this.buildings) {
      this.buildingsCopy.push(this.buildings[i])
    }
    for (i in this.buildingsCopy) {
      if (this.taskNumbers[i] === undefined) {
        this.numbers[i] = []
      } else {
        this.numbers[i] = this.taskNumbers[i]
      }
    }
  }
}
</script>

 <style lang="scss">
 .outerOuter {
   padding:40px 0;
   display:flex;
  flex-direction:column;
   justify-content:center;
   align-items: center;
 }
 //table container
 .tableOuter {
   width:80%;
   overflow: hidden;
   border-radius: 20px;
   border:1px solid gray;
 }
 //full table witdh
 .buildingTable{
   width:100%;
   border-collapse: collapse;
 }
 //styles for headers and cells
  .buildingTable th {
   background-color:#b8bbbd;
   border:solid gray;
   border-width: 0 1px 1px 1px;
   padding:20px;
   font-size:24px
 }
 .buildingTable td {
    text-align:center;
    padding:20px;
    border: 1px solid #c4c8cb;
    font-size:20px;
 }
  //make building column big
 .buildingTable th:nth-child(2), .buildingTable td:nth-child(2) {
   width: 65%;
   text-align: start;
 }
 //hide border for edge cells
 .buildingTable th:first-child, .buildingTable td:first-child{
   border-left:none;
 }
 .buildingTable th:last-child, .buildingTable td:last-child{
   border-right:none;
 }
  .buildingTable tr:last-child td{
   border-bottom:none;
 }
 //increase size of checkbox
  .buildingTable input {
   transform:scale(1.4)
 }
 // make building look clickable
  .buildingTable a {
    text-decoration: underline;
    cursor: pointer;
 }
 .buildingTable a:hover {
    color: #b30738;
 }
 .outerOuter button {
  padding: 15px 20px;
  border: 1px solid #cbcbcb;
  color: #7c7c7c;
  background-color: white;
  border-radius: 5px;
  font-size: 14px;
  transition:.2s;
  cursor: pointer;
}

.outerOuter button:hover {
  color:black;
  border: 1px solid black;
}
 </style>
