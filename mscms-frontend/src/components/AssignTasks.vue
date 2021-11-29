<template>
  <div class = 'tasksOuter'>
    <h2>Assign Tasks to Rooms</h2>
    <div v-if="assigned" class='message'>Task<span v-if="number!==1">s</span> successfully assigned to {{number}} room<span v-if="number!==1">s</span>!</div>
    <div class = 'assignTasks'>
      <p>Assign </p>
      <select v-model="selectedType">
        <option value ='' disabled>Select Task Type</option>
        <option v-for="type in taskTypes" :key="type.name" :value="type">{{ type.name }}
        </option>
      </select>
      <p>to: </p>
      <VueMultiselect
      v-model="value"
      :options="options"
      :multiple="true"
      group-values="rooms"
      group-label="name"
      :group-select="true"
      placeholder="Select rooms"
      track-by="rname"
      label="rname"
      :close-on-select="false"
      :show-labels="false"
      />
      <button @click="assignTasks">Assign Tasks</button>
    </div>
  </div>
</template>

<script>
import VueMultiselect from 'vue-multiselect'
export default {
  components: { VueMultiselect },
  props: { buildings: Object, taskTypes: Object },
  data () {
    return {
      value: [],
      selectedType: '',
      options: [],
      assigned: false,
      number: 0
    }
  },
  methods: {
    assignTasks () {
      this.assigned = true
      this.number = this.value.length
      this.value = []
      console.log(this.options)
    }
  },
  created () {
    var x = []
    for (var i in this.buildings) {
      var y = { name: this.buildings[i].name, rooms: [] }
      for (var j in this.buildings[i].rooms) {
        y.rooms.push({ rname: this.buildings[i].name + ' - ' + this.buildings[i].rooms[j], room: this.buildings[i].rooms[j], building: this.buildings[i].name })
      }
      x.push(y)
    }
    this.options = x
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style>
.tasksOuter {
    margin:40px;
  padding: 0 40px;
  width: calc(100% -  160px);
}
.tasksOuter h2 {
  font-size: 30px;
}
.assignTasks {
  margin-top:30px;
  display:flex;
  align-items: center;
  justify-content: space-between;

}
.multiselect {
  width:600px;
  margin-right:50px;
}
.assignTasks select {
  width:200px;
  border: 1px solid #cbcbcb;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}
.assignTasks p {
  font-size: 20px;
  margin: 0
}
.multiselect__tags {
  max-height:200px;
  overflow: scroll;
}
.multiselect__option--group, .multiselect__option--group-selected.multiselect__option--highlight {
  background: #ededed;
  color: #35495e;
}
.multiselect__option--group-selected {
  background: #35495e;
  outline: none;
  color: #fff;
}

.multiselect__option--group-selected.multiselect__option--highlight {
  background: #35495e;
  color: #fff;
}

.multiselect__option--highlight, .multiselect__option--selected.multiselect__option--highlight {
  background: #b30738;
  color: #fff;
}
.multiselect__option--selected {
  background: #f3f3f3;
  color: #35495e;
  font-weight: 700;
}
.multiselect__tag {
  background: #b30738;
}
.multiselect__tag-icon:after {
  color: white;
}
.assignTasks button {
  padding: 15px 20px;
  border: 1px solid #cbcbcb;
  color: #7c7c7c;
  background-color: white;
  border-radius: 5px;
  font-size: 14px;
  transition:.2s;
  cursor: pointer;
}

.assignTasks button:hover {
  color:black;
  border: 1px solid black;
}
</style>
