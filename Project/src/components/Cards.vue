<script setup>
defineProps({
  svgPath: {
    type: String,
    required: true
  }
});
</script>

<template>
    <q-card class="slot custom-card my-card">
        <q-card-section class="card-link">
              <div class="slot">
                  <q-item class="center">
                    <slot clickable to=""></slot>
                  </q-item>
              </div>
        </q-card-section>
    </q-card>
</template>

<style scoped>
.my-card {
  width: 150px;
  height: 120px;
  display: inline-block;
  background-color:  #e0eafa9a ;  
  border-radius: 7%;
  transition: transform 0.5s ease, box-shadow 0.5s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);

.cards{
  display: flex;
}  
  .q-img {
      height: 80px !important;
  }
.slot {
    text-align: center;
    display: inherit;
}
  
.custom-card{
  transform: translateY(-5px) scale(1.03);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}
  .card-link {
      padding: 7px;
      height: 50px !important;
      border-radius: 10%;
      .q-item {
          height: 30px;
      }
  }
}

.center {
  display: block;
}
</style>