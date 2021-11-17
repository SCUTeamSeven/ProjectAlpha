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
import { useCookies } from 'vue3-cookies'
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
        const googleUser = await this.$gAuth.signIn()

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
        this.cookies.set('user', this.user)
        this.$emit('googleAuth', this.user)
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
        this.cookies.set('user', this.user)
      } catch (error) {
        console.error(error)
      }
      // Reload the page
      this.$router.go()
    }
  },
  setup (props) {
    const { isSignIn } = toRefs(props)
    const Vue3GoogleOauth = inject('Vue3GoogleOauth')
    const handleClickLogin = () => {}
    const { cookies } = useCookies()
    return {
      Vue3GoogleOauth,
      handleClickLogin,
      isSignIn,
      cookies
    }
  },
  beforeMount () {
    var userCookie = this.cookies.get('user')
    if (Object.keys(userCookie).length !== 0) {
      this.user = userCookie
      this.$emit('googleAuth', this.user)
    }
  }
}
</script>

<style>
</style>
