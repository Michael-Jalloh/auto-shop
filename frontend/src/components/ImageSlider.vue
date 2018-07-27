<template>
  <div id="">
     <p>
         <a @click="prev" href="#">Previous</a> || <a href="#" @click="next">Next</a>
     </p>

     <transistion-group name="fade" tag="div">
         <div class="" v-for="number in [currentNumber]"
            :key="number">
             <img :src="currentImage" alt=""
             v-on:mouseover="stopRotation"
             v-on:mouseout="startRotation"/>
         </div>
     </transistion-group>
  </div>
</template>
<script>
export default {
    name: "",
    data() {
        return {
          images: ['http://i.imgur.com/vYdoAKu.jpg', 'http://i.imgur.com/PUD9HQL.jpg', 'http://i.imgur.com/Lfv18Sb.jpg', 'http://i.imgur.com/tmVJtna.jpg', 'http://i.imgur.com/ZfFAkWZ.jpg'],
          currentNumber: 0,
          timer: null
        }
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
