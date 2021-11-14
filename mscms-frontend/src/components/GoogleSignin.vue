<template>
  <div>
    <button class="login-button" @click="handleClickSignIn" v-if="!Vue3GoogleOauth.isAuthorized">
      <span class="login-text">Sign in</span>
    </button>

    <button class="login-button" @click="handleClickSignOut" v-if="Vue3GoogleOauth.isAuthorized" >
      <span class="logout-text">Sign Out</span>
    </button>

  </div>
</template>

<script>
import { inject, toRefs } from 'vue'
export default {
  name: 'GoogleSignIn',
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
    async handleClickSignIn () {
      try {
        this.getGoogleProfile(await this.$gAuth.signIn())
      } catch (error) {
        // on fail do something
        console.error(error)
        return null
      }
    },
    async handleClickSignOut () {
      try {
        await this.$gAuth.signOut()
        this.user = {}
      } catch (error) {
        console.error(error)
      }

      // // Reload the page
      // this.$router.go()
    },
    getGoogleProfile (googleUser) {
      if (!googleUser) {
        return null
      }

      // User profile obtained by Google
      var profile = googleUser.getBasicProfile()

      // Clientside authenticated user information
      this.user = { email: profile.getEmail(), fullName: profile.getName(), ID: profile.getId(), givenName: profile.getGivenName(), imageURL: profile.getImageUrl(), isAdmin: false }

      // Authentication token for the flask web API server
      var idToken = googleUser.getAuthResponse().id_token

      // Authorize user
      if (this.user.email === 'jjimenez2@scu.edu' || this.user.email === 'csarkissian@scu.edu') {
        this.user.isAdmin = true
        this.user.authToken = idToken
      } else {
        this.user.authToken = idToken
      }
    }
  },
  setup (props) {
    const { isSignIn } = toRefs(props)
    const Vue3GoogleOauth = inject('Vue3GoogleOauth')
    const handleClickLogin = () => {}
    return {
      Vue3GoogleOauth,
      handleClickLogin,
      isSignIn
    }
  },
  updated () {
    this.getGoogleProfile(this.$gAuth.instance.currentUser.Vd)
  }
}
</script>

<style>
button {
  display: inline-block;
  line-height: 1;
  white-space: nowrap;
  cursor: pointer;
  background: #fff;
  border: 1px solid #dcdfe6;
  color: #606266;
  -webkit-appearance: none;
  text-align: center;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  outline: 0;
  margin: 0;
  -webkit-transition: 0.1s;
  transition: 0.1s;
  font-weight: 500;
  padding: 12px 20px;
  font-size: 14px;
  border-radius: 4px;
  margin-right: 1em;
}
.login-button {
  background-color: lightgreen;
}
.login-text {
  color: white;
}
.logout-button {
  background-color: lightgrey;
}
.logout-text {
  color: white;
}
</style>
