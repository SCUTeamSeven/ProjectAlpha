<template>
  <div class="menu">
      <p>
          <button @click="$emit('c', 'Tasks')" v-if="user.isAdmin">Tasks</button>
          <button @click="$emit('c', 'Buildings')" v-if="user.isAdmin">Buildings</button>
          <button @click="$emit('c', 'Employees')" v-if="user.isAdmin">Employees</button>
      </p>
  </div>
</template>

<script>

export default {
  name: 'Menu',
  components: {
  },
  props: {
    signedUser: Object
  },
  data () {
    return {
      user: {},
      isAuthed: false
    }
  },
  watch: {
    signedUser: function () {
      this.user = this.signedUser
      this.isAuthed = true
    }
  },
  methods: {
  }
}
</script>

<style>
</style>
