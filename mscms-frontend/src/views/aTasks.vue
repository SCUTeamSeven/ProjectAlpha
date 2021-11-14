<template>
  <div class="tasks">
    <task-type-creator/>
    <multiselect/>
  </div>
</template>

<script>
import Multiselect from '../components/Multiselect.vue'
import TaskTypeCreator from '../components/TaskTypeCreator.vue'
export default {
  name: 'aTasks',
  components: {
    TaskTypeCreator,
    Multiselect
  },
  data () {
    return {
      title: 'Create/Assign Tasks'
    }
  },
  created () {
    this.$emit('t', this.title)
  }
}
</script>
