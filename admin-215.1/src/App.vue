<template>
  <div id="app">
  <home></home>
  </div>
</template>

<script>


import home from "@/components/home";


export default {
  name: 'App',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    home
  },
 beforeCreate() {

  },
  created() {

  },
  data(){
    return{

    }
  },
  methods:{


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
