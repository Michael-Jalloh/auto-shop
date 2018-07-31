<template>
  <div id="">
     <p>
         <a @click="prev" href="#">Previous</a> || <a href="#" @click="next">Next</a>
     </p>

     <div class="" style="height:500px; max-height:500px; border: 1px solid;">
         <transistion-group name="fade" tag="div">
             <div class="" v-for="number in [currentNumber]"
                :key="number">
                 <img style="height: 100%; object-fit:contain;" :src="currentImage" alt=""
                 v-on:mouseover="stopRotation"
                 v-on:mouseout="startRotation"/>
             </div>
         </transistion-group>
     </div>
     <div class="">
        <el-upload
        :action="upload_url"
        :auto-upload="false"
        ref="upload"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :on-change="onChange"
        list-type="picture"
        multiple>
        <el-button slot="trigger" size="small" type="primary">Click to upload</el-button>
        <el-button size="small" style="margin-left:10px;" type="success" @click="send">Send to server</el-button>
        </el-upload>

     </div>
  </div>
</template>
<script>
export default {
    name: "",
    data() {
        return {
          images: ['http://i.imgur.com/vYdoAKu.jpg', 'http://i.imgur.com/PUD9HQL.jpg', 'http://i.imgur.com/Lfv18Sb.jpg', 'http://i.imgur.com/tmVJtna.jpg', 'http://i.imgur.com/ZfFAkWZ.jpg'],
          currentNumber: 0,
          timer: null,
          fileData: []
        }
    },

    created(){
        var url = "127.0.0.1:5500";
        this.upload_url = 'http://' + url + '/api/v1/upload-photo-test';
    },

    mounted(){
        this.startRotation();
    },
    methods: {
          startRotation(){
              this.timer = setInterval(this.next, 3000)
          },

          stopRotation(){
              clearTimeout(this.timer);
              this.timer = null
          },

          next(){
              this.currentNumber += 1
          },
          prev(){
              this.currentNumber -= 1
          },
          send(){

              console.log("File Data");
              let that = this
              this.fileData.forEach(function(file){
                  console.log(file)
                  var formData = new FormData();
                  formData.append('file',file.raw);
                  that.$http.post('http://127.0.0.1:5500/api/v1/upload-photo-test', formData)
              })

              //this.$http.post('http://127.0.0.1:5500/api/v1/upload-photo-test', formData)
             //this.$refs.upload.submit();
          },
        handleRemove(file, fileList) {
            console.log(file, fileList);
            },
        handlePreview(file) {
                console.log(file);
            },
        onChange(file, fileList){

            this.fileData.push(file)

        }
      },
      computed: {
          currentImage(){
              return this.images[Math.abs(this.currentNumber) % this.images.length]
          }
  }
}
</script>
<style lang="scss">
    .fade-enter-active, .fade-leave-active {
    transition: all 0.8s ease;
    overflow: hidden;
    visibility: visible;
    opacity: 1;
    position: absolute;
    }
    .fade-enter, .fade-leave-to {
    opacity: 0;
    visibility: hidden;
    }
</style>
