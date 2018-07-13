<template lang="html">
  <div class="">
    <div class="" style="max-width: 900px; padding-right: 20px;">


      <el-steps :active="step" finish-status="success">
        <el-step title="Step 1"></el-step>
        <el-step title="Step 2"></el-step>
        <el-step title="Step 3"></el-step>
        <el-step title="Image"></el-step>
      </el-steps>

      <div v-if="step == 0"class="step-container">
        <h1>Step 1</h1>
        <el-form label-position="left" label-width="120px">
          <el-form-item label="Name" prop="name">
            <el-input  v-model="car.name" placeholder=""></el-input>
          </el-form-item>
          <el-form-item label="Price" prop="price">
            <el-input v-model="car.price"></el-input>
          </el-form-item>
          <el-form-item label="Brand" prop="brand">
            <el-input v-model="car.brand"></el-input>
          </el-form-item>
          <el-form-item label="Model" prop="model">
            <el-input v-model="car.model"></el-input>
          </el-form-item>
          <el-form-item label="Year" prop="year">
            <el-date-picker
              format="yyyy"
              value-format="yyyy,MM,dd"
              v-model="car.year"
              type="year"

              placeholder="Pick a year"
              class="w-100"
              >
            </el-date-picker>
          </el-form-item>
        </el-form>
      </div>
      <div class="step-container" v-if="step==1">
        <h1>Step 2</h1>
        <el-form label-position="left" label-width="120px">

          <el-form-item label="Transmission" prop="transmission">
            <el-select placeholder="Transmission" v-model="car.transmission" class="w-100">
              <el-option
                v-for="item in transmissions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Engine" prop="engine">
            <el-select placeholder="Cylinder" v-model="car.engine" class="w-100">
              <el-option
                v-for="item in engines"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Mileage" prop="mileage">
            <el-input v-model="car.mileage"></el-input>
          </el-form-item>
          <el-form-item label="Fuel" prop="fuel">
            <el-select placeholder="Fuel" v-model="car.fuel" class="w-100">
              <el-option
                v-for="item in fuel_type"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                >
              </el-option>
            </el-select>
          </el-form-item>

          <el-form-item label="Type" prop="type">
            <el-select placeholder="Type of car" v-model="car.type" class="w-100">
              <el-option
                v-for="item in car_type"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                >
              </el-option>
            </el-select>
          </el-form-item>

        </el-form>

      </div>
      <div class="step-container" v-if="step == 2">
        <h1>Step 3</h1>
        <el-form label-position="left"  label-width="120px">
          <el-form-item label="Drive Train" prop="drive_train">
            <el-select placeholder="Drive Train" v-model="car.drive_train" class="w-100">
              <el-option
                v-for="item in drive_type"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Description" prop="description">
            <el-input type="textarea" :rows="8" v-model="car.description"></el-input>
          </el-form-item>
        </el-form>
      </div>
      <div class="step-container" v-if="step == 3">
        <h3>Images</h3>
        <div class="">
          <img :src="imageUrl" alt="Car image">
        </div>
        <el-upload
          :action="upload_url"
          :show-file-list="false"
          :on-change="onChanged"
          :auto-upload="false"
          ref="upload"
          :data="fileData"
          :on-success="handleAvatarSuccess">
          <el-button class="mb-10" size="small" type="primary">Update Image</el-button>
        </el-upload>
      </div>
      <div class="btn-container">
        <el-button @click="step--" v-if="step > 0">Previous</el-button>
        <el-button @click="move" v-if="step < 3">next</el-button>
        <el-button @click="onSubmit" v-if="step == 3">Save</el-button>
      </div>

    </div>
  </div>
</template>

<script>

import { bus } from '../../main';

export default {
  data(){
    return {
      have_photo: true,
      step: 0,
      car: {},
      transmissions: [{
          value:"manual",
          label: "Manual"
        },
        {
          value:"automatic",
          label:"Automatic"
        }],
      engines: [{
          value:'4',
          label: '4 Cylinder'
        },
        {
          value:'6',
          label: '6 Cylinder'
          },
        {
          value:'8',
          label: '8 Cylinder'
        },
        {
          value: '10',
          label: '10 Cylinder'
        },
        {
          value:'12',
          label: '12 Cylinder'
          },
        ],

      fuel_type: [{
          value: 'diesel',
          label: 'Diesel'
        },
        {
          value: 'petrol',
          label: 'Petrol'
        }],
      drive_type : [{
          value: '2',
          label: '2WD'
        },
        {
          value: '4',
          label: '4WD'
        }],
      car_type: [
        {
          value: 'luxury',
          label: 'Luxury'
        },
        {
          value: 'new',
          label: 'New'
        },
        {
          value: 'old',
          label: 'Old'
        },
        {
          value: 'rent',
          label: 'Rent'
        }
      ],
      imageUrl: '',
      fileData:{
        car_id: '',
      }
    };
  },

  created() {
    //do something after creating vue instance
    var url = window.location.hostname+':'+window.location.port;
    //this.upload_url = 'http://' + url + '/api/v1/upload-photo' // production
    this.upload_url = "http://localhost:5000"+"/api/v1/upload-photo" // dev
    this.car = this.$store.getters.car;
    //this.imageUrl = 'http://' + url +'/api/v1/get-photo/'+this.car.card_id;
    this.imageUrl = 'http://localhost:5000/get-photo/'+this.car.car_id;
  },

  methods: {
    onSubmit() {
      if (this.have_photo){
        console.log(this.car);
        this.$auth.post('/api/v1/edit-car', this.car).then(res => {
          this.$notify({
                title:'Car',
                message: res.data['message'],
                type: res.data['status']
          });
          this.$http.get('/api/v1/get-cars').then( res => {
            this.cars = res.data['data'];
            this.$store.commit('setCars',this.cars)
          }).catch( res => {
            console.log(res.response);
          })
        }).catch( error =>{
          console.log(error.response)
          if (error.response.status == 401) {
            bus.$emit('login')
          } else if (error.response.status == 422) {
            bus.$emit('login')
          }
        })
      } else {
        this.$notify.info({
            title:'Image',
            message: 'Please add a Featured Image'
        })
      }
    },

    handleAvatarSuccess(res, file) {

      //  this.$store.commit('setCar',res.data['data']);
        console.log('upload successful');
        console.log(res.data['data']);
        console.log('upload successful');
    //    bus.$emit('ViewCar',res.data['data'].pic);

        this.$router.push({name: 'View-Car'});
      },
      beforeAvatarUpload(file) {
        this.imageUrl = URL.createObjectURL(file.raw);
        const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        if (!isJPG) {
          this.$message.error('Avatar picture must be JPG format!');
        }
        if (!isLt2M) {
          this.$message.error('Avatar picture size can not exceed 2MB!');
        }
        return isJPG && isLt2M;
      },

      onChanged(file,fileList){
        this.imageUrl = URL.createObjectURL(file.raw);
        this.fileData.car_id = this.car.car_id;
        this.$refs.upload.submit();
      },

      onSubmitTest(){
        console.log(this.form);
      },

      move(){
        if (this.step < 3) {
          this.step++;
        } else {
          this.step = 0;

        }
      }
    }

}
</script>

<style lang="scss">

  .mb-10 {
    margin-bottom: 10px;
  }

  .w-100 {
    width: 100% !important;
  }

  .step-container {
    min-height: 200px;

  }
  .btn-container {
    display: flex;
    justify-content: space-between;
  }
</style>
