<template lang="html">
  <div class="login">
    <el-card>
      <h3>Register</h3>
      <el-input placeholder="Email" class="spacing" v-model="form.email" clearable></el-input>
      <el-input placeholder="username" class="spacing" v-model="form.username" clearable></el-input>
      <el-input placeholder="Password" type="password" class="spacing" v-model="form.password" clearable></el-input>
      <el-input placeholder="Confirm Password" type="password" class="spacing" v-model="form.password_confirm" clearable></el-input>
      <el-button v-show="form.password && form.username && form.password == form.password_confirm && form.email" type="success" class="spacing" v-bind:loading="loading" @click="Register()">Register</el-button>
      <el-button type="danger" @click="cancel">Cancel</el-button>
    </el-card>
  </div>
</template>

<script>
export default {
  data(){
    return{
      loading: false,
      form: {
        password:'',
        password_confirm:'',
        email:'',
        username: ''
      },
    }
  },
  methods: {
    Register(){
      if (this.form.password == this.form.password_confirm){
        this.$http.post('/api/v1/sign-up', this.form).then(res => {
          this.$notify({
            title: 'Sign Up',
            message: res.data['message'],
            type: res.data['status']
          });
          this.$router.push('/login')
        }).catch(res => {
          console.log(res.data);
        });
      }else {
        this.$notify({
          title:'Error',
          message: 'Passwords do not match',
          type: 'error'
        })
      }
      console.log(this.form);
    },

    cancel(){
      this.$router.push('/view-cars')
    }
  }
}
</script>

<style lang="scss">
.spacing {
  margin: 10px 0;
}

.login {
  display: flex;
  width: 100%;
  justify-content: center;
  height: 100%;
  align-items: center;

}
</style>
