// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
import VueLocalStorage from 'vue-localstorage'
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuex from 'vuex'
import VeeValidate from 'vee-validate'
import Auth from './packages/auth/Auth.js'


Vue.config.productionTip = false
Vue.use(VueAxios, axios);
var url = window.location.hostname + ':'+window.location.port;
axios.defaults.baseURL = "http://localhost:5000"; // for dev
//axios.defaults.baseURL = url; // for production

Vue.use(Vuex)
Vue.use(ElementUI, { locale} )
Vue.use(VueLocalStorage,{
  name:'ls'
})
Vue.use(Auth)
Vue.auth.setBaseUrl("http://localhost:5000/api/v1")
Vue.auth.setStorage(Vue.ls)
Vue.component('icon',Icon)

export const bus = new Vue()

router.beforeEach(
  (to, from, next) => {
    if(to.matched.some(record => record.meta.forVisitors)){
      if (Vue.auth.isAuthenticated()) {
        next({
          path: '/'
        })
      } else {
        next()

      }
    } else if(to.matched.some(record => record.meta.forAuth)){
      if ( ! Vue.auth.isAuthenticated()) {
        next({
          path: '/login'
        })
      } else {
        next()

      }
    } else {next()}
  }
)


const store = new Vuex.Store({
  state: {
    car: {},
    cars: [],
  },

  getters: {
    car: state => state.car,
    cars: state => state.cars
  },

  mutations: {
    setCar: (state, payload) => {
      state.car = payload;
    },

    setCars: (state, payload) => {
      state.cars = payload;
    }
  }

})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store: store,
  components: { App },
  template: '<App/>'
})
