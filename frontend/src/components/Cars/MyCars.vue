<template lang="html">
  <div class="">

    <hr>
    <div class=" flex-container">
      <car  v-for="car in cars.length" :key="car" :car="cars[car - 1]" ></car>
      <div class="" v-if="no_car">
        <p>You haven't added any cars yet...s</p>
      </div>
    </div>
  </div>
</template>

<script>
import Image from '../Image'
import Car from './Car'

export default {
  components: {
    'my-img':Image,
    'car': Car
  },

  data(){
    return {
      user:{},
      cars:[],
      no_car: true
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
      this.cars = res.data['data'];
      console.log(res.data['data']);
      this.no_car = false;
    }).catch( res => {
      if (error.response.status == 401) {
        bus.$emit('login')
      } else if (error.response.status == 422) {
        bus.$emit('login')
      }
    })
  },

  methods: {
    Edit(car) {
      this.$store.commit('setCar',car);
      this.$router.push({name: 'Edit-Car'});
    },

    View(car_id){
      console.log(car_id);
      this.$router.push('/my-car/'+car_id)
    },

    Delete(car) {
      this.cars.splice(car,1);

    }
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
