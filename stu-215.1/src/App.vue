<template>
  <div id="app" >
    <home  :filelog="fileLog" @fileupload="getfileinf"></home>
  </div>
</template>

<script>

import home from "./components/home";
import axios from "axios";
import {sendRedirect} from "./untils/oauthTool";


export default {
  beforeCreate() {
    let uid=window.localStorage.getItem("215_uid")
    if (uid==null){
      sendRedirect();
    }
  },
  created() {
      this.getAccesstoken();//获取token
  },
  name: 'App',
  data(){
    return {
      uid:window.localStorage.getItem("215_uid"),
      token:this.$store.state.token,
      fileLog:[],//学生提交记录表格数据
    }
  },
  components: {
   home
  },
  methods:{
    changeUser(usr){//登录改变全局的info
      this.$store.commit("changeUser",usr);
    },
    /**
     *  获取密匙
     * */

    getAccesstoken(){
      let that=this;
      axios.get('https://csxy-yiban.cn/api/app215/oauth/get_accesstoken/',{
        params:{uid:window.localStorage.getItem("215_uid")}
      }).then((res)=>{
        if (res.data.message==="success"){
        let token=res.data.access_token;
         this.$store.commit("changeToken",token);
          that.getstumsg(token);
          that.getfileinf(token);
        }
        else {
          sendRedirect();
        }
      })
    },
    getstumsg(token){//获取学生信息
      axios.get('https://csxy-yiban.cn/api/app215/oauth/get_info/', {
        params: {access_token:token}
      }).then(res=>{
        if (res.data.message==="success"){
          let data=res.data.info;
          window.sessionStorage.setItem("stu_info",JSON.stringify(data));
          this.changeUser(data);
        }
        else
          console.log(res.data.message);
      })
    },
    getfileinf(token){//获取学生提交信息
      let that =this;
      axios.get('https://csxy-yiban.cn/api/app215/stu/get_selfall/',{
        params:{access_token:token}
      }).then(res=>{
        if (res.data.message==="success"){
          that.fileLog=res.data.all_recode;
        }
      })
    },

  }

}
</script>

<style>
#app {
  min-width:407px ;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
