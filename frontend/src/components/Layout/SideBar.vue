<template lang="html">

  <div class="">
    <el-menu default-active="2" class="side-menu" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      <el-submenu index="1">
        <template slot="title">
          <icon class="icon" scale="1.50" name="dashboard"></icon>
          <span slot="title">Dashboard</span>
        </template>
        <el-menu-item-group>
          <!--<span slot="title">View Location</span>-->
          <el-menu-item index="1-1"><router-link class="router-link" to="">Dashboard</router-link></el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <icon class="icon" scale="1.50" name="car"></icon>
          <span slot="title">Cars</span>
        </template>
        <el-menu-item-group>
          <!--<span slot="title">View Location</span>-->
          <el-menu-item index="2-1"><router-link to="/my-cars">My Cars</router-link></el-menu-item>
          <el-menu-item index="2-2"><router-link to="/add-car">Add Car</router-link></el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">
          <icon class="icon" scale="1.50" name="user"></icon>
          <span  slot="title">Profile</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="3-1"><router-link to="/my-profile">Profile</router-link></el-menu-item>
          <el-menu-item index="3-1"><router-link to="/edit-my-profile">Edit Profile</router-link></el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <!--<el-submenu index="4">
        <template slot="title">
          <icon class="icon" scale="1.50" name="envelope"></icon>
          <span  slot="title">Message</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="4-1"><router-link to="">Messages</router-link></el-menu-item>
        </el-menu-item-group>
    </el-submenu> -->
    </el-menu>
    <div class="collapse-btn" v-on:click="isCollapse = !isCollapse">
      <i  class="el-icon-arrow-left"  color="white" v-if="!isCollapse" ></i>
      <i class="el-icon-arrow-right" name="angle-right" color="black" v-if="isCollapse" scale="5"></i>
    </div>
  </div>

</template>

<script>
export default {
  data() {
      return {
        isCollapse: true
      };
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      toggle(){
        this.isCollapse = !this.isCollapse;
      },

      profile(){
        alert("Hello");
      }
    }
}
</script>

<style lang="scss"  >

  .side-menu{
    height: calc(100vh - 120px);

  }

  .collapse-btn {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    //background-color: #343A40;
  }

  .router-link {
    text-decoration: none;
  }
</style>
