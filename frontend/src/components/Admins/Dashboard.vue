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
    }
  },

  created(){
    this.$auth.get('/ads-images').then(res =>{
      this.ads_left = res.data['data'][0]
      this.ads_left_url = 'http://127.0.0.1:5000/api/v1/get-images/'+res.data['data'][0].value
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
      width: 100%;
      height: 100%;
    }
  }
}
</style>
