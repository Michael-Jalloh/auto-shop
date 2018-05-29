<template lang="html">
  <div class="">
    <el-card v-for="car in cars.length" :key="car" :label="car" style="margin-bottom:10px;">
      <div class="" style="display:flex; justify-content:space-between;">
        <div class="car-content" style="display:flex; max-width:400px;">
          <div class="profile-sm">
            <my-img :image_url="cars[car - 1].car_id"></my-img>
          </div>
          <div class="">
            {{ cars[car - 1].name }}
          </div>
        </div>
        <div class="">
          <el-button @click="Edit(cars[car - 1])">Edit</el-button>
          <el-button type="danger">Delete</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import Image from '../Image'

export default {
  components: {
    'my-img':Image,
  },

  data(){
    return {
      user:{},
      cars:[]
    }
  },

  created() {
    if (!this.$auth.isAuthenticated()) {
      this.$router.push('/view-cars');
      this.$notify.error({
        title: "Forbidden",
        message: "Please login to access this page"
      })
      return
    }
    this.user = this.$store.getters.user;
    this.$auth.get('/my-cars/').then(res => {
      this.cars = res.data['data']
      console.log(res.data['data'])
    })
  },

  methods: {
    Edit(car) {
      this.$store.commit('setCar',car);
      this.$router.push({name: 'Edit-Car'});
    },
  }
}
</script>

<style lang="scss">

.profile-sm {
  width: 75px;
  height: 75px;
  min-width: 75px;
  border: 1px solid;
  border-radius: 50%;
  margin-right: 20px;
  overflow: hidden;
}
</style>
