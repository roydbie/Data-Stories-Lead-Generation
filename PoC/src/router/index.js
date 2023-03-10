import { createRouter, createWebHistory } from 'vue-router'
import Start from '../views/Start.vue'
import Settings from '../views/Settings.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Start',
      component: Start
    },
    {
      path: '/settings',
      name: 'Settings',
      component: Settings
    },
  ]
})

export default router
