// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueLocalStorage from 'vue-localstorage'
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'
import axios from 'axios'
import VueAxios from 'vue-axios'
import './layout.scss'


Vue.config.productionTip = false
Vue.use(VueAxios, axios);
axios.defaults.baseURL = "http://localhost:5000/api/v1";

Vue.use(ElementUI)
Vue.use(VueLocalStorage,{
  name:'ls'
})

Vue.component('icon',Icon)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
