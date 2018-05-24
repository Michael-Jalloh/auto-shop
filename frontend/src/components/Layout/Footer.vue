<template lang="html">
  <div class="app-footer" >
      Tech Solution &copy;  {{ date }}
    </div>
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
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  background-color: #343A40;
}

</style>
