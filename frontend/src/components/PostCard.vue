<template lang="html">
  <el-card class="post-card relative"  style="margin-bottom:10px;">
    <div class="overlay" @click="selectPost">
      <div class="post-content">
          <img  :src="getImage"></img>
        <div class="" style="margin: 20px;">
          <h4>{{ post.title }}</h4>
        </div>
      </div>
    </div>
  </el-card>
</template>

<script>
export default {
  props: ['post'],

  data(){
    return {

    }
  },

  computed: {
    getImage(){
      //var image_url = "http://localhost:5000/api/v1/get-image/"+this.post.pic
      var url = window.location.host;
       var image_url = "http://" +url+"/api/v1/get-image/" + this.post.pic
      return image_url
    }
  },

  methods: {
    selectPost() {
      this.$router.push({name: 'BlogPost',params: {id: this.post.id}});
    }
  }
}
</script>

<style lang="scss">
.post-card {
  width: 47%;
  margin: 10px;

    @include until($large-tablet){
      width: 100%;
    }

    img {
      width: 100%;
      height: 300px;
    }
  }
</style>
