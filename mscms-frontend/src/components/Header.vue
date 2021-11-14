<template>
  <div class="header">
    <div class="top-bar">
    <img src="../assets/sculogo.png" class="logo-image" />
    <GoogleSignIn class="sign-in-component" @gAuth="onAuth"/>
    </div>
    <div class="title-bar">
      <h1 v-if="ready"> {{currentTitle}} </h1>
      <button v-if="(user.isAdmin) && (currentPage !== 'Home')" @click="sendPage('Home')">Back to Home</button>
    </div>
    <Menu v-if="currentPage === 'Home'" :signedUser="user" @c="sendPage"/>
  </div>
</template>

<script>
// @ is an alias to /src
import GoogleSignIn from '@/components/GoogleSignIn.vue'
import Menu from '@/components/Menu.vue'

export default {
  name: 'Header',
  props: {
    inputTitle: String
  },
  components: {
    GoogleSignIn,
    Menu
  },
  data () {
    return {
      user: {},
      currentPage: 'Home',
      currentTitle: '',
      ready: false
    }
  },
  watch: {
    user: function () {
      this.currentTitle = 'Welcome, ' + this.user.givenName
      this.$emit('gAuth', this.user)
    },
    inputTitle: function () {
      this.currentTitle = this.inputTitle
    }
  },
  methods: {
    onAuth (e) {
      this.user = e
      this.ready = !(Object.keys(this.user).length === 0)
    },
    sendPage (e) {
      this.currentPage = e
      if (e === 'Home') {
        this.currentTitle = 'Welcome, ' + this.user.givenName
      }
      this.$emit('currentPage', e)
    }
  }
}
</script>

<style lang='scss'>
$primary-color: #b30738;
.header {
  display: flex;
  flex-direction:column;
}
.top-bar{
  display:flex;
  align-items: center;
  justify-content: center;
  padding:10px;
  background-color: $primary-color;
  box-shadow: 0px 2px 9px 0px rgba(0,0,0,0.4);
}
.title-bar{
  display: flex;
  align-items: center;
  padding:0 20px;
}
.sign-in-component {
  margin-left: auto;
}
.logo-image {
  width: 5%;
}
</style>
