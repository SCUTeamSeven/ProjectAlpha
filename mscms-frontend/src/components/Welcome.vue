<template>
  <div class = 'container'>
    <h1 class="welcome-message">Welcome to MSCMS, please sign in to proceed.</h1>
    <GoogleSignIn class ='home-signin' @googleAuth="welcomeAuth"/>
  </div>
</template>

<script>
import GoogleSignIn from '@/components/GoogleSignIn.vue'

export default {
  name: 'Welcomee',
  components: {
    GoogleSignIn
  },
  data () {
    return {
    }
  },
  watch: {
  },
  methods: {
    welcomeAuth (e) {
      this.$emit('welcomeAuth', e)
    }
  }
}
</script>

<style>
.container {
  display:flex;
  flex-direction: column;
  align-items: stretch;
  text-align: center;
}
.home-signin {
  margin: auto;
}
.home-signin button{
  margin:50px 0;
  padding:15px 60px;
  font-size:25px;
  border:1px solid gray;
  border-radius:10px;
  background-color: #b30738;
  color:white;
  cursor: pointer;
  transition: all .2s;
}
.home-signin button:hover {
  background-color: white;
  color:black;
}
</style>
