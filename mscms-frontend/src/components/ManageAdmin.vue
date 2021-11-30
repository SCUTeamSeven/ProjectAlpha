<template>
  <div class="admins">
    <h3 class="admin-header">Manage Admins</h3>
    <table>
      <tr v-for="admin in admins" v-bind:key="admin">
        <td> <input v-model="checkedAdmins" style="text-align: left;" type="checkbox" /> {{ admin }} </td>
      </tr>
    </table>
    <div class="button-group-admins">
      <input v-model="adminInp"/>
      <button @click="admins.push(adminInp)">Add admin</button>
      <button>Delete selected admins</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ManageAdmins',
  components: {
  },
  props: ['inputAdmins'],
  data () {
    return {
      checkedAdmins: [],
      selectedAdmins: [],
      adminInp: '',
      admins: this.inputAdmins
    }
  },
  methods: {

  },
  watch: {
    checkedAdmins: function () {
      for (var i = 0; i < this.admins.length; i++) {
        if (this.checkedAdmins[i] === true) {
          this.selectedAdmins[this.selectedAdmins.length + 1] = this.admins[i]
          console.log(this.selectedAdmins)
        }
      }
    }
  }
}
</script>

<style>
.admin-header {
    text-align: center;
}
.admins {
    flex-basis:49%;
    margin: auto;
    height: 100%;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: auto;
}

td, th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}

.button-group-admins {
  text-align: center;
  padding: 2%;
}
</style>
