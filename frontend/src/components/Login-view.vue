<template lang="html">
  <el-dialog
    title="Login"
    :visible.sync="show"
    width="50%"
    center>

    <h3>Sign In</h3>
    <el-input placeholder="Email" class="spacing" v-model="email" clearable></el-input>
    <el-input placeholder="Password" type="password" class="spacing" v-model="password" clearable></el-input>
    <el-button type="success" class="spacing" v-bind:loading="loading" @click="login()">Login </el-button>


  </el-dialog>
</template>

<script>
import { bus } from '../main'

export default {
  data(){
    return{
      password:'',
      email:'',
      loading: false,
      show: false
    }
  },

  created(){
    bus.$on('login', ()=> {
      this.show = true
    })
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
          this.$notify({
            title:' Login',
            message: response.data['message'],
            type: response.data['status']
          });
          console.log(response.data['data'].account_type)
          this.$store.commit('setUser', response.data['data']);
        } else {
          this.$notify({
            title:' Login',
            message: response.data['message'],
            type: response.data['status']
          });
        }

      }).catch(
       response => {
         console.log(response);
         this.$notify.error({
           title: 'Login',
           message: 'Error Occur',
         })
       });
       this.show = false;
       this.loading = false;
       this.show = false;
    },

    close(){
      this.show = false;
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
