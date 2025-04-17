import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Index from '../views/Index.vue'
import CeVerification from '../views/CeVerification.vue'
import PowerVerification from '../views/PowerVerification.vue'
import ClientVerification from '../views/ClientVerification.vue'
import Config from '../views/Config.vue'
import Help from '../views/Help.vue'
import Fiber from '../views/Fiber.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('../views/Login.vue'),
      children: [
        {
          name: 'login',
          path: 'login',
          component: Login,
          meta: { requiresAuth: true }
        },
      ]
    }, {
      path: '/',
      component: () => import('../layouts/Menu.vue'),
      children: [
        {
          name: 'index',
          path: 'index',
          component: Index,
          meta: { requiresAuth: true }
        },

      ]
    },
    {
      path: '/',
      component: () => import('../layouts/OptionMenu.vue'),
      children: [
        {
          name: 'ceverification',
          path: 'ceverification',
          component: CeVerification,
          meta: { requiresAuth: true }
        },
        {
          name: 'powerverification',
          path: 'powerverification',
          component: PowerVerification,
          meta: { requiresAuth: true }
        },
        {
          name: 'clientverification',
          path: 'clientverification',
          component: ClientVerification,
          meta: { requiresAuth: true }

        },
        {
          name: 'fiber',
          path: 'fiber',
          component: Fiber,
          meta: { requiresAuth: true }

        },
        {
          name: 'config',
          path: 'config',
          component: Config,
          meta: { requiresAuth: true }
        },
        {
          name: 'help',
          path: 'help',
          component: Help,
          meta: { requiresAuth: true }
        }

      ]
    },

  ]
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('user');

  if (to.matched.some(record => record.meta.requiresAuth) && isAuthenticated === "") {
    next('/login');
  } else {
    next();
  }
});

export default router;
