<template lang="html">
  <el-container>
    <el-footer class="app-footer">
        <div class="">
          <p>
            Auto Shop &copy;  {{ date }}
          </p>
          <p>
            Built by Tech Solutions
          </p>
        </div>
    </el-footer>
  </el-container>
</template>

<script>
export default {
  name: 'Footer',
  data(){
    return {
      date: ''
    }
  },

  created(){
    var d = new Date();
    this.date = d.getFullYear();
  },
    methods: {

    }
}
</script>

<style lang="scss" scoped>

.app-footer {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  background-color: #343A40;
  color: #FFFFFF;

  div {
    display: flex;
    max-width: 900px;
    justify-content: space-between;
    width: 100%;
  }
}

</style>
