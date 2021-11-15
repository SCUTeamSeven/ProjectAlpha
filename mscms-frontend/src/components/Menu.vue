<template>
  <div class="menu">
    <button @click="$emit('c', 'Home')" v-if="user.isAdmin">Home</button>
    <button @click="$emit('c', 'Buildings')" v-if="user.isAdmin">View/Edit Buildings</button>
    <button @click="$emit('c', 'Tasks')" v-if="user.isAdmin">Create/Assign Tasks</button>
    <button @click="$emit('c', 'Employees')" v-if="user.isAdmin">Manage Employees</button>
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
.menu button {
  height:100%;
  margin:0;
  background-color: transparent;
  border:none;
  color:white;
  font-size: 18px;
  padding:0 20px;
  transition: all .2s;
  cursor: pointer;
}

.menu button:hover {
  box-shadow: 0px 1px 4px 0px rgba(0,0,0,0.5);
  background-color:white;
  color: black;
}
</style>
