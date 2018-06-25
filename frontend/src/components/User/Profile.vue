<template lang="html">
  <div class="profile">
    <el-card class="box-card">
      <div class="flex-container">
        <!--<div class="">
          <div class="profile-img">
            <img :src="imageUrl" alt="">
          </div>
          <el-upload
            :action="upload_url"
            :show-file-list="false"
            :auto-upload="false"
            :on-change="onChanged"
            ref="upload"
            :data="fileData"
            :on-success="handleAvatarSuccess"
            >
            <el-button size="small" type="primary">Click to upload</el-button>
          </el-upload>
        </div> -->
        <div class="">
            <h2>{{ user.username}}</h2>
            <h4>{{ user.email}}</h4>
            <h4>{{ user.contact }}</h4>

            <el-button @click="EditProfile">Edit Profile</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {

  components: {
    'my-img': Image,
  },

  data(){
    return {
      url:'',
      user: {},
      cars: [],
      imageUrl: '',
      fileData: {
        user_id:'',
      }
    }
  },

  created() {
    this.user = this.$store.getters.user;
    this.url = window.location.hostname+':'+window.location.port;
    this.upload_url = 'http://' + this.url + '/api/v1/upload-profile' // production
    //this.upload_url = "http://localhost:5000"+"/api/v1/upload-profile" // dev

    this.imageUrl = "http://"+this.url+"/api/v1/get-profile-pic/"+this.user.id // production
    //this.imageUrl = "http://localhost:5000/api/v1/get-profile-pic/"+this.user.id

  },

  methods: {
    handleAvatarSuccess(res,file){
      console.log("[*] Success");
      console.log(file);
      console.log(res.data);

      this.imageUrl=URL.createObjectURL(file.raw);

      //this.imageUrl = this.url+"/api/v1/get-profile-pic/"+this.user.id // production
      //this.imageUrl = "http://localhost:5000/api/v1/get-profile-pic/"+this.user.id
    },

    onChanged(file, fileList){
      console.log("File");
      console.log(file);
      console.log("fileList");
      console.log(fileList);
      this.fileData.user_id = this.user.id;
      this.$refs.upload.submit();
    },

    EditProfile(){
      this.$router.push({name: 'EditProfile'})
    }
  }
}
</script>

<style lang="scss">
.profile-img {
  width: 250px;
  height: 250px;
  min-width: 250px;
  border: 1px solid;
  border-radius: 50%;
  margin-right: 50px;
  overflow: hidden;

  @include until($large-tablet - 1) {
    width: 225px;
  }
}
</style>
