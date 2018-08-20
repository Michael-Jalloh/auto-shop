<template lang="html">
    <img class="my-img" :src="getImage" alt="">
</template>

<script>
export default {
  props: ['image_name'],

  data(){
    return {

    }
  },
  computed: {
    getImage() {
      var url = window.location.host;
      var img  = 'http://' + url + '/api/v1/get-image/'+ this.image_name // for production
      //var img = 'http://localhost:5000/api/v1/get-image/'+this.image_name // for dev
      return img
    }
  }
}
</script>

<style lang="scss">
</style>
