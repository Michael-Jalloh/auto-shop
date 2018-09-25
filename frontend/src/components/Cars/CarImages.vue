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
      var img  = this.$store.getters.url + '/api/v1/get-image/'+ this.image_name // for production
      return img
    }
  }
}
</script>

<style lang="scss">
</style>
