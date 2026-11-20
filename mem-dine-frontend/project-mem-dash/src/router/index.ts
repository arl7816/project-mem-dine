// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import LogIn from '@/components/LogIn.vue'
import { userService } from '../../api/services/userService.ts';

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
    },
    {
      path: '/dashboard',
      name: "dashboard",
      meta: { requiresAuth: true },
      component: () => import('../components/Dashboard.vue')
    },
    {
      // TODO: need to change this requiresAuth to true once implemented
      path: '/grocery-list',
      name: 'grocery-list',
      meta: { requiresAuth: false },
      component: () => import('../components/GroceryList.vue')
    },
  ]
})

router.beforeEach(async (to) => {
  if (to.meta.requiresAuth) {
    try {
      const response = await userService.me()
      if (response.status !== 'success') {
        return { name: 'login' }
      }
    } catch {
      return { name: 'login' }
    }
  }
})

export default router
