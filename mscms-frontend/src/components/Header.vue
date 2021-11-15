<template>
  <div class="top-bar">
  <img src="../assets/sculogo.png" class="logo-image" />
  <Menu :signedUser="user" @c="sendPage"/>
  <GoogleSignIn  class="signin-container" v-show="firstSignIn" @googleAuth="onAuth"/>
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
      user: {},
      firstSignIn: false
    }
  },
  watch: {
    user: function () {
      this.firstSignIn = true
      this.$emit('headerAuth', this.user)
    }
  },
  methods: {
    onAuth (e) {
      this.user = e
      this.$emit('headerAuth', this.user)
      // this.ready = !(Object.keys(this.user).length === 0)
    },
    sendPage (e) {
      this.$emit('currentPage', e)
    }
  }
}
</script>

<style lang='scss'>

.header {
  display: flex;
  flex-direction:column;
}
.top-bar{
  height:60px;
  display:flex;
  align-items: center;
  justify-content: space-between;
  background-color: #b30738;
  padding:0 10px;
  box-shadow: 0px 2px 9px 0px rgba(0,0,0,0.4);
}
.signin-container{
  height:100%;
  display:flex;
  align-items: center;
}
.signin-container button {
  height:60%;
  background-color:white;
  border-radius:5px;
  margin:0 10px;
  color:black;
  border:none;
  font-size:18px;
  transition:all .2s;
  padding:0 10px;
  cursor:pointer;
  border: 1px solid white;
}
.signin-container button:hover {
  box-shadow: 0px 1px 4px 0px rgba(0,0,0,0.5);
  background-color:#b30738;
  color: white;
  border:1px solid white;
}

.logo-image {
  width: 50px;
}
</style>
