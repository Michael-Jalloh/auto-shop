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
import AddPost from '@/components/Post/Add-Post'
import AdminPost from '@/components/Post/AdminPost'
import EditPost from '@/components/Post/Edit-Post'
import Drafts from '@/components/Post/Drafts'
import Post from '@/components/Post/Post'
import Main from '@/components/Main'
import View from '@/components/View'
import Admin from '@/components/Admin'
import AdminCars from '@/components/Admins/Admin-Cars'
import FlagCars from '@/components/Admins/Flag-Cars'
import Users from '@/components/Admins/Users'
import AdminViewCar from '@/components/Admins/ViewCar'
import AdminUser from '@/components/Admins/User'
import BlogPosts from '@/components/Blog-Posts'
import ImageSlider from '@/components/ImageSlider'


Vue.use(Router)



export default new Router({
  routes: [
    {
        path:'/image-slider',
        name: 'ImageSlider',
        component: ImageSlider
    },
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
        },
        {
          path: '/blog-post/:id',
          name: 'BlogPost',
          component: Post
        },
        {
          path: '/blog-posts',
          name: 'BlogPosts',
          component: BlogPosts
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
          component: MyCars,
          meta: {
            forAuth: true
          }

        },
        {
          path: '/add-car',
          name: 'AddCar',
          component: AddCar,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/edit-car',
          name:'Edit-Car',
          component: EditCar,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/my-profile',
          name: 'MyProfile',
          component: Profile,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/edit-my-profile',
          name: 'EditProfile',
          component: EditProfile,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/my-car/:id',
          name: 'MyCarView',
          component: MyCarView,
          meta: {
            forAuth: true
          }
        }
      ]
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin,
      children: [
        {
          path: '/admin-cars',
          name: 'AdminCars',
          component: AdminCars,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/flag-cars',
          name: 'FlagCars',
          component: FlagCars,
          meta: {
            forAuth: true
          }
        },
        {
          path:'/add-post',
          name:'Add-Post',
          component: AddPost,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/admin-posts',
          name: 'AdminPost',
          component: AdminPost,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/edit-post/:id',
          name: 'EditPost',
          component: EditPost,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/drafts',
          name:'Drafts',
          component: Drafts,
          meta: {
            forAuth: true
          }
        },
        {
          path:'/post/:id',
          name: 'Post',
          component: Post,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/admin/view-car/:id',
          name: 'AdminViewCar',
          component: AdminViewCar,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/admin/users',
          name: 'Users',
          component: Users,
          meta: {
            forAuth: true
          }
        },
        {
          path: '/admin/user/:id',
          name: 'AdminUser',
          component: AdminUser,
          meta: {
            forAuth: true
          }
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


  ],

})
