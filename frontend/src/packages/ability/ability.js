export default function(Vue){

  Vue.can = {
    edit(user, car){
      if (user.id == car.owner.id){
        return true;
      }
      return false
    },

    delete(user, car){
      if (user.id == car.owner.id){
        return true;
      }
      return false
    },

  }

  Object.defineProperties(Vue.prototype, {
    $can: {
      get: () => {
        return Vue.can
      }
    }
  })
}
