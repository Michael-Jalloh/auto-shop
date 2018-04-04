<template lang="html">
  <el-container>
    <el-header class="header">
      <div class="" v-on:click="active = false">
        <router-link :to="{ name: 'View-Cars', params: {} }" class="brand-link"> {{ brand }}</router-link>
      </div>
      <div id="hamburger" v-on:click="active = !active"  v-bind:class="{active:active}">
        <span class="bar1"></span>
        <span class="bar2"></span>
        <span class="bar3"></span>
      </div>
      <div id="side-menu" v-bind:class="{active:active}">

        <ul>
          <li><el-input v-model="search_input" placeholder="Search">
          </el-input></li>
          <li v-on:click="active = false"><router-link to="" class="link">Blog</router-link></li>
          <li v-on:click="active = false"><router-link :to="{ name:'Add-Car', params: {} }" class="link" >Add Car</router-link></li>
          <li v-on:click="active = false"><router-link to="" class="link">Luxury Cars</router-link></li>
          <li v-on:click="active = false"><router-link to="" class="link">New Cars</router-link></li>
          <li v-on:click="active = false"><router-link to="" class="link">Old Cars</router-link></li>
          <li v-on:click="active = false"><router-link to="" class="link">Scarp Cars</router-link></li>
          <li class="log-out" v-show="!$auth.isAuthenticated()" v-on:click="active = false"><router-link :to="{ name: 'Login', params: {} }" class="link"><icon class="icon" scale="1.75" name="sign-in" ></icon></router-link></li>
          <li class="log-out" v-show="$auth.isAuthenticated()" v-on:click="logout"><icon class="icon" scale="1.75" name="sign-out" ></icon></li>
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
      this.active = false;
      console.log('Logout');
      this.$auth.logout().then(response=> {
        this.$auth.logoutRefresh();
        this.$auth.destroyTokens();
        this.$router.push('/');
        this.$notify({
          title: 'Logout',
          message: 'You have been logged out',
          type: response.data['status']
        });
        this.$store.commit('setUser',{});
      })
    }
  }

}
</script>


<style lang="scss" scoped>
@import '../layout.scss';

.header {
  background-color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #343A40;
}

.brand {
  width: 250px;
  color: black;
  text-decoration: none;
}

.icon {
  margin: 0 10px;
}
#side-menu {
  display: none;
  align-items: center;

  ul {
    display: flex;
    align-items: center;
    list-style: none;


    flex-direction: column;
    align-items: left;
    padding: 0;


    li {
       margin: 15px;
       width: 100%;
       text-align: center;
    }
  }



  &.active {
    display: flex;
    position: absolute;
    top: 60px;
    height: calc(100vh - 120px);
    background: #FFFFFF;
    left: 0;
    padding: 0;
    flex-direction: column;
    z-index: 999;
    align-items: flex-start;
    transition: .02s display;
    width: 100%;
    align-items: center;
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



  &:hover {
    cursor: pointer;
  }

  .bar1, .bar2, .bar3{
    //background-color: #ffffff;
    position: absolute;
    transition: .5s;
    width: 44%;
    border: 4px solid #252525;
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
  color: #252525;
  text-decoration: none;
  font-weight: bold;
}

.brand-link {
  font-size: 20px;
}

</style>
