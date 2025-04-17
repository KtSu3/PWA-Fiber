<template>
      <q-btn
        :loading="progress[0].loading"
        :percentage="progress[0].percentage"
        color="primary"
        @click="startComputing(0)"
        style="width: 200px"
      >
        Comparar Potencias
        <template v-slot:loading>
          <q-spinner-gears class="on-left" />
          Comparando...
        </template>
      </q-btn>

  </template>
  
  <script>
  import { ref, onBeforeUnmount } from 'vue'
  
  export default {
    setup () {
      const progress = ref([
        { loading: false, percentage: 0 },
        { loading: false, percentage: 0 },
        { loading: false, percentage: 0 }
      ])
  
      const intervals = [ null, null, null ]
  
      function startComputing (id) {
        progress.value[ id ].loading = true
        progress.value[ id ].percentage = 0
  
        intervals[ id ] = setInterval(() => {
          progress.value[ id ].percentage += Math.floor(Math.random() * 8 + 10)
          if (progress.value[ id ].percentage >= 100) {
            clearInterval(intervals[ id ])
            progress.value[ id ].loading = false
          }
        }, 700)
      }
  
      onBeforeUnmount(() => {
        intervals.forEach(val => {
          clearInterval(val)
        })
      })
  
      return {
        progress,
        startComputing
      }
    }
  }
  </script>
  