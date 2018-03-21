<template lang="html">
  <img class="my-img" :src="imageUrl" alt="">
  <!--<h1>{{ imageUrl }}</h1>-->
</template>

<script>
export default {
  props: ['image_url'],

  data(){
    return{

    }
  },
   created(){
     this.imageUrl ='http://localhost:5000/get-photo/'+this.image_url
   }
}
</script>

<style lang="scss">
my-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
