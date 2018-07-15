<template lang="html">
  <div class="">
    <el-card class="box-card">
        <div class=" info">
            <h2>Username: {{ user.username}}</h2>
            <h4>Email: {{ user.email}}</h4>
            <h4>Tel: {{ user.contact }}</h4>
        </div>
    </el-card>
    <hr>
    <h3>{{ user.username}}'s Cars</h3>
    <div class="flex-container" >
      <el-card class="car-card" v-for="car in cars.length" :key="car" :label="car" style="margin-bottom:10px;">
        <div class="" >
          <div class="car-content">
              <my-img :image_url="cars[car - 1].car_id"></my-img>
            <div class="" style="margin: 20px;">
              <h4>{{ cars[car - 1].name }}</h4>
            </div>
          </div>
          <div class="">
            <el-button type="primary" @click="View(cars[car - 1].car_id)" >View</el-button>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import Image from '../Image.vue';

export default {


  components: {
    'my-img': Image,
  },

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
    this.url = window.location.host;
    this.imageUrl = "http://" + this.url+"/api/v1/get-profile-pic/"+this.$route.params.id // production
    //this.imageUrl = "http://localhost:5000/api/v1/get-profile-pic/"+this.$route.params.id

    this.$http.get("/api/v1/get-profile/"+this.$route.params.id).then( res => {
      this.user = res.data['data'];
      console.log(this.user)
      this.$http.get('api/v1/user-cars/' + this.user.id).then( res => {
        this.cars = res.data['data']
      })
    });



  },

  methods: {
    View(car_id){
      this.$router.push({name: 'View-Car', params: { id: car_id}})
    }
  }

}
</script>

<style lang="scss">
.profile-img {
  width: 250px;
  height: 250px;
  min-width: 250px;
  border: 1px solid;
  border-radius: 40%;
  margin: 0px;
  margin-right: 50px;
  overflow: hidden;
}


.car-card {
  width: 47%;
  margin: 10px;

  @include until($large-tablet){
    width: 100%;
  }

}



</style>
