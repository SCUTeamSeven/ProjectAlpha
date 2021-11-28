<template>
  <div class="outerOuter">
    <div class="tableOuter">
      <table class="roomTable">
        <tr>
          <th><input type='checkbox' v-model="allChecked" @change="selectAllRooms"></th>
          <th>Room</th>
          <th>Tasks</th>
        </tr>
        <tr v-for="room in rooms" :key="room">
          <td><input type='checkbox' v-model="selectedRooms" :value="room.name"></td>
          <td><a @click="$emit('roomSelected', room)"> {{room}} </a></td>
          <td> 0 Tasks </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'roomsTable',
  components: {
  },
  props: {
    rooms: Object
  },
  data () {
    return {
      allChecked: false,
      selectedRooms: []
    }
  },
  watch: {
    selectedRooms () {
      // check if all the rooms are selected, if so mark allChecked
      if (this.selectedRooms.length === this.rooms.length) {
        this.allChecked = true
      } else {
        this.allChecked = false
      }
    }
  },
  methods: {
    selectAllRooms () {
      if (this.allChecked) {
        // if allChecked, add all rooms to the selected array
        this.selectedRooms = []
        for (var i = 0; i < this.rooms.length; i++) {
          this.selectedRooms.push(this.rooms[i].name)
        }
      } else {
        // otherwise, remove everything
        this.selectedRooms = []
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
 .roomTable{
   width:100%;
   border-collapse: collapse;
 }
 //styles for headers and cells
  .roomTable th {
   background-color:#b8bbbd;
   border:solid gray;
   border-width: 0 1px 1px 1px;
   padding:20px;
   font-size:24px
 }
 .roomTable td {
    text-align:center;
    padding:20px;
    border: 1px solid #c4c8cb;
    font-size:20px;
 }
  //make room column big
 .roomTable th:nth-child(2), .roomTable td:nth-child(2) {
   width: 65%;
   text-align: start;
 }
 //hide border for edge cells
 .roomTable th:first-child, .roomTable td:first-child{
   border-left:none;
 }
 .roomTable th:last-child, .roomTable td:last-child{
   border-right:none;
 }
  .roomTable tr:last-child td{
   border-bottom:none;
 }
 //increase size of checkbox
  .roomTable input {
   transform:scale(1.4)
 }
  // make room look clickable
  .roomTable a {
    text-decoration: underline;
    cursor: pointer;
 }
 .roomTable a:hover {
    color: #b30738;
 }
 </style>
