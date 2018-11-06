<template lang="html">
    <div class="">
      <h3>{{  search }} </h3>
      <el-button @click="Refresh">Refresh</el-button>
      <hr>
      <div class="flex-container" >
        <el-card class="car-card relative"  v-for="car in cars.length" :key="car" :label="car" style="margin-bottom:10px;">
          <div class="overlay" @click="selectCar(cars[ car - 1])">
            <div class="car-content">
                <my-img :image_url="cars[car - 1].car_id"></my-img>
              <div class="" style="margin: 20px;">
                <h4>{{ cars[car - 1].name }}</h4>
              </div>
            </div>
            <div class="details">
              <h3>Price: {{ cars[car - 1].price}}</h3>
              <h3>Brand: {{ cars[car - 1].brand }}</h3>
              <h3>Year: {{ cars[car - 1].year }}</h3>
            </div>
          </div>
        </el-card>
      </div>
    </div>
</template>

<script>
import Image from '../Image.vue'

export default {
    components: {
      'my-img': Image
    },

    data(){
        return {
            search: "",
            cars:[]
        }

    },

    created(){
      this.search = this.$route.params.search;
      this.$http.post('/api/v1/search',{"search":this.search}).then( res => {
        this.cars = res.data['data'];
        console.log("Cars")
        console.log(this.cars)
      })
    },

    methods: {
      selectCar(car) {
        this.$store.commit('setCar',car);
        this.$router.push({name: 'View-Car',params: {id: car.car_id}});
      },

      Refresh(){
        this.$http.post('/api/v1/search',{"search":this.search}).then( res => {
          this.cars = res.data['data'];
          console.log("Cars")
          console.log(this.cars)
        })
      }
    }
}
</script>

<style lang="scss">
</style>
