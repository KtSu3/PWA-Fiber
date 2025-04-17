<template>
      <div class="text-h5 text-center q-mt-md title">
        <slot></slot>
      </div>
    
</template>

<script>
  export default {
    name: "MobileTitle",
    props: {
      title: {
        type: String,
        default: "Primeira Consulta"
      },
    },

  };
</script>

<style scoped>
 .q-page {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
.text-h5 {
    font-size: 1.25rem; 
    color: black;
  }
</style>
  