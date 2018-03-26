<template lang="html">
  <el-container>
    <el-header class="header">
      <div class="">
        <router-link :to="{ name: 'View-Cars', params: {} }" class="brand-link"> {{ brand }}</router-link>
      </div>
      <div id="hamburger" v-on:click="active = !active"  v-bind:class="{active:active}">
        <span class="bar1"></span>
        <span class="bar2"></span>
        <span class="bar3"></span>
      </div>
      <div id="side-menu" v-bind:class="{active:active}">
        <!--<div class="icon">
          <icon name="envelope" scale="1.75"></icon>
        </div> -->
        <ul>
          <li v-on:click="active = false"><router-link to="" class="link">Blog</router-link></li>
          <li v-on:click="active = false"><router-link to="" class="link">About us</router-link></li>
          <li v-on:click="active = false"><router-link :to="{ name:'Add-Car', params: {} }" class="link" >Add Car</router-link></li>
          <li><el-input v-model="search_input" placeholder="Search">
          </el-input></li>
          <li class="log-out" v-on:click="active = !active"><icon class="icon" scale="1.75" name="sign-out" v-on:click="logout()"></icon></li>
          <li></li>
        </ul>
      </div>
    </el-header>

  </el-container>
</template>

<script>

export default {
  name: 'Header',

  components:{
  },

  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      brand: "Auto Shop",
      search_input: '',
      active: false
    }
  },

  methods: {
    logout: function(){
      console.log('Logout');
      this.$auth.logout().then(response=> {
        this.$router.push('/login');
      })
    }
  }

}
</script>


<style lang="scss" scoped>
@import '../layout.scss';

.header {
  background-color: #343A40;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #FFFFFF;
}

.brand {
  width: 250px;
  color: #FFFFFF;
  text-decoration: none;
}

.icon {
  margin: 0 10px;
}
#side-menu {
  display: flex;
  align-items: center;

  ul {
    display: flex;
    align-items: center;
    list-style: none;

    @include until($large-tablet - 1){
      flex-direction: column;
      align-items: left;
      padding: 0;
    }

    li {
       margin: 5px;
    }
  }

  @include until($large-tablet - 1){
    display: none;
  }

  &.active {
    display: flex;
    position: absolute;
    top: 60px;
    height: calc(100vh - 140px);
    background: #343A40;
    left: 0;
    padding: 40px 20px;
    flex-direction: column;
    z-index: 1;
    align-items: flex-start;
    transition: .02s display;
  }

}

#hamburger {
  position: relative;
  width: 44px;
  height: 40px;
  //top: -10px;
  //left: 5px;
  padding: 4px;
  transition: .25s;

  @include at-least($large-tablet){
    display: none;
  }

  &:hover {
    cursor: pointer;
  }

  .bar1, .bar2, .bar3{
    //background-color: #ffffff;
    position: absolute;
    transition: .5s;
    width: 44%;
    border: 4px solid #fff;
    border-bottom: none;
    border-radius: 2px;
    outline: none;
  }

  .bar1 {
    top: 10px;
  }

  .bar2 {
    top: 22px;
  }

  .bar3{
    bottom: 10px;
  }
}

.active {
  .bar1 {
      transform: rotate(45deg) translate(11px,6px);
      transition: .5s;
    }
    .bar2{
      opacity: 0;
      transition: .2s all linear;
    }

    .bar3{
      transform: rotate(-45deg) translate(10px,-6px);
      transition: .5s all linear;
    }
}

.log-out{
  cursor: pointer;
}

.link, .brand-link{
  color: #FFFFFF;
  text-decoration: none;
  font-weight: bold;
}

.brand-link {
  font-size: 20px;
}

</style>
