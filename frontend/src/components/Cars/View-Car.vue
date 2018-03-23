<template lang="html">
  <div class="flex-container">
    <div class="grid-md-8">
      <el-card class="box-card">
        <p>{{ car }}</p>
      </el-card>
    </div>
    <div class="grid-md-4 ">
      <el-card class="box-card">
      </el-card>
    </div>
  </div>
</template>

<script>

import {bus} from '../../main';

export default {
  data(){
    return {
      car: {}
    }
  },

  created(){
    this.car = this.$store.getters.car;
  }

}
</script>

<style lang="css">


</style>
