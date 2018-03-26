<template lang="html">
  <div class="flex-container">
    <div class="grid-md-8">
      <el-card class="box-card">
        <my-img v-bind:image_url="car.car_id">
        </my-img>
      </el-card>

      <el-card class="mt-10">
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

  },

  methods: {
    carTable(car){
      return [
        {
          label: "Name",
          value: car.name,
        },
        {
          label: "Price",
          value: 'D'+car.price
        },
        {
          label: "Brand",
          value: car.brand
        },
        {
          label: "Model",
          value: car.model
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
          value: 'V' + car.engine
        },
        {
          label: 'Mileage',
          value: car.mileage
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

</style>
