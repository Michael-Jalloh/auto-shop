<template lang="html">
  <el-card class="car-card" v-show="show">
    <div class="">

        <div class="">
          <img class="img" :src="image_url" alt="">
        </div>
        <div class="" style="margin: 20px 0px;">
          {{ car.name }}
        </div>


      <div class="">
        <el-button @click="Edit(car)">Edit</el-button>
        <el-button type="primary" @click="View(car)" >View</el-button>
        <el-button type="danger" @click="Confirm_Delete" >Delete</el-button>
      </div>
    </div>
    <el-dialog
          title="Deletion"
          :visible.sync="dialogVisible"
          width="30%">
          <span>Do you want to delete this {{ car.name}}</span>
          <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">Cancel</el-button>
            <el-button type="primary" @click="Delete">Confirm</el-button>
          </span>
    </el-dialog>
  </el-card>
</template>

<script>
import { bus } from '../../main'
export default {
  props: ['car'],

  data(){
    return {
      image_url: '',
      show: true,
      dialogVisible: false
    }
  },

  created(){

    var url = this.$store.getters.url;
    //this.image_url = 'http://localhost:5000/api/v1/get-image-by-id/'+ this.car.car_id; // dev
    this.image_url = url + "/api/v1/get-image-by-id/" + this.car.car_id; // production
  },

  methods: {
    Edit(car) {
      this.$store.commit('setCar',car);
      this.$router.push({name: 'Edit-Car'});
    },

    Confirm_Delete(){
        this.dialogVisible = true
    },

    Delete(){

      this.$auth.delete('/delete-car/'+this.car.car_id).then( res => {
        console.log(res)
        this.$notify({
          title: "Deletion",
          message: res.data['message'],
          type: res.data['status']
        }),

        this.show = false
      }).catch( res => {
        if (error.response.status == 401) {
          bus.$emit('login')
        } else if (error.response.status == 422) {
          bus.$emit('login')
        }
      })

    },

    View(car){
      console.log(car.car_id);
      this.$router.push('/my-car/'+car.car_id)
    },
  }
}
</script>

<style lang="scss">

.profile-sm {
  .img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
}

.car-card {
  width: 47%;
  margin: 10px;

  @include until($large-tablet){
    width: 100%;
  }

  .details {
    position: absolute;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
    padding: 30px;
    color: #ffffff;
    display: none;
  }

  &:hover {
    .details{
      display: block;
    }
  }
}

.img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

</style>
