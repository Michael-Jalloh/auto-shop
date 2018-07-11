<template>
  <el-table
      :data="posts"
      style="width: 100%">
      <el-table-column
          prop="title"
          label="Title">
      </el-table-column>
      <el-table-column
          label="Published"
          width="150">
          <template slot-scope="scope">
            <el-checkbox v-model="scope.row.publish"  @change="published_check(scope.row)"></el-checkbox>
          </template>
      </el-table-column>
      <el-table-column
          fixed="right"
          label="Operations"
          width="150">
          <template slot-scope="scope">
            <el-button type="text" @click="View(scope.row)">View</el-button>
            <el-button type="text" @click="Edit(scope.row)">Edit</el-button>
            <el-button type="text" @click="Delete(scope.row)">Delete</el-button>
          </template>
      </el-table-column>
  </el-table>
</template>
<script>
  export default {

    data(){
      return {
        posts:[]
      }
    },

    created(){
      this.$http.get('/api/v1/all-posts').then(res => {
        this.posts = res.data['data']
        console.log(res.data['data'])
      }).catch(res => {
        console.log(res);
      })
    },

    methods: {
      published_check(post){
        alert(post)
      },
      View(post){
        this.$router.push({name:'Post', params:{id:post.id}})
      },
      Delete(post){
        var index = this.posts.indexOf(post)
        this.$http.delete('/api/v1/delete-post/'+post.id).then(res => {
          if (res.data['status'] == 'success') {
            this.posts.splice(index,1);
            this.$notify.success({
              title:'Post',
              message:'Post has been deleted'
            })
          }
        })
      },
      Edit(post){
        this.$router.push({name:'EditPost', params:{id:post.id}})
      }
    }
  }
</script>
