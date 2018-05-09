<template lang="html">
    <img class="my-img" :src="imageUrl" alt="">
</template>

<script>
export default {
  props: ['image_url'],

  data(){
    return{

    }
  },
   created(){
     var url = window.location.hostname+':'+window.location.port
    this.imageUrl ='http://localhost:5000/get-photo/'+this.image_url // for dev
     //this.imageUrl = 'http://' + url + '/get-photo/'+ this.image_url // for production

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
