<template lang="html">
  <div class="flex-container">
    <div class="grid-md-8 mb-10">

      <div class="">
        <el-tabs  class="relative" type="border-card">
          <el-tab-pane label="Image" >
            <div class="tab">
              <p style="font-style:bold;">{{ car.name }}</p>
              <my-img v-bind:image_url="id">
              </my-img>
            </div>
          </el-tab-pane>

          <el-tab-pane label="Specification">
            <div class="tab">
              <el-table
                class="car-table"
                :data="carTable(car)"
                style="width: 100%"
                >
                <el-table-column
                prop="label"
                label=""
                >
                </el-table-column>

                <el-table-column
                prop="value"
                label=""
                >
                </el-table-column>
              </el-table>
            </div>
          </el-tab-pane>
          <el-tab-pane label="Description">
            <div class="tab">
                <p>{{ car.description}}</p>
            </div>
          </el-tab-pane>
        </el-tabs>


      </div>
    </div>
    <div class="grid-md-4 mb-10 mt-10">
      <el-card class="box-card">
        <div class="">
          <div class="">
            <p>{{ owner.username}}</p>
              <el-button @click="ViewProfile">View Profile</el-button>
          </div>
        </div>

        <el-button @click="flagDialog=true" style="margin-top:10px;">Flag</el-button>
      </el-card>
    </div>
    <el-dialog
      title="Flag"
      :visible.sync="flagDialog"
      width="50%">
      <p>Please enter your reason for flagging this car please</p>
      <el-input placeholder="Email" v-model="flagForm.flagger" style="margin-bottom:10px;"></el-input>
      <el-input type="textarea" :rows="4" v-model="flagForm.flag_reason" placeholder="Reason"></el-input>
      <div class="" style="margin-top:10px;">
        <el-button type="primary" @click="flag">Flag</el-button>
        <el-button type="danger" @click="flagDialog=false">Cancel</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>

import { bus } from '../../main';
import Image from '../Image.vue';

export default {

  components: {
    'my-img': Image,
  },

  data(){
    return {
      id: this.$route.params.id,
      car: {},
      image:'image',
      owner: {
        username:'',
        location: ''
        },
      profile_url: '',
      flagForm: {
        flagger: '',
        flag_reason: '',
        car_id: ''
      },
      flagDialog: false

    }
  },

  created(){
    var url = window.location.host
    console.log(this.$route.params.id);
    this.$http.get('/api/v1/get-car/'+this.$route.params.id).then( res => {
        this.car = res.data['data'];
        this.owner  = this.car.owner;
        console.log(res.data);
        //this.profile_url = "http://localhost:5000/api/v1/get-profile-pic/"+this.car.owner.id
        this.profile_url = "http://" + url + "/api/v1/get-profile-pic/"+this.car.owner.id
        console.log(url)
        console.log(this.car.owner.id)
        console.log(this.profile_url);
    }).catch( res => {
      console.log(res.response);
    })

    console.log("Created")




  },

  methods: {
    carTable(car){
      return [
        {
          label: "Brand",
          value: car.brand
        },
        {
          label: "Model",
          value: car.model
        },
        {
          label: "Price",
          value: 'D'+car.price
        },
        {
          label: "Year",
          value: car.year
        },
        {
          label: "Transmission",
          value: car.transmission
        },
        {
          label: 'Engine',
          value: car.engine + ' Cylinder'
        },
        {
          label: 'Mileage',
          value: car.mileage
        },
        {
          label: 'Type',
          value: this.capitalize(car.type)
        },
        {
          label: 'Fuel',
          value: car.fuel
        },
        {
          label: 'Drive Train',
          value: car.drive_train+'WD'
        }
      ]
    },

    Edit() {
      this.$store.commit('setCar',this.car);
      this.$router.push({name: 'Edit-Car'});
    },

    capitalize(string=""){
      return string.charAt(0).toUpperCase() + string.slice(1);
    },

    flag() {
      this.flagForm.car_id = this.car.car_id
      if (this.flagForm.flag_reason == '' || this.flagForm.flagger == '') {
        this.$notify.error({
          title:'Error',
          message: 'Please fill in your reason'
        })
        return
      }
      this.$http.post('/api/v1/flag/', this.flagForm).then(res => {
        if (res.data['status'] == 'success') {
          this.$notify.success({
            title: "Flag Report",
            message: "You have raise a flag report for "+ this.car.name+".\nYou will be contact for more details"
          })
        } else {
          this.$notify.error({
            title: "Flag Report",
            message: res.data['message']
          })
        }
      })
    this.flagDialog = false
    },

    ViewProfile(){
      this.$router.push({name:"UserProfile", params:{id:this.car.owner.id}})
    }
  }

}
</script>

<style lang="scss">
.car-table {
  table {
      tbody {
        tr {
          td {
            &:nth-child(2){
              text-align: right;
          }
          }
        }
      }
  }
}

.ab-btn {
  position: absolute;
  right: 32px;
  top: 5px;
  font-size: 15px;
  z-index: 100;
}

.tab {
  max-height: 550px;
  min-height: 400px;
  overflow-y: auto;
}

.profile-img {
  width: 250px;
  height: 250px;
  border: 1px solid;
  border-radius: 50%;
  margin: 0 auto;
  overflow: hidden;
}
</style>
