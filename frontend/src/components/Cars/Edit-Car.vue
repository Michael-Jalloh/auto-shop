<template lang="html">
  <div class="flex-container">
    <div class="grid-md-8">
      <el-card class="box-card relative">
        <div class="" slot="header">
          <span>{{ car.name }}</span>
          <el-button  class="btn" v-show=" owner && $can.delete(owner,car)" @click="" type="text">Delete</el-button>
        </div>
        <div class="">
          <el-button  class="" v-show=" owner && $can.delete(owner,car)" @click="" type="text">View</el-button>
        </div>
        <my-img v-bind:image_url="car.car_id">
        </my-img>
      </el-card>
      <el-card class="mt-10">
        <div class="edit-car-fields" v-for="item in info.length ">
          <span>{{ info[item - 1].label }}</span>
          <span><el-input v-model:value="info[item - 1].value"></el-input></span>
        </div>
        <div class="mt-10">
          <el-button @click="Save">Save</el-button>
        </div>
      </el-card>
    </div>
    <div class="grid-md-4 ">
      <el-card class="box-card">
      </el-card>
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
      car: {},
      image:'image',

    }
  },

  created(){
    this.car = this.$store.getters.car;
    this.owner = this.$store.getters.user;
    this.info = [
      {
        label: "Name",
        value: this.car.name
      },
      {
        label: "Brand",
        value: this.car.brand
      },
      {
        label: "Model",
        value: this.car.model
      },
      {
        label: "Price",
        value: this.car.price
      },
      {
        label: "Year",
        value: this.car.year
      },
      {
        label: "Transmission",
        value: this.car.transmission
      },
      {
        label: 'Engine',
        value: this.car.engine
      },
      {
        label: 'Mileage',
        value: this.car.mileage
      },
      {
        label: 'Fuel',
        value: this.car.fuel
      },
      {
        label: 'Drive Train',
        value: this.car.drive_train
      }
    ]
  },

  methods: {

    Edit() {
      this.$store.commit('setCar',this.car);
      this.$router.push({name: 'Edit-Car'});
    },

    Info2Car() {
      this.car.name = this.info[0].value;
      this.car.brand = this.info[1].value;
      this.car.model = this.info[2].value;
      this.car.price = this.info[3].value;
      this.car.year = this.info[4].value;
      this.car.transmission = this.info[5].value;
      this.car.engine = this.info[6].value;
      this.car.mileage = this.info[7].value;
      this.car.fuel = this.info[8].value;
      this.car.drive_train = this.info[9].value;
    },

    Save(){
      this.Info2Car();
      console.log(this.car);
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

.btn {
  position: absolute;
  right: 32px;
  top: 5px;
  font-size: 20px;
}

.edit-car-fields {
  display: flex;
  justify-content: space-between;
  padding: 20px 0;
  border-bottom: 1px solid #ebeef5;
  flex-flow: row wrap;

  &:hover{
    background-color: #F5F7FA;
  }


  @include until($large-mobile){
    span {
      &:nth-child(2){
        width: 100%;
        margin-top: 15px;
      }
    }
  }
}

</style>
