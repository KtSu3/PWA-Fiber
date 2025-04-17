<template>
  <q-layout view="hHh lpR fFf">
    <app-header @toggle-drawer="toggleDrawer" />
    <menu-drawer ref="drawer" />
    <q-page-container>
      <div class="cards">
        <q-item class="card" clickable to="/ceverification">
          <cards>
            <div>
              <div class="card-title">Procedimento</div>
            </div>
            <div>
              <Procedures></Procedures>
            </div>
          </cards>
        </q-item>

        <q-item class="card" clickable to="/powerverification">
          <cards>
            <div>
              <div class="card-title">Potencias</div>
            </div>
            <div>
              <Potencias></Potencias>
            </div>
          </cards>
        </q-item>

        <q-item class="card" clickable to="/clientverification">  
          <cards>
            <div>
              <div class="card-title">Histórico</div>
            </div>
            <div>
              <ClientHistory></ClientHistory>
            </div>
          </cards>
        </q-item>

        <q-item class="card" clickable to="/fiber">  
          <cards>
            <div>
              <div class="card-title">Fibra</div>
            </div>
            <div>
              <Fiber></Fiber>
            </div>
          </cards>
        </q-item>
        
      </div>
    </q-page-container>
    <app-footer />
  </q-layout>
</template>

<script>
import AppHeader from "../components/AppHeader.vue";
import MenuDrawer from "../components/MenuDrawer.vue";
import AppFooter from "../components/AppFooter.vue";
import Cards from "../components/Cards.vue";
import ClientHistory from "../components/icons/themes/ClientHistory.vue";
import Potencias from "../components/icons/themes/Potencias.vue";
import Procedures from "../components/icons/themes/Procedures.vue";
import Fiber from "../components/icons/themes/Fiber.vue";


export default {
  name: "MainLayout",
  components: {
    AppHeader,
    MenuDrawer,
    AppFooter,
    Cards,
    ClientHistory,
    Potencias,
    Procedures,
    Fiber,
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
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 10px;
  text-align: center;

}

.cards { 
  margin-top: 75px;
  justify-content: center;
  display: flex;
  flex-wrap: wrap;
}

.card-title {
  margin-bottom: 5px; 
  font-size: 1.2em;
  color: black;
}

</style>