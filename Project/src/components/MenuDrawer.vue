<template>
</template>
  
<script>
import MenuItem from "./MenuItem.vue";
import buttonAccount from "./ButtonAccount.vue";

export default {
  name: "MenuDrawer",
  components: {
    MenuItem,
    buttonAccount
  },
  data() {
    return {
      drawer: false,
    };
  },
  methods: {
    logout() {
      console.log("Usuário deslogado");
     
    },
  },
};
</script>
