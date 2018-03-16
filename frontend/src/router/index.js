import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ViewCars from '@/components/Cars/View-Cars'
import AddCar from '@/components/Cars/Add-Car'

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
    }
  ]
})
