<template>
  <div class="buildings">
    <h1>View/Edit Buildings</h1>
    <BuildingTable :buildings="buildings"></BuildingTable>
  </div>
</template>

<script>
import BuildingTable from '@/components/BuildingTable.vue'

export default {
  name: 'Buildings',
  components: {
    BuildingTable
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
      }
    }
  }
}
</script>
