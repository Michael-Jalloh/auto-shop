<template>
  <div>
    <el-header class="header">
      <nav>
        <div class="branding">
          <p>
            Auto Shop
          </p>
        </div>
        <div id="hamburger" v-on:click="active = !active"  v-bind:class="{active:active}">
          <span class="bar1"></span>
          <span class="bar2"></span>
          <span class="bar3"></span>
        </div>
        <ul>
          <li>Login</li>
          <li>
            <el-input v-model="search_input" placeholder="Search">
            </el-input>
          </li>
        </ul>
      </nav>
    </el-header>
  </div>
</template>

<script>
export default {
  name: 'Header',

  data(){
    return {
      search_input: '',
      active: false,
    }
  }
}
</script>

<style lang="scss">

.header {
  padding: 20px;
  background-color: #343A40;
  color: #FFFFFF;

  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 11px;

    ul {
      display: flex;
      list-style: none;
      align-items: center;

      li {
        margin: 0 20px;
      }
    }
  }
}


</style>
