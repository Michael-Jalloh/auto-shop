<template lang="html">
  <div class="flex-container">
    <div class="grid-md-2">
      <el-form :ref="myform" :model="form" :rules="rules" label-width="120px">
        <el-form-item label="Name" prop="name">
          <el-input  v-model="form.name" placeholder="Name *"></el-input>
        </el-form-item>
        <el-form-item label="Price" prop="p">
          <el-input v-model="form.price"></el-input>
        </el-form-item>
        <el-form-item label="Description" prop="d">
          <el-input type="textarea" :rows="4" v-model="form.description"></el-input>
        </el-form-item>
        <el-form-item label="Brand" prop="b">
          <el-input v-model="form.brand"></el-input>
        </el-form-item>
        <el-form-item label="Model" prop="m">
          <el-input v-model="form.model"></el-input>
        </el-form-item>
        <el-form-item label="Year" prop="y">
          <el-input v-model="form.year"></el-input>
        </el-form-item>
        <el-form-item label="Transmission" prop="t">
          <el-input v-model="form.transmission"></el-input>
        </el-form-item>
        <el-form-item label="Engine" prop="e">
          <el-input v-model="form.engine"></el-input>
        </el-form-item>
        <el-form-item label="Mileage" prop="m">
          <el-input v-model="form.mileage"></el-input>
        </el-form-item>
        <el-form-item label="Fuel" prop="f">
          <el-input v-model="form.fuel"></el-input>
        </el-form-item>
        <el-form-item label="Drive Train" prop="dr">
          <el-input v-model="form.drive_train"></el-input>
        </el-form-item>
        <el-form-item>
    <el-button type="primary" @click="onSubmit">Save</el-button>
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
        name: '',
        price: '',
        description: '',
        brand: '',
        model: '',
        year: '',
        transmission: '',
        engine: '',
        mileage: '',
        fuel: '',
        drive_train:''
      },
      rules: {
        name: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        p: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        d: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        b: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        m: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        y: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        t: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        e: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        m: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        f: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        dr: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
      }
    };
  },

  methods: {
    onSubmit() {
      console.log(this.refs.myform);
    }
  }
}
</script>

<style lang="scss">
@import '../../layout.scss';


.two-column {
  display: flex;
  flex-flow: row wrap;
}
</style>
