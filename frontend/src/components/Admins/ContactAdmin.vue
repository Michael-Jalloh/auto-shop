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
        <template slot-scope="scope">
          <el-button type="primary" @click="view(scope.row)" size="small">View</el-button>
          <el-button type="danger" size="small">Delete</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      :page-size="page_size"
      layout="prev, pager, next"
      :total="total_feedback">
    </el-pagination>
    <el-dialog title="Feed Back" :visible.sync="feedback_view">
      <h3>Name: {{ feedback.name}}</h3>
      <h3>Last Name: {{ feedback.last_name}}</h3>
      <h3>Email: {{ feedback.email}}</h3>
      <h3>Telephone: {{ feedback.tel}}</h3>
      <h3>Message</h3>
      <h3>{{ feedback.msg}}</h3>
    </el-dialog>
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
      total_feedback: 100,
      feedback: {},
      feedback_view: false
    }
  },
  created(){
    this.$auth.get('/feedbacks').then( res => {
      this.feedbacks = res.data['data'];
      this.feedData = this.feedbacks.slice(0, this.page_size);
      this.total_feedback = this.feedbacks.length
      console.log(this.feedData)
    })
  },
  methods: {
    view(feedback){
      this.feedback = feedback;
      console.log(feedback)
      this.feedback_view = true;
    }
  }
}
</script>

<style lang="scss">

</style>
