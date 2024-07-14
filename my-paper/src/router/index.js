import { createRouter, createWebHistory } from 'vue-router'
import ChatBox from '@/components/ChatBox.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ChatBox,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
