<template lang="html">
  <div class="">
    <el-card class="box-card">
      <div class="" style="display:flex;">
        <div class="">
          <div class="profile-img">
            <img :src="imageUrl" alt="">
          </div>
        </div>
        <div class="">
            <h2>Username: {{ user.username}}</h2>
            <h4>Email: {{ user.email}}</h4>
            <h4>Address: {{user.location}}</h4>
            <h4>Tel: {{ user.contact }}</h4>
            <h4>Bio: {{ user.bio}}</h4>
        </div>
      </div>
    </el-card>

    
  </div>
</template>

<script>
export default {



  data(){
    return {
      url:'',
      user: {},
      cars: [],
      imageUrl: '',
    }
  },

  created() {
    //alert(this.$route.params.id)
    //this.imageUrl = this.url+"/api/v1/get-profile-pic/"+this.user.id // production
    this.imageUrl = "http://localhost:5000/api/v1/get-profile-pic/"+this.$route.params.id

    this.$http.get("/api/v1/get-profile/"+this.$route.params.id).then( res => {
      this.user = res.data['data'];
    });


  },

}
</script>

<style lang="scss">
.profile-img {
  width: 250px;
  height: 250px;
  min-width: 250px;
  border: 1px solid;
  border-radius: 50%;
  margin-right: 50px;
  overflow: hidden;
}
</style>
