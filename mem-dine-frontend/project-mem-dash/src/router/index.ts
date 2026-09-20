// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import LogIn from '@/components/LogIn.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LogIn
    },
    {
      // 1. Define the URL path matching your RouterLink
      path: '/create-account', 
      name: 'create-account',
      // 2. Lazy-load the component (improves page load performance)
      component: () => import('../components/CreateAccount.vue') 
    }
  ]
})

export default router
