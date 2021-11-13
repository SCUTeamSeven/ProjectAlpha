<template>
  <div class="main-view">
    <Header @gAuth="onAuth"></Header>
    <Welcome v-show="!isAuthed"></Welcome>
    <aTasks v-show="currentPage === 'Tasks'"></aTasks>
    <Buildings v-show="currentPage === 'Buildings'"></Buildings>
    <Employees v-show="currentPage === 'Employees'"></Employees>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import Welcome from '@/components/Welcome.vue'
import aTasks from '@/views/aTasks.vue'
import Buildings from '@/views/Buildings.vue'
import Employees from '@/views/Employees.vue'

export default {
  name: 'Home',
  components: {
    Header,
    Welcome,
    aTasks,
    Buildings,
    Employees
  },
  data () {
    return {
      user: {},
      isAuthed: false,
      isAdmin: false,
      currentPage: ''
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
    recurCurrentPage (e) {
      this.currentPage = e
      alert(e)
    }
  }
}
</script>
