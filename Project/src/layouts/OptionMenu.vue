<template>
  <q-layout view="hHh lpR fFf">
    <app-header @toggle-drawer="toggleDrawer" />
    <menu-drawer ref="drawer" />
    <q-page-container>
      <router-view />
    </q-page-container>
    <app-footer />
  </q-layout>
</template>
  
<script>
import AppHeader from "../components/AppHeader.vue";
import MenuDrawer from "../components/MenuDrawer.vue";
import AppFooter from "../components/AppFooter.vue";
import buttonAccount from "../components/ButtonAccount.vue";
import cards from "../components/Cards.vue";


export default {
  name: "MainLayout",
  components: {
    AppHeader,
    MenuDrawer,
    AppFooter,
    buttonAccount,
    cards,
  },
  methods: {
    toggleDrawer() {
      this.$refs.drawer.drawer = !this.$refs.drawer.drawer;
    },
  },
};
</script>
  
<style scoped>
.card {
  margin-left: 14%;
  margin-top: 30%;
  margin-right: 10%;
}
</style>
  