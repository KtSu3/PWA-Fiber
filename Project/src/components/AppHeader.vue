<template>
    <q-header elevated class="color">
      <q-toolbar>
        <q-toolbar-title><buttonReturn></buttonReturn></q-toolbar-title>
        <buttonAccount></buttonAccount>
      </q-toolbar>
    </q-header>
  </template>
  
<script>
import buttonAccount from './ButtonAccount.vue';
import buttonReturn from './ButtonReturn.vue';
export default {
  name: "AppHeader",
  components: {
    buttonAccount,  
    buttonReturn
  }
};
</script>
  
<style>
.color {
  background-color: rgb(10, 55, 138); 
}
</style>