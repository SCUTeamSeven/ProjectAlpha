import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import gAuth from 'vue3-google-oauth2'
const gAuthOptions = { clientId: '51950083564-a1pe4gencpmiqk22rb0osfci2f944f27.apps.googleusercontent.com', scope: 'profile email', prompt: 'consent', fetch_basic_profile: true }
createApp(App).use(gAuth, gAuthOptions).use(store).use(router).mount('#app')
