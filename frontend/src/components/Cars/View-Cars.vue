<template lang="html">
  <div class="">
    <el-button @click="test">Location</el-button>
    <h3>Luxury Cars</h3>
    <el-carousel ref="carousel" arrow="always" :autoplay="false">
      <el-carousel-item class="overlay" v-for="item in cars.length" :key="item">
        <my-img v-bind:image_url="cars[item - 1].pic" ></my-img>
      </el-carousel-item>
    </el-carousel>
    <hr>
    <h3>New Cars</h3>
    <el-carousel  arrow="always" :autoplay="false">
      <el-carousel-item v-for="item in cars.length" :key="item">
        <h3>{{ cars[item - 1] }}</h3>
      </el-carousel-item>
    </el-carousel>
    <hr>
    <h3>Old Cars</h3>
    <el-carousel  arrow="always" :autoplay="false">
      <el-carousel-item v-for="item in cars.length" :key="item">
        <my-img v-bind:image_url="cars[item - 1].pic" ></my-img>
      </el-carousel-item>
    </el-carousel>
    <hr>
  </div>
</template>

<script >
import Image from '../Image.vue'

export default {
  components: {
    'my-img': Image,
  },

  data(){
    return {
      cars: [],
      autoplay: false
    }
  },

  created() {
    this.$http.get('/api/v1/get-cars').then( res => {
      this.cars = res.data['data'];
      console.log(res.data['data']);
      //console.log(res.data);
    }).catch( res => {
      console.log(res);
    })
  },
  methods: {
    printCar() {
      console.log(this.cars);
      console.log(this.cars.length);
      this.$refs.carousel.next();
    },

    test() {
      var url = window.location.hostname + ':'+window.location.port;
      alert(url);
    }
  }
}
</script>

<style lang="scss">

</style>
