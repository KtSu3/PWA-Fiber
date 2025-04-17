<template>
    <svg 
        xmlns="http://www.w3.org/2000/svg" 
        :height="size" 
        viewBox="0 -960 960 960" 
        :width="size"
        :fill="color">
        <slot></slot>
        <path d="M250-279h220v-60H250v60Zm120-171h220v-60H370v60Zm120-171h220v-60H490v60ZM180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/>
    </svg>
  </template>
  
  <script>
  export default {
      name: "CustomIcon",
      props: {
          size: {
              type: [String, Number],
              default: 50,
          },
          color: {
              type: String,
              default: "#FAF13A"
          },
      },
  };
  </script>