<template lang="html">
  <div class="">
    <el-table
        :data="carData"
        style="width: 100%">
        <el-table-column
            prop="name"
            label="Name"
            width="150">
        </el-table-column>
        <el-table-column
            prop="owner.username"
            label="Owner"
            width="150">
        </el-table-column>
        <el-table-column
            prop="published"
            label="Published"
            width="150">
        </el-table-column>
        <el-table-column
            prop="featured"
            label="Featured"
            width="150">
        </el-table-column>
        <el-table-column
            fixed="right"
            label="Operations"
            width="150">
            <template slot-scope="scope">
              <el-button type="text">View</el-button>
              <el-button type="text">Delete</el-button>
            </template>
        </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data(){
    return {
      carData: []
    }
  },

  created(){
    this.$auth.get('/admin-cars').then( res => {
      if (res.data['status'] == 'success') {
        this.carData = res.data['data'];

      }
    })
  }

}
</script>

<style lang="css">
</style>
