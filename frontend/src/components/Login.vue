<template lang="html">
  <div class="login">
    <el-card>
      <h3>Sign In</h3>
      <el-input placeholder="Email" class="spacing" v-model="email" clearable></el-input>
      <el-input placeholder="Password" type="password" class="spacing" v-model="password" clearable></el-input>
      <el-button type="success" class="spacing" v-bind:loading="loading" @click="login()">Login </el-button>
      <p class="spacing">If You don't have an account? You can create one <router-link :to="{ name:'Register', params: {} }">here!</router-link></p>
    </el-card>


  </div>
</template>

<script>
export default {
  data(){
    return{
      password:'',
      email:'',
      loading: false
    }
  },
  methods: {
    login() {
      this.loading = true;
      this.$auth.login({
        email:this.email,
        password:this.password
      }).then( response => {
        if (response.data['status']=='success') {
          this.$auth.setTokens(response.data, this.$ls);
          if (response.data['data'].account_type == "individual") {
            this.$router.push('/main')
          } else {
            this.$router.push('/')
          }
          this.$notify.success({
            title:' Login',
            message: response.data['message'],
            type: response.data['status']
          });
          console.log(response.data['data'].account_type)
          this.$store.commit('setUser', response.data['data']);
        } else {
          this.$notify.success({
            title:' Login',
            message: response.data['message'],
            type: response.data['status']
          });
        }

      }).catch(
       response => {
         console.log(response);
       });

      this.loading = false;
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
