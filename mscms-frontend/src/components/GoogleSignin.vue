<template>
  <div>
    <button @click="handleClickSignIn" v-show="!Vue3GoogleOauth.isAuthorized">
      <span class="login-text">Sign in with </span><img class="glogo" alt="Google logo" src="../assets/glogo.png">
    </button>

    <button @click="handleClickSignOut" v-show="Vue3GoogleOauth.isAuthorized" >
      Sign Out
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

        // Check if admin
        if (this.user.email === 'jjimenez2@scu.edu' || this.user.email === 'csarkissian@scu.edu') {
          this.user.isAdmin = true
          this.user.authToken = idToken
        } else {
          this.user.authToken = idToken
        }
      } catch (error) {
        // on fail do something
        console.error(error)
        return null
      }
    },
    async handleClickGetAuthCode () {
      try {
        const authCode = await this.$gAuth.getAuthCode()
        console.log('authCode', authCode)
      } catch (error) {
        // on fail do something
        console.error(error)
        return null
      }
    },
    async handleClickSignOut () {
      try {
        await this.$gAuth.signOut()
        console.log('isAuthorized', this.Vue3GoogleOauth.isAuthorized)
        this.user = {}
      } catch (error) {
        console.error(error)
      }
    },
    handleClickDisconnect () {
      window.location.href = `https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=${window.location.href}`
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
button:disabled {
  background: #fff;
  color: #ddd;
  cursor: not-allowed;
}
.glogo {
  width: 17px;
  padding-left: 4px;
}

.login-text {
  font-size: 150%;
  padding: 4px;
}
</style>
