// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import VueResource from 'vue-resource'
import VueAnalytics from 'vue-analytics'

import Icon from 'vue-awesome/components/Icon'
import 'vue-awesome/icons'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueCookie from 'vue-cookie'

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(BootstrapVue)
Vue.component('icon', Icon)
Vue.use(VueCookie)
Vue.use(VueAnalytics, {
  id: 'UA-105182087-1',
  router
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
