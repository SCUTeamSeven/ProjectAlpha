<template>
  <div class="menu">
      <p>
          <a href="#" v-if="user.isAdmin"> Tasks  |</a>
          <a href="#" v-if="user.isAdmin"> Buildings |</a>
          <a href="#" v-if="user.isAdmin"> Employees </a>
      </p>
  </div>
</template>

<script>

export default {
  name: 'Menu',
  components: {
  },
  props: {
    signedUser: Object
  },
  data () {
    return {
      user: {},
      isAuthed: false
    }
  },
  watch: {
    signedUser: function () {
      this.user = this.signedUser
      this.isAuthed = true
    }
  },
  methods: {
  }
}
</script>

<style>
</style>
