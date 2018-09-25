<template lang="html">
  <div class="">
    <h3>Featured Cars</h3>
    <el-carousel ref="carousel" indicator-position="none" arrow="always" :autoplay="false" v-loading="loading">
      <el-carousel-item    v-for="item in cars.length"  :key="item">
        <div class="" v-on:click="selectCar(cars[item - 1 ])" class="overlay">
          <my-img v-bind:image_url="cars[item - 1].car_id"    ></my-img>
        </div>
      </el-carousel-item>
    </el-carousel>
    <div class="spacing" >
      <el-button @click="Refresh">Refresh</el-button>
    </div>


  </div>
</template>

<script>

import Image from '../Image.vue'
import { bus } from '../../main'

export default {
  components: {
    'my-img': Image,
  },

  data(){
    return {
      cars: [],
      autoplay: false,
      loading: true
    }
  },

  created() {
    if(this.$store.getters.cars && this.$store.getters.cars.length > 0){
      this.cars = this.$store.getters.cars;
      this.loading = false
    } else{
      this.$http.get('/api/v1/featured-cars').then( res => {
        this.cars = res.data['data'];
        this.$store.commit('setCars',this.cars)
        console.log(res.data['data']);
        this.loading = false;
        //console.log(res.data);
      }).catch( res => {
        console.log(res);
      })
    }

  },


  methods: {

    selectCar(car) {
      this.$store.commit('setCar',car);
      this.$router.push({name: 'View-Car',params: {id: car.car_id}});
    },

    test(){
      bus.$emit('login');
    },

    Refresh(){
        console.log(this.$store.getters.url)
        this.$http.get('/api/v1/featured-cars').then( res => {
            this.cars = res.data['data'];
            this.$store.commit('setCars',this.cars)
            console.log(res.data['data']);
            this.loading = false;
            //console.log(res.data);
      }).catch( res => {
        console.log(res);
      })
    }
  }
}
</script>

<style lang="scss">

</style>
