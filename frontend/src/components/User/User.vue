  <template lang="html">
    <div class="">
      <el-tabs type="border-card">
        <el-tab-pane label="Profile">
          <div class="tab">
            <div class="" style="display:flex;">
              <div class="profile-img">
                <img src="" alt="">
              </div>
              <div class="">
                  <p>{{ user }}</p>
                  <p>{{ }}</p>
                  <el-button>Edit Profile</el-button>
              </div>
            </div>
          </div>
        </el-tab-pane>
        <el-tab-pane label="Cars">
          <div class="tab">
            <el-card v-for="car in cars" :key="car" :label="car" style="margin-bottom:10px;">
              <div class="" style="display:flex; justify-content:space-between;">
                <div class="car-content" style="display:flex; max-width:400px;">
                  <div class="profile-sm">
                    <my-img :image_url="car.car_id"></my-img>
                  </div>
                  <div class="">
                    {{ car.name }}
                  </div>
                </div>
                <div class="">
                  <el-button @click="Edit(car)">Edit</el-button>
                  <el-button type="danger">Delete</el-button>
                </div>
              </div>
            </el-card>
          </div>
        </el-tab-pane>
        <el-tab-pane label="Profile">
          <div class="tab">

          </div>
        </el-tab-pane>
      </el-tabs>
    </div>

</template>

<script>
import Image from '../Image'
export default {

  components: {
    'my-img': Image,
  },

  data(){
    return {
      user: {},
      cars: []
    }
  },

  created() {
    this.user = this.$store.getters.user;
    this.$auth.get('/my-cars/'+this.user.id).then(res => {
      this.cars = res.data['data']
      console.log(res.data['data'])
    })
  },

  methods: {
    Edit(car) {
      this.$store.commit('setCar',car);
      this.$router.push({name: 'Edit-Car'});
    },
  }
}
</script>

<style lang="scss">

.tab {
  max-height: 425px;
  min-height: 400px;
  overflow-y: auto;
}

.profile-img {
  width: 250px;
  height: 250px;
  min-width: 250px;
  border: 1px solid;
  border-radius: 50%;
  margin-right: 50px;
  overflow: hidden;
}

.profile-sm {
  width: 75px;
  height: 75px;
  min-width: 75px;
  border: 1px solid;
  border-radius: 50%;
  margin-right: 20px;
  overflow: hidden;
}
</style>
