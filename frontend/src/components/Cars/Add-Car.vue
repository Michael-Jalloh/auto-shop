<template lang="html">
  <div class="two-column">
    <div class="grid-md-2">
      <el-form ref="form" :model="form" label-width="120px">
        <el-form-item label="Name">
          <el-input v-model="form.name"></el-input>
        </el-form-item>
      </el-form>
    </div>
    <div class="grid-md-2">

    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      form: {
        name: ''
      }
    };
  }
}
</script>

<style lang="css">

.two-column {
  display: flex;
}
</style>
