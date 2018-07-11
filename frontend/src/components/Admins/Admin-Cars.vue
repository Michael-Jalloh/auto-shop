<template lang="html">
  <div class="">
    <el-button @click="Refresh">Refresh</el-button>
    <el-table
        :data="carData"
        style="width: 100%"
        :row-class-name="FlagCar">
        <el-table-column
            prop="name"
            label="Name">
        </el-table-column>
        <el-table-column
            prop="owner.username"
            label="Owner"
            width="150">
        </el-table-column>
        <el-table-column
            label="Published"
            width="150">
            <template slot-scope="scope">
              <el-checkbox v-model="scope.row.published"  @change="published_check(scope.row)"></el-checkbox>
            </template>
        </el-table-column>
        <el-table-column
            label="Featured"
            width="150">
            <template slot-scope="scope">
              <el-checkbox @change="feature_check(scope.row)" v-model="scope.row.featured"></el-checkbox>
            </template>
        </el-table-column>
        <el-table-column
            fixed="right"
            label="Operations"
            width="150">
            <template slot-scope="scope">
              <el-button type="text" @click="View(scope.row)">View</el-button>
              <el-button type="text" @click="Delete(scope.row)">Delete</el-button>
            </template>
        </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data(){
    return {
      carData: []

    }
  },

  created(){
    this.$auth.get('/admin-cars').then( res => {
      if (res.data['status'] == 'success') {
        this.carData = res.data['data'];
        console.log(this.carData);
      }
    })
  },


  methods: {
    View(car){
      console.log(car);
    },

    Delete(car){
      var carIndex = this.carData.indexOf(car);
      this.$auth.delete('/admin-delete-car/'+ carIndex).then( res => {
        if (res.data['status'] == 'success') {
          this.carData.splice(carIndex,1);
          this.$notify.success({
            title:'Deletion',
            message:res.data['message']
          })
        }
      })

      console.log(carIndex)
    },

    FlagCar({row, rowIndex}){
      if (row.flagged == true) {
        return "flag-car"
      } else {
        return '';
      }
    },

    feature_check(car){
       var formData = {
         featured: car.featured,
         car_id: car.car_id
       }
      this.$auth.post('/featured', formData).then( res => {
        this.$notify.success({
          title: 'Featured',
          message: res.data['message']
        })
      }).catch ( res => {
        console.log(res.response)
      })

    },

    published_check(car){
       var formData = {
         published: car.published,
         car_id: car.car_id
       }
      this.$auth.post('/published', formData).then( res => {
        this.$notify.success({
          title: 'Published',
          message: res.data['message']
        })
      }).catch ( res => {
        console.log(res.response)
      })

    },

    Refresh(){
      this.$auth.get('/admin-cars').then( res => {
        if (res.data['status'] == 'success') {
          this.carData = res.data['data'];
          console.log(this.carData);
        }
      })
    },

    View(car){
      this.$router.push({name:'AdminViewCar', params: {id: car.car_id}})

    }
  }

}
</script>

<style lang="scss">
.el-table .flag-car {
   background: oldlace;
 }
</style>
