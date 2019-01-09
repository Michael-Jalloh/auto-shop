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
              <el-button type="text" @click="Edit(scope.row)">Edit</el-button>
              <el-button type="text" @click="Confirm_Delete(scope.row)">Delete</el-button>
            </template>
        </el-table-column>
    </el-table>
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
  </div>
</template>

<script>
import  { bus } from '../../main'

export default {
  data(){
    return {
      carData: [],
      car: {},
      dialogVisible: false

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

    Confirm_Delete(car){
        this.car = car
        this.dialogVisible = true
    },
    Delete(){
        this.dialogVisible = false
      var carIndex = this.carData.indexOf(this.car);
      this.$auth.delete('/admin-delete-car/'+ this.car.car_id).then( res => {
        console.log(res.data['status'])
        if (res.data['status'] == 'success') {
          this.carData.splice(carIndex,1);
          this.$notify.success({
            title:'Deletion',
            message:res.data['message']
          })
        }
      }).catch(res => {
        if (error.response.status == 401) {
          bus.$emit('login')
        } else if (error.response.status == 422) {
          bus.$emit('login')
        }
      })

      console.log(carIndex)
    },
    Edit(car) {
      this.$store.commit('setCar',car);
      this.$router.push({name: 'AdminEdit-Car'});
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
        if (error.response.status == 401) {
          bus.$emit('login')
        } else if (error.response.status == 422) {
          bus.$emit('login')
        }
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
        if (error.response.status == 401) {
          bus.$emit('login')
        } else if (error.response.status == 422) {
          bus.$emit('login')
        }
      })

    },

    Refresh(){
      this.$auth.get('/admin-cars').then( res => {
        if (res.data['status'] == 'success') {
          this.carData = res.data['data'];
          console.log(this.carData);
        }
      }).catch( res => {
        if (error.response.status == 401) {
          bus.$emit('login')
        } else if (error.response.status == 422) {
          bus.$emit('login')
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
