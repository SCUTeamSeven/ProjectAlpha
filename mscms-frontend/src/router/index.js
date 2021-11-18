import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
// import Employees from '../views/Employees.vue'
import aTasks from '../views/aTasks.vue'
import Buildings from '../views/Buildings.vue'
import uTasks from '../views/uTasks.vue'
import ActiveBuilding from '../views/ActiveBuilding.vue'
import User from '../views/User.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/employees',
    name: 'Employees',
    component: Home
  },
  {
    path: '/employees/:id',
    name: 'Employee',
    component: User
  },
  {
    path: '/atasks',
    name: 'aTasks',
    component: aTasks
  },
  {
    path: '/buildings',
    name: 'Buildings',
    component: Buildings
  },
  {
    path: '/buildings/:building',
    name: 'Building',
    component: ActiveBuilding
  },
  {
    path: '/utasks',
    name: 'uTasks',
    component: uTasks
  }
]

const router = createRouter({
  mode: 'history',
  history: createWebHistory(process.env.BASE_URL),
  hash: false,
  routes
})

export default router
