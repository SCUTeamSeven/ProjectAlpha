<template>
  <div class="main-view">
    <Header @headerAuth="onAuth" @currentPage="updatePage"></Header>
    <aTasks v-if="currentPage === 'Tasks' && isAdmin"></aTasks>
    <Buildings v-if="currentPage === 'Buildings' && isAdmin"></Buildings>
    <Employees v-if="currentPage === 'Employees' && isAdmin"></Employees>
    <div v-if="currentPage === 'Home' && isAuthed">
      <h1> Search Tasks </h1>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import aTasks from '@/views/aTasks.vue'
import Buildings from '@/views/Buildings.vue'
import Employees from '@/views/Employees.vue'

export default {
  name: 'Home',
  components: {
    Header,
    aTasks,
    Buildings,
    Employees
  },
  data () {
    return {
      user: {},
      isAuthed: false,
      isAdmin: false,
      currentPage: 'Home'
    }
  },
  methods: {
    onAuth (e) {
      if (e) {
        this.user = e
        this.isAuthed = true
        this.isAdmin = this.user.isAdmin
      } else {
        this.isAuthed = false
        alert('User has not been authenticated.')
      }
    },
    updatePage (e) {
      this.currentPage = e
    }
  }
}
</script>

<style>
 h1 {
   padding:30px 20px;
   font-size: 3em;
   margin: 0;
   background-color:#e6ebee;
 }
</style>
