<template lang="html">
  <div class="flex-container">
    <div class="">
      <h4>Title</h4>
      <div class="editor-pane">
        <el-input v-model="post.title" placeholder= "Title"></el-input>
      </div>
      <h4>Content</h4>
      <div class="editor-pane">
        <vue-editor v-model="post.content"
          useCustomImageHandler
          @imageAdded="handleImageAdded"
          placeholder="Content"
        ></vue-editor>
      </div>
      <div class="" style="margin-top: 20px;">
        <div class="">
          <el-checkbox v-model='post.published'><h4>Publish</h4></el-checkbox>
        </div>
        <el-button type="success" @click="Save">Save</el-button>
        <el-button type="danger" @click="Cancel">Cancel</el-button>
      </div>
    </div>
    <div class="" style="margin-left:10px; max-width: 300px;">
      <h4>Feature Image</h4>
      <el-upload
        class="avatar-uploader"
        :action="upload_url"
        :show-file-list="false"
        :on-change="onChanged"
        :auto-upload="false"
        ref="upload"
        :on-success="handleAvatarSuccess">
        <el-button>Select File</el-button>
      </el-upload>
      <div class="mt-10" style="">
        <img v-if="post.image_url" :src="post.image_url" class="avatar" style="width:100%;">
      </div>
    </div>
  </div>

</template>

<script>
import { bus } from '../../main'
import { VueEditor } from 'vue2-editor'

export default {

  components: {
    VueEditor
  },

  data(){
    return {
      have_photo: false,
      post : {
        content:'',
        title: '',
        published: false,
        image_url: ''
      },
      form: new FormData(),
      post_id: ''
    }
  },

  created(){
    this.upload_url = 'http://' + window.location.host + '/api/v1/upload-photo' // production
    //this.upload_url = "http://localhost:5000"+"/api/v1/photo-test" // dev
    },

  methods: {
    handleImageAdded(file, Editor, cursorLocation, resetUploader) {
      var formData = new FormData();
      formData.append('file',file)
      formData.append('title',this.post.title)
      formData.append('id', this.post_id)
      console.log(this.post_id)
      this.$http.post('/api/v1/upload-post-photo',formData).then( res => {
        console.log(res.data['data']);
        let url = "http://" + window.location.host + "/api/v1/get-image/" + res.data['data'];
         //let url = 'http://localhost:5000/api/v1/get-image/'+ res.data['data'];
          console.log(url);
          this.post_id = res.data['post_id']
          console.log("<Post></Post>")
          console.log(this.post_id)
          Editor.insertEmbed(cursorLocation, 'image', url);
          resetUploader();
      }).catch( err => {
        console.log(err);
      })
    },

    Save(){
      if (this.have_photo) {
        if (this.post.content && this.post.title ) {
          this.form.append('content', this.post.content)
          this.form.append('title', this.post.title)
          this.form.append('published', this.post.published)
          this.form.append('id', this.post_id)
          console.log("Save")
          console.log(this.post_id)
          this.$auth.post('/add-post', this.form).then(res => {
            if (res.data['status']=='success') {
              this.$notify.success({
                title: 'Post',
                message: 'Post save'
              })
              this.$router.push('/admin-posts')
              return;
            }
            this.$notify.error({
              title: 'Post',
              message:'Error Occurred'
            })
            return;
          }).catch( res =>{
            if(res.response.status == 422){
              bus.$emit('login');
            };
          })
          return
        }
        this.$notify.error({
          title:'Post',
          message:'Please fill in all the fields'
        })
      }
    },

    Cancel(){
      this.$router.push('/admin-posts');
    },
    beforeAvatarUpload(file) {
      this.post.image_url = URL.createObjectURL(file.raw);
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('Avatar picture must be JPG format!');
      }
      if (!isLt2M) {
        this.$message.error('Avatar picture size can not exceed 2MB!');
      }
      return isJPG && isLt2M;
    },

    onChanged(file,fileList){
      this.post.image_url = URL.createObjectURL(file.raw);
      //this.form.file = file.raw;
      this.form.append('file', file.raw)
      this.form.append('pic_name',file.name)
      this.have_photo = true;
      //this.$auth.post('/photo-test', formData).then(res => {
        //console.log(res.data)
    //  })
      //this.fileData.car_id = this.car.car_id
      //this.$refs.upload.submit();
    },
    handleAvatarSuccess(res, file){

    }
  },

  computed: {
    markdownText() {
      return marked(this.post.content, {sanitize: true})
    }
  }
}
</script>

<style lang="scss">
.editor-pane {
  max-height: 500px;
  border: 2px solid;
  overflow-y: auto;
  //display: flex;
  max-width: 900px;

  .ql-editor {
    height: 400px;
  }

  input {
    border: none;
  }
}

.ql-blank {
  content: "Content";
}

.editor, .preview {
  border: 1px solid;
  width: 50%;
}

.preview {
  background-color: #eee;
}
</style>
