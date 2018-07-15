<template lang="html">
  <div class="">
    <h2>Blog Posts</h2>
    <hr>
    <div class="flex-container" >
      <post-card v-for="post in posts.length" :key="post" v-bind:post="posts[post -1]"></post-card>
    </div>
  </div>
</template>

<script>
import  PostCard  from './PostCard'
export default {

  components: {
    'post-card': PostCard
  },

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

  }
}
</script>

<style lang="scss">


</style>
