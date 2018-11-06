<template lang="html">
  <div class="" >
    <h2 style="text-align: center">Contact Us</h2>
    <p style="text-align: center">We will like to hear from you, Please contact us with the form below</p>
    <p style="text-align: center">Please fill in all the details incase we want to contact you.</p>
    <div class=" flex-container mb-50">
      <el-input class="input" v-model="form.name" placeholder="Name"></el-input>
      <el-input class="input" v-model="form.last_name" placeholder="Last Name"></el-input>
    </div>
    <div class=" flex-container mt-50">
      <el-input class="input" v-model="form.email" placeholder="Email"></el-input>
      <el-input class="input" v-model="form.tel" placeholder="Telephone"></el-input>
    </div>
    <div class="mt-50 message">
      <el-input type="textarea"
        v-model="form.msg"
        :rows="5"
        placeholder="Message" ></el-input>
    </div>
    <el-button type="success" @click="send" class="mt-50">Submit</el-button>
  </div>
</template>

<script>
export default {
  data(){
    return {
      form: {
        name: '',
        last_name: '',
        email: '',
        tel: '',
        msg: ''
      },
    }
  },

  methods: {
    send(){
      this.$http.post('/api/v1/save-feedback', this.form).then(res => {
        this.form.name ="";
        this.form.last_name ="";
        this.form.email ="";
        this.form.tel ="";
        this.form.msg ="";
        this.$notify.success({
          title: 'FeedBack',
          message: res.data['message']
        })
      })
    }
  }
}
</script>

<style lang="scss">
.input {
  @include at-least($desktop){
    width: 44%;
    margin-right: 55px;
  }

  input {
    border-radius: 0;
    border: none;
    border-bottom: 2px solid;
  }

}

.message {
  width: 97%;

  textarea {
    border: none;
    border-radius: 0;
    border-bottom: 2px solid;
  }
}
.mt-50 {
  @include at-least($tablet){
      margin-top: 50px;
  }
}
</style>
