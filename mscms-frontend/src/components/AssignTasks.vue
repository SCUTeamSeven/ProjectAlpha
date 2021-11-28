<template>
  <div>
    <VueMultiselect
    v-model="value"
    :options="options"
    :multiple="true"
    group-values="rooms"
    group-label="name"
    :group-select="true"
    placeholder="Type to search"
    track-by="name"
    label="name"
    :close-on-select="false"
    @select="dispatchAction"
    :show-labels="false"
    />
  </div>
</template>

<script>
import VueMultiselect from 'vue-multiselect'
export default {
  components: { VueMultiselect },
  props: { buildings: Object },
  data () {
    return {
      value: []
    }
  },
  computed: {
    options () {
      var x = []
      for (var i in this.buildings) {
        var y = { name: this.buildings[i].name, rooms: [] }
        for (var j in this.buildings[i].rooms) {
          y.rooms.push({ name: this.buildings[i].name + ' - ' + this.buildings[i].rooms[j], room: this.buildings[i].rooms[j], building: this.buildings[i].name })
        }
        x.push(y)
      }
      return x
    }
  },
  methods: {
    dispatchAction (actionName) {
      console.log(actionName)
    }
  },
  updated () {
    console.log(this.value)
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style scoped>
.multiselect__option--group {
background: #ededed;
color: #35495e;
}
.multiselect__option--group-selected.multiselect__option--highlight {
background: #ff6a6a;
color: #fff;
}
.multiselect__option {
display: block;
padding: 12px;
min-height: 40px;
line-height: 16px;
text-decoration: none;
text-transform: none;
position: relative;
cursor: pointer;
white-space: nowrap;
}
.multiselect__option--highlight {
background: #41b883;
outline: none;
color: #fff;
}
.multiselect__option--selected {
background: #f3f3f3;
color: #35495e;
font-weight: 700;
}
</style>
