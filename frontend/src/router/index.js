import Vue from 'vue'
import Router from 'vue-router'
import ViewCars from '@/components/Cars/View-Cars'
import AddCar from '@/components/Cars/Add-Car'
import ViewCar from '@/components/Cars/View-Car'
import EditCar from '@/components/Cars/Edit-Car'
import Login from '@/components/Login'
import Register from '@/components/Register'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      name: 'View-Cars',
      component: ViewCars
    },
    {
      path: '/add-car',
      name: 'Add-Car',
      component: AddCar,
      meta: {
        forAuth: true
      }
    },
    {
      path: '/view-car',
      name: 'View-Car',
      component: ViewCar,
    },
    {
      path: '/edit-car',
      name: 'Edit-Car',
      component: EditCar,
      meta: {
        forAuth: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    }
  ]
})
