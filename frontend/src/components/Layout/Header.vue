<template lang="html">
  <el-container>
    <el-header class="header user">
      <div class="">
        <router-link :to="{ name: 'ViewCars', params: {} }" class="brand-link"> {{ brand }}</router-link>
      </div>
      <div id="hamburger" v-on:click="active = !active"  v-bind:class="{active:active}">
        <span class="bar1"></span>
        <span class="bar2"></span>
        <span class="bar3"></span>
      </div>
      <div id="side-menu" v-bind:class="{active:active}">
        <div class="icon">
          <icon name="envelope" scale="1.75"></icon>
        </div>
        <div class="icon">
          <icon name="bell" scale="1.75"></icon>
        </div>
          <div class="log-out" v-on:click="logout()">
            <icon class="icon" scale="1.75" name="sign-out" v-on:click="logout()"></icon>
          </div>
      </div>
    </el-header>

    <el-dialog
      title="Login"
      :visible.sync="loginVisible"
      width="30%"
      center>
      <el-input placeholder="Username" v-model="user"></el-input>
      <el-input placeholder="Password" type="password" v-model="password"></el-input>
    </el-dialog>
  </el-container>
</template>

<script>


export default {
  name: 'Header',

  components:{
  },

  data () {
    return {
      brand: "Auto Shop",
      search_input: '',
      active: false,
      loginVisible: false,
      user: "",
      password: ""
    }
  },

  methods: {
    logout: function(){
      console.log('Logout');
      this.$auth.logout().then(response=> {
        this.$auth.destroyTokens();
        this.$router.push('/view-cars');
      })
    }
  }

}
</script>


<style lang="scss" scopde>
@import '../../variable.scss';
@import '../../mixins.scss';
@import '../../main.scss';

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

.user {
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
