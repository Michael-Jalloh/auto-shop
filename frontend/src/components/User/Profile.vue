<template lang="html">
  <div class="">
    <el-card class="box-card">
      <div class="" style="display:flex;">
        <div class="">
          <div class="profile-img">
            <img src="" alt="">
          </div>
          <el-button>Update</el-button>
        </div>
        <div class="">
            <p>{{ user }}</p>
            <p>{{ }}</p>
            <el-button>Edit Profile</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {

  components: {
    'my-img': Image,
  },

  data(){
    return {
      user: {},
      cars: []
    }
  },

  created() {
    this.user = this.$store.getters.user;
    this.$auth.get('/my-cars/'+this.user.id).then(res => {
      this.cars = res.data['data']
      console.log(res.data['data'])
    })
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
