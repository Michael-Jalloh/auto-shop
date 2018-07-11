<template lang="html">
  <div class="">
    <h2>Blog Posts</h2>
    <hr>
    <div class="flex-container" >
      <el-card class="post-card relative"  v-for="post in posts.length" :key="post" :label="post" style="margin-bottom:10px;">
        <div class="overlay" @click="selectPost(posts[ post - 1])">
          <div class="post-content">
              <img src="posts[post - 1].id"></img>
            <div class="" style="margin: 20px;">
              <h4>{{ posts[post - 1].title }}</h4>
            </div>
          </div>

        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      posts: []
    }
  },

  created(){
    this.$http.get('/api/v1/posts').then(res => {
      this.posts = res.data['data']
      console.log(this.posts)
    })
  },

  methods: {
    selectPost(post) {
      this.$router.push({name: 'BlogPost',params: {id: post.id}});
    }
  },

  computed: {
    getImage(){
      var image_url = "http://localhost:5000/api/v1/post-pic"+this.post.id
      var url = window.host;
      // var image_url = "http://" +url+"/api/v1/post-pic"
      return image_url
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
  }
</style>
