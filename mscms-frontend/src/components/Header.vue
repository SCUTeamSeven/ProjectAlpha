<template>
<div>
  <div class="top-bar">
    <img src="../assets/sculogo.png" class="logo-image" />
    <Menu :signedUser="user" @c="sendPage"/>
    <div style='height:100%' v-show="firstSignIn">
      <button class = 'user-button'> Hello, {{ user.givenName }}</button>
      <GoogleSignIn class="signin-container" v-if="firstSignIn"/>
    </div>
  </div>
  <Welcome v-if="!firstSignIn" @welcomeAuth="onAuth"></Welcome>
</div>
</template>

<script>
// @ is an alias to /src
import GoogleSignIn from '@/components/GoogleSignIn.vue'
import Menu from '@/components/Menu.vue'
import Welcome from '@/components/Welcome.vue'

export default {
  name: 'Header',
  components: {
    GoogleSignIn,
    Menu,
    Welcome
  },
  data () {
    return {
      user: {},
      firstSignIn: false
    }
  },
  methods: {
    onAuth (e) {
      this.firstSignIn = true
      this.user = e
      this.$emit('headerAuth', this.user)
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
.signin-container button {
  height:0;
  width:100%;
  padding:0;
  margin:0;
  background-color:#b30738;
  color: white;
  border:none;
  font-size:18px;
  transition:all .2s;
  cursor:pointer;
  border-top: 1px solid #e6ebee;
  box-shadow: 0px 2px 6px 0px rgba(148, 116, 116, 0.2);
  border-radius: 0 0 5px 5px;
}
.signin-container button:hover {
  background-color:white;
  color:black;
}
.user-button, .menu button {
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

.user-button:hover, .menu button:hover{
  box-shadow: 0px 1px 4px 0px rgba(0,0,0,0.5);
  background-color:white;
  color: black;
}

.user-button:hover + .signin-container button, .signin-container button:hover{
  height: 41px !important;
  padding:0 !important;
  border-top: 1px solid #e6ebee;
}
.logo-image {
  width: 50px;
}
</style>
