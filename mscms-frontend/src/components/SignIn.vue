<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <GoogleSignin></GoogleSignin>
  </div>
</template>

<script>
// @ is an alias to /src
import GoogleSignin from '@/components/GoogleSignin.vue'

export default {
  name: 'SignIn',
  props: {
    msg: String
  },
  components: {
    GoogleSignin
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
