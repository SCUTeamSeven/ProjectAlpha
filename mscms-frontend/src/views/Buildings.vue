<template>
  <div class="buildings">
    <h1>Buildings</h1>
  </div>
</template>

<script>
export default {
  name: 'Buildings',
  components: {
  },
  data () {
    return {
      title: 'View/Edit Buildings'
    }
  },
  created () {
    this.$emit('t', this.title)
  }
}
</script>
