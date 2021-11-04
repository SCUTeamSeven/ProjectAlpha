<template>
  <div class="home">
    <img alt="Vue logo" width="150" src="https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/Santa_Clara_U_Seal.svg/1200px-Santa_Clara_U_Seal.svg.png">
    <SignIn msg="SCU Media Services CMS"/>
  </div>
</template>

<script>
// @ is an alias to /src
import SignIn from '@/components/SignIn.vue'

export default {
  name: 'Home',
  components: {
    SignIn
  }
}
</script>
