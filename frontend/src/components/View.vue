<template>
  <div id="app">
    <app-header></app-header>
    <div class="main-container">
      <aside class="aside">
        <img :src="ads_left_url" alt="">
      </aside>
        <main>
            <router-view/>
        </main>
    </div>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
  name: 'App',

  components: {
    'app-header': Header,
    'app-footer': Footer
  },
  data() {
      return {
          left_ads: {},
          ads_left_url: ''
      }
  },

  created(){
    this.$http.get('/api/v1/get-ads').then( res => {
        this.left_ads = res.data['data']
        this.ads_left_url = this.$store.getters.url +'/api/v1/get-image/'+this.left_ads.value
    })
    if (this.$route.path == "/") {
      this.$router.push({path: '/view-cars'})
    }
    //
  }
}
</script>

<style lang="scss">

body {
  margin: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100vh;
}

.main-container {
 // height: calc(100vh - 120px);
  //overflow-y: scroll;
  display: flex;

  @include until($large-mobile){
    flex-direction: column;
    //margin-bottom: 50px;
  }

}

main{
  //max-width: 1200px;
  flex: 1;
  padding: 20px 10px 20px;
}

.aside {
  max-width: 300px;
  flex: 1;
  //background-color: crimson;
  padding: 10px;
  height: 100%;
  img {
      width: 100%;
  }
}

</style>
