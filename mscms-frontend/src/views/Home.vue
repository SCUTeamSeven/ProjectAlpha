<template>
  <div class="main-view">
    <Header @gAuth="onAuth" @currentPage="updatePage" :inputTitle="currentTitle"></Header>
    <Welcome v-if="!isAuthed"></Welcome>
    <aTasks v-if="currentPage === 'Tasks'" @t="changeTitle"></aTasks>
    <Buildings v-if="currentPage === 'Buildings'" @t="changeTitle"></Buildings>
    <Employees v-if="currentPage === 'Employees'" @t="changeTitle"></Employees>
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
      currentPage: '',
      currentTitle: ''
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
    },
    changeTitle (t) {
      console.log(t)
      this.currentTitle = t
    }
  }
}
</script>
