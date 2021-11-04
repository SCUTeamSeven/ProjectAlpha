import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Employees from '../views/Employees.vue'
import aTasks from '../views/aTasks.vue'
import Buildings from '../views/Buildings.vue'
import uTasks from '../views/uTasks.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/employees',
    name: 'Employees',
    component: Employees
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
