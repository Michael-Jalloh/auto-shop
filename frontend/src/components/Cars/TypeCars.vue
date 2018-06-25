<template lang="html">
  <div class="">
    <h3>{{ car_type | capitalize }} Cars</h3>
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
            <h3>Price: D{{ cars[car - 1].price}}</h3>
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
      car_type: '',
      cars: [],
    }
  },


    watch: {
      '$route.params.id': function(id){
        this.car_type = id;
        this.$http.get('/api/v1/get-cars/'+ this.car_type).then( res => {
          this.cars = [];
          this.cars = res.data['data'];
        })
      }
    },

  created(){
    this.car_type = this.$route.params.id;
    this.$http.get('/api/v1/get-cars/'+ this.car_type).then( res => {
      this.cars = res.data['data'];
    })
  },

  methods: {
    selectCar(car) {
      this.$store.commit('setCar',car);
      this.$router.push({name: 'View-Car',params: {id: car.car_id}});
    }
  }
}
</script>

<style lang="scss">
.car-card {
  width: 47%;
  margin: 10px;

  @include until($large-tablet){
    width: 100%;
  }

  .details {
    position: absolute;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
    padding: 30px;
    color: #ffffff;
    display: none;
  }

  &:hover {
    .details{
      display: block;
    }
  }

}

</style>
