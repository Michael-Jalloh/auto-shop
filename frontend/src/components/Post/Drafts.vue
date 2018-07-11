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
            <el-checkbox v-model="scope.row.published"  @change="published_check(scope.row)"></el-checkbox>
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
      this.$http.get('/api/v1/drafts').then(res => {
        this.posts = res.data['data']
      }).catch(res => {
        console.log(res);
      })
    },

    methods: {
      published_check(post){

      },
      View(post){

      },
      Delete(Post){

      },
      Edit(post){
        this.$router.push({name:'EditPost', params:{id:post.id}})
      }
    }
  }
</script>
