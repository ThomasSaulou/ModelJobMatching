import Vue from 'vue'
import VueRouter from 'vue-router'
import Home  from '@/views/Home/Home.vue'
import JobSheet  from '@/views/job-sheet/job-sheet.vue'
import CandidatePage  from '@/views/candidate-page/candidate-page.vue'
import MatchingPage  from '@/views/matching-page/matching-page.vue'
import CreateCandidate from '@/views/create-candidate-page/create-candidate-page.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/jobsheet',
    name: 'job-sheet',
    component: JobSheet,
  },
  {
    path: '/candidate',
    name: 'candidate-page',
    component: CandidatePage,
  },
  {
    path: '/matching',
    name: 'matching-page',
    component: MatchingPage,
  },
  {
    path: '/createcandidate',
    name: 'create-candidate-page',
    component: CreateCandidate,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
