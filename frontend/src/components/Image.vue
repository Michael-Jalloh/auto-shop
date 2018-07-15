<template lang="html">
    <img class="my-img" :src="getImage" alt="">
</template>

<script>
export default {
  props: ['image_url'],

  data(){
    return{

    }
  },
   created(){
     var url = window.location.host;
    // this.imageUrl ='http://localhost:5000/get-photo/'+this.image_url // for dev
     this.imageUrl = 'http://' + url + '/get-photo/'+ this.image_url // for production
   },

   computed: {
     getImage() {
       var url = window.location.host;
       var img  = 'http://' + url + '/get-photo/'+ this.image_url // for production
       //var img = 'http://localhost:5000/get-photo/'+this.image_url // for dev
       return img
     }
   }
}
</script>

<style lang="scss">
.my-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
