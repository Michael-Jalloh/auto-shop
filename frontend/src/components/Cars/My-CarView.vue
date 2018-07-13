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
    }
  },

  created(){
    ///console.log(this.$route.params.id);
    this.$http.get('/api/v1/get-car/'+this.$route.params.id).then( res => {
        this.car = res.data['data'];
    }).catch( res => {
      console.log(res.data);
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
      this.$notify.success({
        title: "Flag Report",
        message: "You have raise a flag report for "+ this.car.name+".\nYou will be contact for more details"
      })
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
