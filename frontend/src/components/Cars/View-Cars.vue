<template lang="html">
  <div class="">
    <h3>Luxury Cars</h3>
    <el-carousel ref="carousel" arrow="always" :autoplay="false">
      <el-carousel-item class="overlay" v-for="item in cars.length" :key="item">
        <h3>{{ cars[item - 1] }}</h3>
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
      <el-carousel-item v-for="item in cars" :key="item">
        <h3>{{ item.pic}}</h3>
        <img :src="item.pic" alt="">
      </el-carousel-item>
    </el-carousel>
    <hr>
  </div>
</template>

<script >
export default {
  data(){
    return {
      cars: [],
      autoplay: false
    }
  },

  created() {
    this.$http.get('/get-cars').then( res => {
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
    }
  }
}
</script>

<style lang="scss">

</style>
