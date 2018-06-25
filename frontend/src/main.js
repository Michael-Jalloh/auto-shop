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
import Ability from './packages/ability/ability.js'



Vue.config.productionTip = false
Vue.use(VueAxios, axios);
var url = window.location.hostname + ':'+window.location.port;
axios.defaults.baseURL = "http://localhost:5000"; // for dev
//axios.defaults.baseURL = "http://" + url; // for production

Vue.use(Vuex)
Vue.use(ElementUI, { locale} )
Vue.use(VueLocalStorage,{
  name:'ls'
})
Vue.use(Auth)
Vue.use(Ability)
Vue.auth.setBaseUrl("http://localhost:5000/api/v1") // for dev
//Vue.auth.setBaseUrl("http://"+url+ "/api/v1") // for production
Vue.auth.setStorage(Vue.ls)
Vue.component('icon',Icon)

Vue.filter('capitalize', function(value){
  return value.charAt(0).toUpperCase() + value.slice(1);
})
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
    user: [],
  },

  getters: {
    car: state => state.car,
    cars: state => state.cars,
    user: state => state.user,
  },

  mutations: {
    setCar: (state, payload) => {
      state.car = payload;
    },

    setCars: (state, payload) => {
      state.cars = payload;
    },

    setUser: (state, payload) => {
      state.user = payload;
    }
  }

})

export const myBus = new Vue()

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store: store,
  components: { App },
  template: '<App/>'
})
