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
      // Reload the page
      this.$router.go()
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
      this.$emit('googleAuth', this.user)
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
  }
}
</script>

<style>
</style>
