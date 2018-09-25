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
     this.imageUrl = this.$store.getters.url + '/get-photo/'+ this.image_url;
   },

   computed: {
     getImage() {
       var img  = this.$store.getters.url + '/get-photo/'+ this.image_url;
       return img;
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
