<template lang="html">
  <div class="">
    <el-card class="box-card">
      <div class="" style="display:flex;">
        <div class="">
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
        </div>
        <div class="" style="width: 100%;">
          <div class="flex-container">
            <h4>Username</h4>
            <el-input placeholder="Username" v-model="user.username"></el-input>
          </div>
          <div class="flex-container">
            <h4>Email</h4>
            <el-input placeholder="Email" v-model="user.email"></el-input>
          </div>
          <div class="flex-container">
            <h4>Password</h4>
            <el-input placeholder="Password" type="password" v-model="user.password"></el-input>
          </div>
          <div class="flex-container">
            <h4>Comfirm Password</h4>
            <el-input placeholder="Comfirm Password" type="password" v-model="user.comfirm_password" ></el-input>
          </div>
          <div class="flex-container">
            <h4>Location</h4>
            <el-input placeholder="Location" v-model="user.location"></el-input>
          </div>
          <div class="flex-container">
            <h4>Contact</h4>
            <el-input placeholder="Contact" v-model="user.contact"></el-input>
          </div>
          <div class="flex-container">
            <h4>Bio</h4>
            <el-input placeholder="Bio" v-model="user.bio" type="textarea" :rows="5"></el-input>
          </div>




            <el-button class="mt-10" @click="submit">Save Profile</el-button>
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
    //this.upload_url = 'http://' + this.url + '/api/v1/upload-photo' // production
    this.upload_url = "http://localhost:5000"+"/api/v1/upload-profile" // dev

    //this.imageUrl = this.url+"/api/v1/get-profile-pic/"+this.user.id // production
    this.imageUrl = "http://localhost:5000/api/v1/get-profile-pic/"+this.user.id

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
      this.fileData.user_id = this.user.id;
      this.$refs.upload.submit();
    },

    submit(){
      this.$auth.post('/api/v1/edit-profile',this.user).then(res => {
      this.$notify.success({
          title:'Profile',
          message: res.data['message']
      });
      this.$store.commit('setUser', res.data['data']);
      this.$router.push('/my-profile');
      console.log(res.data['data']);
      })
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
}

.flex-container {
  display: flex;
  justify-content: space-between;
  align-items: center;

  .el-input, .el-textarea {
    width: 70%;
  }

  .mt-10 {
    margin-top: 10px;
  }
}
</style>
