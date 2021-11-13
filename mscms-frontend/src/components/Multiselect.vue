<template>
  <div>
<VueMultiselect
 v-model="value"
 :options="options"
 :multiple="true"
 group-values="libs"
 group-label="language"
 :group-select="true"
 placeholder="Type to search"
 track-by="name"
 label="name"
 :close-on-select="false"
 @select="dispatchAction"
 :allow-empty="false"
 :show-labels="false"
/>

  </div>
</template>

<script>
import VueMultiselect from 'vue-multiselect'
export default {
  components: { VueMultiselect },
  data () {
    return {
      value: [],
      options: [
        {
          language: 'Javascript',
          libs: [
            { name: 'Vue.js', category: 'Front-end' },
            { name: 'Adonis', category: 'Backend' }
          ]
        },
        {
          language: 'Ruby',
          libs: [
            { name: 'Rails', category: 'Backend' },
            { name: 'Sinatra', category: 'Backend' }
          ]
        },
        {
          language: 'Other',
          libs: [
            { name: 'Laravel', category: 'Backend' },
            { name: 'Phoenix', category: 'Backend' }
          ]
        }
      ]
    }
  },
  methods: {
    dispatchAction (actionName) {
      console.log(actionName)
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.css"></style>

<style scoped>
.multiselect__option--group {
background: #ededed;
color: #35495e;
}
.multiselect__option--group-selected.multiselect__option--highlight {
background: #ff6a6a;
color: #fff;
}
.multiselect__option {
display: block;
padding: 12px;
min-height: 40px;
line-height: 16px;
text-decoration: none;
text-transform: none;
position: relative;
cursor: pointer;
white-space: nowrap;
}
.multiselect__option--highlight {
background: #41b883;
outline: none;
color: #fff;
}
.multiselect__option--selected {
background: #f3f3f3;
color: #35495e;
font-weight: 700;
}
</style>
