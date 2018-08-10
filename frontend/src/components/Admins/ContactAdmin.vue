<template>
  <div id="">
    <el-table
      :data="feedData"
      height="450">
      <el-table-column
        prop="name"
        label="Name">
      </el-table-column>
      <el-table-column
        prop="last_name"
        label="Last Name">
      </el-table-column>
      <el-table-column
        prop="email"
        label="Email">
      </el-table-column>
      <el-table-column
        prop="tel"
        label="Telephone">
      </el-table-column>
      <el-table-column
        label="Operation">
        <template slot="scope-slot">
          <el-button type="primary" size="small">View</el-button>
          <el-button type="danger" size="small">Delete</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      :page-size="page_size"
      layout="prev, pager, next"
      :total="total_feedback">
    </el-pagination>
  </div>
</template>

<script>
export default {
  name: "",
  data(){
    return {
      feedbacks: [],
      feedData: [],
      page_size: 10,
      total_feedback: 100
    }
  },
  created(){
    this.$auth.get('/feedbacks').then( res => {
      this.feedbacks = res.data['data'];
      this.feedData = this.feedbacks.slice(0, this.page_size);
      console.log(this.feedData)
    })
  }
}
</script>

<style lang="scss">

</style>
