<template lang="html">
  <div class="profile-img">
    <img :src="profile_url" alt="">
  </div>
</template>

<script>
export default {

  data(){
    return {
      profile_url: '',
    }
  },

  created(){

  }
}
</script>

<style lang="css">
</style>
