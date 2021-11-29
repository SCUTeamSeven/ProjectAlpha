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
        <tr v-for="building in buildings" :key="building.name">
          <td><input type='checkbox' v-model="selectedBuildings" :value="building.name"></td>
          <td><a @click="$emit('buildingSelected', building.name)"> {{building.name}} </a></td>
          <td> {{building.rooms.length}} Rooms </td>
          <td> 0 Tasks </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BuildingsTable',
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
        for (var i = 0; i < this.buildings.length; i++) {
          this.selectedBuildings.push(this.buildings[i].name)
        }
      } else {
        // otherwise, remove everything from selected array
        this.selectedBuildings = []
      }
    }
  }
}
</script>

 <style lang="scss">
 .outerOuter {
   display:flex;
   justify-content:center;
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
 </style>
