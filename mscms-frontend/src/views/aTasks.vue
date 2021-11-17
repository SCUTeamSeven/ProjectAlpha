<template>
  <div class="tasks">
    <h1>Create/Assign Tasks</h1>
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
    }
  }
}
</script>
