<template>
  <div class="buildings">
    <div v-if="activeBuilding===null">
      <h1>View/Edit Buildings</h1>
      <BuildingsTable :buildings="buildings" @buildingSelected="buildingSelected"/>
    </div>
    <ActiveBuilding v-if="activeBuilding!==null" :currentBuilding="activeBuilding" @r="buildingSelected(null)"/>
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
    buildings: Object
  },
  data () {
    return {
      activeBuilding: null
    }
  },
  methods: {
    buildingSelected (e) {
      if (e === null) {
        this.activeBuilding = null
      } else {
        this.activeBuilding = this.buildings.find(({ name }) => name === e)
      }
    }
  }
}
</script>
