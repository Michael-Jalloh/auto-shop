<template lang="html">
  <div class="">
    <div class="editor-pane">
      <vue-editor v-model="content"></vue-editor>
    </div>
    <div class="" v-html="content">

    </div>
  </div>

</template>

<script>
import { VueEditor } from 'vue2-editor'
var marked = require('marked')
export default {

  components: {
    VueEditor
  },

  data(){
    return {
      content:''
    }
  },

  computed: {
    markdownText() {
      return marked(this.content, {sanitize: true})
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
}

.editor, .preview {
  border: 1px solid;
  width: 50%;
}

.preview {
  background-color: #eee;
}
</style>
