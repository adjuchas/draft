import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex);

const store=new Vuex.Store({
    state: {
        token:sessionStorage.getItem("access_token"),
        user:JSON.parse(sessionStorage.getItem("stu_info"))
    },
    getters:{

    },
    mutations: {
        changeUser(state,user){
            state.user=user;
        },
        changeToken(state,token){
            state.token=token;
        }
    },
    actions: {

    }
})
export  default store