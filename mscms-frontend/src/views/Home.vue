<template>
  <div class="main-view">
    <Header @gAuth="onAuth"></Header>
    <Welcome v-show="!isAuthed"></Welcome>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import Welcome from '@/components/Welcome.vue'

export default {
  name: 'Home',
  components: {
    Header,
    Welcome
  },
  data () {
    return {
      user: {},
      isAuthed: false,
      isAdmin: false
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
    }
  }
}
</script>
