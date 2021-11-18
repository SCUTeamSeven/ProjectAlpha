<template>
  <div>
    <h1>Manage Users</h1>

    <div class="manage-users">
      <ManageAdmin :inputAdmins='admins'/>
      <ManageEmployee :inputEmps='employees'/>
    </div>
  </div>
</template>

<script>
import ManageAdmin from '@/components/ManageAdmin.vue'
import ManageEmployee from '@/components/ManageEmployee.vue'

export default {
  name: 'Employees',
  components: {
    ManageAdmin,
    ManageEmployee
  },
  data () {
    return {
      admins: ['jjimenez2@scu.edu', 'travisscott@astroworld.com'],
      employees: ['jj@scu.edu', 'dd@scu.edu']
    }
  },
  methods: {

  }
}
</script>

<style>
.manage-users {
  display: flex;
  flex-wrap:wrap;
}

</style>
