<template>
  <div class="buildings">
    <h1>View/Edit Buildings</h1>
    <table>
      <tr>
        <th><input type='checkbox' v-model="allChecked"></th>
        <th>Building</th>
        <th>Rooms</th>
        <th>Tasks</th>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Buildings',
  components: {
  },
  data () {
    return {
      allChecked: false
    }
  }
}
</script>
