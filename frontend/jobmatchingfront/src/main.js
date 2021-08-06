import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import VueApexCharts from 'vue-apexcharts'

Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(VueApexCharts)



new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
