import Vue from 'vue'
import Router from 'vue-router'
import ViewCars from '@/components/Cars/View-Cars'
import AddCar from '@/components/Cars/Add-Car'
import ViewCar from '@/components/Cars/View-Car'
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
      component: AddCar
    },
    {
      path: '/view-car',
      name: 'View-Car',
      component: ViewCar,
    }
  ]
})
