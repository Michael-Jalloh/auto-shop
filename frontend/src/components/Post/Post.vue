<template lang="html">
  <div class="post">
    <h2 class="post-title">{{ post.title}}</h2>
    <div class="" v-html="post.content">

    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      post: {
        content: '',
        title:''
      }
    }
  },

  created(){
    this.$http.get('/api/v1/post/'+this.$route.params.id).then(res => {
      this.post = res.data['data'];
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


</style>
