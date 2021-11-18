<template>
  <div class="menu">
    <button @click="$emit('c', 'Home')" v-if="user.isAdmin">Search Tasks</button>
    <button @click="$emit('c', 'Buildings')" v-if="user.isAdmin">View/Edit Buildings</button>
    <button @click="$emit('c', 'Tasks')" v-if="user.isAdmin">Create/Assign Tasks</button>
    <button @click="$emit('c', 'Employees')" v-if="user.isAdmin">Manage Users</button>
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
  }
}
</script>

<style>
.menu{
  display:flex;
  justify-content: space-evenly;
  height:100%;
}
</style>
