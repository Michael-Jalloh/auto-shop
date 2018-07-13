<template lang="html">
    <div class="">
      <el-table
          :data="userData"
          style="width: 100%">
          <el-table-column
              prop="username"
              label="Username">
          </el-table-column>
          <el-table-column
              prop="email"
              label="Email">
          </el-table-column>
          <el-table-column
              label="Actions">
              <template slot-scope="scope">
                <el-button type="danger" @click="Delete(scope.row)">Delete</el-button>
              </template>
          </el-table-column>
      </el-table>
    </div>
</template>

<script>
export default {
  data(){
    return {
      userData: []
    }
  },

  created(){
    this.$auth.get('/get-users').then(res => {
      if (res.data['status']=='success') {
        this.userData = res.data['data'];
      }
    })
  },

  methods: {
    Delete(user){
      console.log(user);
    }
  }
}
</script>

<style lang="css">
</style>
