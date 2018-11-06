<template lang="html">
  <div class="">
    <app-header></app-header>
    <el-container>
      <app-side-bar></app-side-bar>
      <div class="content">
        <el-main class="main">
          <router-view/>
        </el-main>
        <app-footer></app-footer>
    </div>
    </el-container>
  </div>

</template>

<script>
import Header  from './Layout/Header.vue'
import SideBar from './Admins/SideMenu.vue'
import Footer from '@/components/Layout/Footer.vue'


export default {
  name: 'Main',

  components: {
    'app-header': Header,
    'app-side-bar': SideBar,
    'app-footer': Footer,
  },

  created(){
    //this.$router.push({path: '/my-cars'})
  }
}
</script>

<style lang="css">





.el-footer {
  padding: 0px !important;
}
</style>
