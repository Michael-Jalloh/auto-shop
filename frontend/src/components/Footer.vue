<template lang="html">
  <div>
    <footer class="app-footer">
        <div class="" >
            <div class="logo">
                <img src="../assets/logo.png" alt="">
            </div>
            <div class="text">
                <ul>
                    <li v-for="page in pages.length" :key="page" ><router-link :to="{ name: 'BlogPost', params: {id: pages[ page - 1].id} }" class="link">{{ pages[ page - 1].title}}</router-link></li>
                </ul>
            </div>
        </div>
        <div class="" style="border: 1px solid white; padding: 0px;">
        </div>
        <div class="">
          <p>
            <span>Auto Shop &copy;  {{ date }}</span> <span>Built by Tech Solutions</span>

          </p>
          <p>
              <a  :href="social_media.facebook" target="blank"><icon  name="facebook" scale="1" class="icon"></icon></a>
              <a  :href="social_media.twitter" target="blank"><icon  name="twitter" scale="1" class="icon"></icon></a>
              <a  :href="social_media.instagram" target="blank"><icon  name="instagram" scale="1" class="icon"></icon></a>
          </p>

        </div>
    </footer>
</div>
</template>

<script>
export default {
  name: 'Footer',
  data(){
    return {
      date: '',
      social_media: {
          facebook:'',
          twitter:'',
          instagram:''
      },
      pages: []
    }
  },

  created(){
    var d = new Date();
    this.date = d.getFullYear();
    this.$http.get('/api/v1/get-social-media').then(res =>{
      this.social_media.facebook = res.data['data'].facebook
      this.social_media.twitter = res.data['data'].twitter
      this.social_media.instagram = res.data['data'].instagram
      console.log(res.data['data']['facebook'])

    })
    this.$http.get('/api/v1/pages').then (res => {
        this.pages = res.data['data']
        console.log(this.pages)
    })
  },
    methods: {
        selectPage(page_id) {

          this.$router.push({name: 'BlogPost',params: {id: page_id}});
        }
    }
}
</script>

<style lang="scss" scoped>

.app-footer {
  height: 100%;
  //display: flex;
  //justify-content: center;
  //align-items: center;
  width: 100%;
  background-color: #343A40;
  color: #FFFFFF;
  padding: 0px;
  font-size: 15px;

  div {
      margin: 0 auto;
    display: flex;
    max-width: 900px;
    justify-content: space-between;
    width: 100%;
    align-items: center;
    padding: 10px;

    @include until($tablet){
        flex-direction: column;
        align-items: center;

        p {
            text-align: center;

            span {
                display: block;
                width: 100%;
            }
        }
    };
  }

  p {
      margin-top: 0;
      margin-bottom: 0;
  }

  a {
      color: #ffffff;
  }

  .text {
      p {
          @include until($tablet){
              text-align: left;
          }
      }
  }

}
 .logo {


     img {
         width: 100%;
         height: 100%;
     }
 }
</style>
