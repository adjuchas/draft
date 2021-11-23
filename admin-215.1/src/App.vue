<template>
  <div id="app">
  <home :allmessage="allrecodes"></home>
  </div>
</template>

<script>


import home from "@/components/home";

//import {sendRedirect} from "@/umtils/oauthTool";

export default {
  name: 'App',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    home
  },
 beforeCreate() {
    // let uid=window.localStorage.getItem("uid");
    // if (uid==null){
    //  sendRedirect();
    // }
  },
  created() {
    // let uid=localStorage.getItem("uid")
    // let token =window.sessionStorage.getItem("token")
    // if (token==null&&uid!=null){
    //   this.getToken;
    // }

  },
  data(){
    return{
      uid:window.localStorage.getItem("uid"),
      allrecodes:[]
    }
  },
  methods:{
    // getToken(){
    //   let that=this;
    //   axios.post('http://120.25.121.177:443/api/oauth/get_accesstoke/',{
    //     "uid":that.uid
    //   }).then(res=>{
    //     if (res.data.message==="success"){
    //       let token=res.data.access_token;
    //       window.sessionStorage.setItem("token",token);
    //       that.getAllinfo();
    //     }
    //   })
    // },

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
