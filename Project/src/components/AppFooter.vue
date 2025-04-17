<template>
  <div>
    <q-footer elevated class="developed-by">
      <slot></slot>
      
      <q-tabs 
        v-model="tab"
        align="justify"
        class="text-white"
      >
        <q-tab 
          name="home" 
          icon="home" 
          label="Home" 
          class="custom-tab" 
        />
        <q-tab 
          name="settings" 
          icon="settings" 
          label="Configurações" 
          class="custom-tab" 
        />
        <q-tab 
          name="help" 
          icon="help" 
          label="Ajuda" 
          class="custom-tab" 
        />
      </q-tabs>
    </q-footer>
  </div>
</template>

<script>
export default {
  name: "AppFooter",
  data() {
    return {
      tab: "home",
    };
  },
  watch: {
    tab(newTab) {
      this.navigate(newTab);
    },
  },
  methods: {
    navigate(tabName) {
      const routes = {
        home: "/index",
        settings: "/config",
        help: "/help",
      };
      if (routes[tabName]) {
        this.$router.push(routes[tabName]);
      }
    },
  },
};
</script>

<style scoped>
.developed-by {
  background-color: #275194; 
}

.q-tabs {
  background-color: #013b99; 
}

.custom-tab {
  color: #eeecec;
}

.q-tab--active {
  color: #ffeb3b; 
}

@media (min-width: 1024px) {
  /* footer{
    display: none;
  } */
}
</style>
