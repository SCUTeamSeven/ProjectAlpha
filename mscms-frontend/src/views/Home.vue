<template>
  <div class="home">
    <GoogleSignIn @gAuth="onAuth"></GoogleSignIn>
  </div>
</template>

<script>
// @ is an alias to /src
import GoogleSignIn from '@/components/GoogleSignIn.vue'

export default {
  name: 'Home',
  components: {
    GoogleSignIn
  },
  data () {
    return {
      user: {}
    }
  },
  methods: {
    onAuth (e) {
      this.user = e
    }
  }
}
</script>
