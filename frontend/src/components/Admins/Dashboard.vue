<template lang="html">
  <div class="">
    <div class="flex-container">
      <el-card class="card">
        <h3>Ads</h3>
        <div class="img-container">
          <p>Left Ads</p>
          <el-upload
            action="http://127.0.0.1:5000/api/v1/ads-images/"
            :show-file-list="false"
            :on-change="onChanged"
            :auto-upload="false">
            <img v-show="ads_left_url" :src="ads_left_url" alt="">
            <el-button slot="trigger" size="small" type="primary">click to upload</el-button>
          </el-upload>
        </div>
      </el-card>
      <el-card class="card">
        <h3>Analytics</h3>
      </el-card>
      <el-card class="card">
          <h3>Social Media</h3>
          <div class="">
              <div class="social-media-container">
                  <h4>FaceBook:</h4>
                  <el-input v-model="social_media.facebook"></el-input>
              </div>
              <div class="social-media-container">
                  <h4>Twitter:</h4>
                  <el-input v-model="social_media.twitter"></el-input>
              </div>
              <div class="social-media-container">
                  <h4>Instagram:</h4>
                  <el-input v-model="social_media.instagram"></el-input>
              </div>
              <el-button type="primary" @click="socialMedia">Save</el-button>
          </div>
      </el-card>
      <el-card class="card">
      </el-card>
      <el-card class="card">
      </el-card>
      <el-card class="card">
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      ads_left: '',
      ads_left_url: '',
      social_media: {
          facebook:'',
          twitter: '',
          instagram: ''
      }
    }
  },

  created(){
    this.$auth.get('/ads-images').then(res =>{
      this.ads_left = res.data['data'][0]
      console.log(this.ads_left)
     //this.ads_left_url = 'http://127.0.0.1:5000/api/v1/get-image/'+res.data['data'][0].value
      this.ads_left_url = 'http://'+ window.location.host+'/api/v1/get-image/'+res.data['data'][0].value
    })
    this.$auth.get('/social-media').then(res =>{
      this.social_media.facebook = res.data['data'].facebook
      this.social_media.twitter = res.data['data'].twitter
      this.social_media.instagram = res.data['data'].instagram
      console.log(res.data['data']['facebook'])

    })

  },

  methods: {
    onChanged(file, fileList){
      this.ads_left_url = URL.createObjectURL(file.raw)
      var formData = new FormData();
      formData.append('ads-name','ads-left')
      formData.append('file',file.raw)
      this.$auth.post('/ads-images', formData).then(res => {
        console.log(res)
      })

  },

  socialMedia(){
      console.log('**')
      console.log(this.social_media)
      console.log('**')

      this.$auth.post('/social-media', this.social_media).then(res =>{
        this.$notify.success({
            title:'Social Media',
            message: 'Links updated'
        })
      })
  }

  }
}
</script>

<style lang="scss">
.card {
  width: 47%;
  margin: 10px;

  @include until($large-tablet){
    width: 100%;
  }

  .img-container {
    height: 350px;

    img {
      width: auto;
      height: auto;
    }
  }

  .social-media-container {
      display: flex;
      align-items: center;
      justify-content: space-between;

      .el-input{
          width: 80%;
      }
  }
}
</style>
