<template>
    <svg xmlns="http://www.w3.org/2000/svg" 
    height="48px" 
    viewBox="0 -960 960 960" 
    width="48px" 
    fill="#FFFF55">
    <path d="M160-240v-60h284L84-660l42-42 353 353 234-233q-6-11-9.5-23.5T700-630q0-38 26-64t64-26q38 0 64 26t26 64q0 38-26 64t-64 26q-8 0-14.5-1t-14.5-4L516-300h284v60H160Z"/>
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