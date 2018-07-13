import axios from 'axios'




export default function(Vue){
  let authenticatedUser = {};
  let ready = false;
  let baseURL = '';
  let storage  = {};
  let userLogout = false;

  Vue.auth = {
    setAccessToken(data) {
      this.storage.set('access-token',data['access-token']);
      var t = Date.now() + (900 * 1000);
      this.storage.set('expiration-time',t);

    },

    setBaseUrl(url){
      this.baseURL = url;
    },

    setTokens(data, storage){
      // Set the refresh token and access tokens are login
      if (data['expires']) {
        storage.set('expiration-time', Date.now() + data['expires'])
      } else {
        var t = (Date.now() + (1020 * 1000)) - 2000;
      }
      if (data['refresh-token']) {
        storage.set('refresh-token',data['refresh-token']);
      }
      if (data['access-token']) {
        storage.set('access-token',data['access-token']);
      }

    },

    setAuthenticatedUser(data){
      authenticatedUser = data;
    },

    setStorage(storage){
      this.storage = storage;
    },

    getAccessToken(){
      // Check for the access token and return it
      var token = this.storage.get('access-token');
      var expiration = this.storage.get('expiration-time');
      if(!token || !expiration){
        return null
      }
      var timeLeft = ((expiration - Date.now()) / 1000) / 60;

      console.log(timeLeft + ' minutes');
      if (Date.now() > expiration){
        this.destroyTokens();
        return null;

      }
      return token;
    },

    destroyTokens(){
      // Delete the access token from the system
      this.storage.remove('access-token');
      this.storage.remove('expiration-time');
      this.storage.remove('refresh-token');

    },

    isAuthenticated(){
      // Check if the User is authenticated
      if (this.getAccessToken()) {
        return true;
      }
      return false;
    },



    getRefreshToken(){
      var token = this.storage.get('refresh-token');
      if (!token) {
        return null
      }
      return token;
    },



    getAuthenticatedUser(data){
      return authenticatedUser;
    },


    login(data){
      return axios.post(this.baseURL+'/login',
      data)
    },


    logout(){
      this.userLogout = false;
      var access_token = this.getAccessToken();
      return axios.get(this.baseURL+'/logout-access', {
        headers: {Authorization: "Bearer " + access_token}
      })
    },

    logoutRefresh(){
      var refresh_token = this.getRefreshToken();
      return axios.get(this.baseURL+'/logout-refresh', {
        headers: {Authorization: "Bearer " + refresh_token}
      })

    },

    refreshToken(){
      axios.get(this.baseURL+'/token-refresh',{
        headers:{Authorization: "Bearer " + this.getRefreshToken()},
      }).then(response => {
        this.setAccessToken(response.data);
        return true;
      }).catch( response => {
        console.log(response.data);
        this.destroyTokens();
      });
    },

    validateToken(){
      var expiration = this.storage.get('expiration-time');
      if (Date.now() > expiration) {
        return this.refreshToken();
      }
      return true;
    },

    get(url){
      if (this.validateToken()) {
        return axios.get(this.baseURL+url,{
          headers:{Authorization: "Bearer " +this.getAccessToken()}
        });
      }
      return null;
    },

    post(url, data){
      if(this.validateToken()){
        var access_token = this.getAccessToken();
       return axios.post(this.baseURL+url,data, {
          headers:{Authorization: "Bearer " + access_token}
        })
      }
    },

    delete(url){
      if (this.validateToken()) {
        return axios.delete(this.baseURL+url,{
          headers:{Authorization: "Bearer " +this.getAccessToken()}
        });
      }
      return null;
    },

}

  Object.defineProperties(Vue.prototype, {
    $auth: {
      get: () => {
        return Vue.auth
      }
    }
  })
}
