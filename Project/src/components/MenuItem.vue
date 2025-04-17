<template>
    <q-item clickable v-ripple @click="onClick">
      <q-item-section avatar>
        <q-icon :name="icon" />
      </q-item-section>
      <q-item-section>
        <q-item-label>{{ label }}</q-item-label>
      </q-item-section>
    </q-item>
  </template>
  
  <script>
  export default {
    name: "MenuItem",
    props: {
      label: {
        type: String,
        required: true,
      },
      icon: {
        type: String,
        required: true,
      },
      to: {
        type: String,
        default: "",
      },
    },
    methods: {
      onClick() {
        if (this.to) {
          this.$router.push(this.to);
        }
      },
    },
  };
  </script>
  