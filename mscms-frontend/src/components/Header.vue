<template>
  <div class="header">
    <img src="../assets/sculogo.png" class="logo-image" />
    <Menu :signedUser="user" @c="sendPage"></Menu>
    <GoogleSignIn class="sign-in-component" @gAuth="onAuth"></GoogleSignIn>
  </div>
</template>

<script>
// @ is an alias to /src
import GoogleSignIn from '@/components/GoogleSignIn.vue'
import Menu from '@/components/Menu.vue'

export default {
  name: 'Header',
  components: {
    GoogleSignIn,
    Menu
  },
  data () {
    return {
      user: {}
    }
  },
  watch: {
    user: function () {
      this.$emit('gAuth', this.user)
    }
  },
  methods: {
    onAuth (e) {
      this.user = e
    },
    sendPage (e) {
      this.$emit('currentPage', e)
    }
  }
}
</script>

<style>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.sign-in-component {
  margin-left: auto;
}
.logo-image {
  width: 5%;
}
</style>
