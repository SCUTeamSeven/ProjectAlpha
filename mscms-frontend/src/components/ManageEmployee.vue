<template>
  <div class="employees">
    <h3 class="employees-header">Manage Employees</h3>
    <table>
      <tr v-for="emp in employees" v-bind:key="emp">
        <td> <input v-model="checkedEmps" style="text-align: left;" type="checkbox" /> {{ emp }} </td>
      </tr>
    </table>
    <div class="button-group-emps">
      <input v-model="empInput"/>
      <button @click="employees.push(empInput)">Add employee</button>
      <button>Delete selected employees</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ManageEmployees',
  components: {
  },
  props: ['inputEmps'],
  data () {
    return {
      checkedEmps: [],
      selectedEmps: [],
      empInput: '',
      employees: this.inputEmps
    }
  },
  methods: {

  }
}
</script>

<style>
.employees-header {
    text-align: center;
}
.employees {
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
.button-group-emps {
  text-align: center;
  padding: 2%;
}
</style>
