<template lang="html">
  <div class="post">
    <h2 class="post-title">{{ post.title}}</h2>
    <div class="" v-if="post.image_url">
      <img :src="post.image_url" alt="">
    </div>
    <hr>
    <div class="" v-html="post.content">

    </div>
    <router-link class="back-btn" :to="{ name: 'BlogPosts', params: {} }">Back</router-link>
  </div>
</template>

<script>
export default {
  data(){
    return {
      post: {
        content: '',
        title:'',
        image_url: ''
      }
    }
  },

  created(){
    this.$http.get('/api/v1/post/'+this.$route.params.id).then(res => {
      this.post = res.data['data'];
      var url = 'http://' + window.location.host + '/api/get-image/' + this.post.pic // prod
      //var url = 'http://localhost:5000/api/v1/get-image/'+ this.post.pic
      this.post.image_url = url;
    })
  }

}
</script>

<style lang="scss">
.post {
  max-width: 900px;
  margin: 0 auto;

  img {
    max-width: 100%;
  }

  .ql-video {
    width: 100%;
    height: 400px;
  }
}
blockquote {
  border-left: 4px solid gray;
  padding: 10px;
  word-break: break-all;
  background-color: azure;
  font-size: 20px;

}

.post-title {
  text-transform: capitalize;
}

.back-btn {
  text-decoration: none;
  color: black;
  font-size: 20px;
}
</style>
