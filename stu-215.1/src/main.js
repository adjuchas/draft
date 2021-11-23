import Vue from 'vue'
import App from './App.vue'
import Element from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import store from "./store"
import controlClickState from "./controlClickState";
Vue.use(controlClickState);

Vue.config.productionTip = false
Vue.use(Element,{size: 'small', zIndex: 3000})
new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
