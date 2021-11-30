<template>
  <div class="tasks">
    <h1>Create/Assign Tasks</h1>
    <TaskTypeCreator :taskTypes="taskTypes" @updateTaskTypes="updateTaskTypes"/>
    <AssignTasks :taskTypes="taskTypes" :buildings="buildings" @updateBuildings="updateBuildings" @assignTasks="assignTasks"/>
  </div>
</template>

<script>
import AssignTasks from '../components/AssignTasks.vue'
import TaskTypeCreator from '../components/TaskTypeCreator.vue'
export default {
  name: 'aTasks',
  props: {
    taskTypes: Object,
    buildings: Object
  },
  components: {
    TaskTypeCreator,
    AssignTasks
  },
  data () {
    return {
    }
  },
  methods: {
    updateTaskTypes (e) {
      this.$emit('updateTaskTypes', e)
    },
    updateBuildings (e) {
      this.$emit('updateBuildings', e)
    },
    assignTasks (e) {
      this.$emit('assignTasks', e)
    }
  }
}
</script>
