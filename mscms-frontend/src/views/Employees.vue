<template>
  <div class="employees">
    <h1>Employees</h1>
  </div>
</template>

<script>
export default {
  name: 'Employees',
  components: {
  },
  data () {
    return {
      title: 'Manage Employees'
    }
  },
  created () {
    this.$emit('t', this.title)
  }
}
</script>
