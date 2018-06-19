import Vue from 'vue'
import Router from 'vue-router'
import ViewCars from '@/components/Cars/View-Cars'
import AddCar from '@/components/Cars/Add-Car'
import ViewCar from '@/components/Cars/View-Car'
import EditCar from '@/components/Cars/Edit-Car'
import MyCars from '@/components/Cars/MyCars'
import MyCarView from '@/components/Cars/My-CarView'
import TypeCars from '@/components/Cars/TypeCars'

import Login from '@/components/Login'
import Register from '@/components/Register'
import Profile from '@/components/User/Profile'
import EditProfile from '@/components/User/Edit-Profile'
import User from '@/components/User/User'
import AddBlog from '@/components/Blog/Add-Blog'
import Main from '@/components/Main'
import View from '@/components/View'


Vue.use(Router)



export default new Router({
  routes: [
    {
      path:'/',
      name: 'View',
      component: View,
      children: [
        {
          path: '/view-cars',
          name: 'ViewCars',
          component: ViewCars
        },
        {
          path: '/view-car/:id',
          name: 'View-Car',
          component: ViewCar,
        },
        {
          path: '/user/:id',
          name: 'UserProfile',
          component: User
        },
        {
          path: '/cars/:id',
          name: 'Type-Cars',
          component: TypeCars
        }
      ]
    },
    {
      path:'/main',
      name: 'Main',
      component: Main,
      children: [
        {
          path:'/my-cars',
          name: 'MyCars',
          component: MyCars
        },
        {
          path: '/add-car',
          name: 'AddCar',
          component: AddCar,
        },
        {
          path: '/edit-car',
          name:'Edit-Car',
          component: EditCar
        },
        {
          path: '/my-profile',
          name: 'MyProfile',
          component: Profile
        },
        {
          path: '/edit-my-profile',
          name: 'EditProfile',
          component: EditProfile
        },
        {
          path: '/my-car/:id',
          name: 'MyCarView',
          component: MyCarView
        }
      ]
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
    },
    {
      path:'/add-blog',
      name:'Add-Blog',
      component: AddBlog
    },

  ],
  
})
