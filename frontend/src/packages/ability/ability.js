export default function(Vue){

  Vue.can = {
    edit(user, car){
      try {
        if (user.id == car.owner.id){
          return true;
        }
        return false;

      } catch (e) {
        console.log(e)
        return false;
      }

    },

    delete(user, car){
      try {
        if (user.id == car.owner.id){
          return true;
        }
        return false
      } catch (e) {
        console.log(e);
        return false;
      }
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
