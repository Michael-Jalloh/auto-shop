<template lang="html">
  <div class="">
    <app-header></app-header>
    <el-container>
      <app-side-bar></app-side-bar>
      <el-container>
        <el-main class="main">
          <router-view/>
        </el-main>
        <el-footer class="footer">
          <app-footer></app-footer>
        </el-footer>
      </el-container>
    </el-container>
  </div>

</template>

<script>
import Header  from './Layout/Header.vue'
import SideBar from './Layout/SideBar.vue'
import Footer from '@/components/Footer.vue'


export default {
  name: 'Main',

  components: {
    'app-header': Header,
    'app-side-bar': SideBar,
    'app-footer': Footer,
  },

  created(){
    this.$router.push({path: '/my-cars'})
  }
}
</script>

<style lang="css">



.main{
  height: calc(100vh - 120px);
}

.el-footer {
  padding: 0px !important;
}
</style>
