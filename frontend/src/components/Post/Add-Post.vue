<template lang="html">
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

</template>

<script>
import { VueEditor } from 'vue2-editor'

export default {

  components: {
    VueEditor
  },

  data(){
    return {
      post : {
        content:'',
        title: '',
        published: false
      }
    }
  },

  methods: {
    handleImageAdded(file, Editor, cursorLocation, resetUploader) {
      var formData = new FormData();
      formData.append('file',file)
      formData.append('title',this.title)
      this.$http.post('/api/v1/upload-post-photo',formData).then( res => {
        console.log(res.data['data']);
          let urls = "http://" + window.host + res.data['data'];
          let url = 'http://localhost:5000/api/v1/get-image/'+ res.data['data'];
          console.log(urls);
          Editor.insertEmbed(cursorLocation, 'image', url);
          resetUploader();
      }).catch( err => {
        console.log(err);
      })
    },

    Save(){
      if (this.post.content && this.post.title ) {
        this.$auth.post('/add-post', this.post).then(res => {
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
          console.log(res);
        })
        return
      }
      this.$notify.error({
        title:'Post',
        message:'Please fill in all the fields'
      })
    },

    Cancel(){
      this.$router.push('/admin-posts');
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
