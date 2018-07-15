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
                <el-button type="" @click="View(scope.row)">Profile</el-button>
                <el-button type="danger" @click="Delete(scope.row)">Delete</el-button>
              </template>
          </el-table-column>
      </el-table>
    </div>
</template>

<script>
import { bus } from '../../main'
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
    }).catch(res => {
      if (res.response.status==422) {
        bus.$emit('login')
      }
    })
  },

  methods: {
    Delete(user){
      this.$auth.delete('/delete-user/'+user.id).then(res =>{
        this.$notify.success({
          title: 'User',
          message: res.data['message']
        })
        var index = this.userData.indexOf(user)
        this.userData.splice(index,1)
      }).catch(res => {
        if (res.response.status==422) {
          bus.$emit('login')
        }
      })
    },
    View(user){
      this.$router.push({name:"AdminUser", params:{id:user.id}})
    }
  }
}
</script>

<style lang="css">
</style>
