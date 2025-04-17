<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <div class="background">
    <RouterView />
  </div>
</template>

<style scoped>
.background {
  width: 100vw;
  height: 100vh;
  background-image: url("../src/components/icons/imgs/BackgroundL.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.background::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(71, 71, 71, 0.411);
}

@media screen and (min-width: 1024px) {
  .background {
    background-image: unset;
  }

  
  .background::before {
    background-color: unset;
  }
}
</style>