<template lang="html">
  <el-card class="box-card" v-show="show">
    <div class="" style="display:flex; justify-content:space-between; ">
      <div class="car-content" style="display:flex; max-width:400px;">
        <div class="profile-sm">
          <img class="img" :src="image_url" alt="">
        </div>
        <div class="">
          {{ car.name }}
        </div>
      </div>

      <div class="">
        <el-button @click="Edit(car)">Edit</el-button>
        <el-button type="danger" @click="Delete(car)" >Delete</el-button>
      </div>
    </div>
  </el-card>
</template>

<script>
export default {
  props: ['car'],

  data(){
    return {
      image_url: '',
      show: true
    }
  },

  created(){

    this.image_url = 'http://localhost:5000/api/v1/get-image-by-id/'+ this.car.car_id;

  },

  methods: {
    Edit(car) {
      this.$store.commit('setCar',car);
      this.$router.push({name: 'Edit-Car'});
    },

    Delete(car){
      console.log(car);
      this.$auth.delete('/delete-car/'+this.car.car_id).then( res => {
        console.log(res)
        this.$notify({
          title: "Deletion",
          message: res.data['message'],
          type: res.data['status']
        }),

        this.show = false
      })

    }
  }
}
</script>

<style lang="scss">

.profile-sm {
  .img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
}

</style>
