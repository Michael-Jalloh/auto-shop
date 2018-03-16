<template lang="html">
  <div class="flex-container">
    <div class="grid-md-2">
      <el-form  :model="form" :rules="rules" label-width="120px">
        <el-form-item label="Name" prop="name">
          <el-input  v-model="form.name" placeholder="Name *"></el-input>
        </el-form-item>
        <el-form-item label="Price" prop="price">
          <el-input v-model="form.price"></el-input>
        </el-form-item>
        <el-form-item label="Description" prop="description">
          <el-input type="textarea" :rows="4" v-model="form.description"></el-input>
        </el-form-item>
        <el-form-item label="Brand" prop="brand">
          <el-input v-model="form.brand"></el-input>
        </el-form-item>
        <el-form-item label="Model" prop="model">
          <el-input v-model="form.model"></el-input>
        </el-form-item>
        <el-form-item label="Year" prop="year">
          <el-input v-model="form.year"></el-input>
        </el-form-item>
        <el-form-item label="Transmission" prop="transmission">
          <el-input v-model="form.transmission"></el-input>
        </el-form-item>
        <el-form-item label="Engine" prop="engine">
          <el-input v-model="form.engine"></el-input>
        </el-form-item>
        <el-form-item label="Mileage" prop="mileage">
          <el-input v-model="form.mileage"></el-input>
        </el-form-item>
        <el-form-item label="Fuel" prop="fuel">
          <el-input v-model="form.fuel"></el-input>
        </el-form-item>
        <el-form-item label="Drive Train" prop="drive_train">
          <el-input v-model="form.drive_train"></el-input>
        </el-form-item>
        <el-form-item>
    <el-button type="primary" @click="onSubmit">Save</el-button>
  </el-form-item>
      </el-form>
    </div>
    <div class="grid-md-2">
      <h3>Featured Image</h3>

      <el-upload
        class="avatar-uploader"
        action="http://localhost:5000/api/v1/upload-car-photo"
        :show-file-list="false"
        :on-success="handleAvatarSuccess">
        <img v-if="imageUrl" :src="imageUrl" class="avatar">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
</el-upload>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      imageUrl: '',
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
        price: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        description: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        brand: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        model: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        year: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        transmission: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        engine: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        mileage: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        fuel: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
        drive_train: [
          {required:true, message:'This field is required', trigger:'changed|blur'}
        ],
      }
    };
  },

  methods: {
    onSubmit() {
      console.log(this.form);
      this.$http.post('/test-car', this.form).then(res => {
        this.$notify({
              title:'Car',
              message: res.data['message'],
              type: res.data['status']
        });
      })
    },

    handleAvatarSuccess(res, file) {
      console.log(res);
        this.imageUrl = URL.createObjectURL(file.raw);
      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('Avatar picture must be JPG format!');
        }
        if (!isLt2M) {
          this.$message.error('Avatar picture size can not exceed 2MB!');
        }
        return isJPG && isLt2M;
      }
    }

}
</script>

<style lang="scss">
@import '../../layout.scss';

.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }

</style>
