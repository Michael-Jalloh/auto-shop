<template>
  <div id="app">
    <router-view/>
    <login></login>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import Login from '@/components/Login-view'

export default {
  name: 'App',

  components: {
    'app-header': Header,
    'app-footer': Footer,
    'login': Login
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
  height: calc(100vh - 120px);
  overflow-y: scroll;
  display: flex;

  @include until($large-mobile){
    flex-direction: column;
  }

}

main{
  //max-width: 1200px;
  flex: 1;
  padding: 20px 10px 0;
}

.aside {
  max-width: 200px;
  flex: 1;
  //background-color: crimson;
  padding: 10px;
  height: 100%;
}

.mb-10 {
  margin-bottom: 10px;
}
</style>
