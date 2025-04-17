<template>
  <div>
    <q-input v-model="filter" label="Filtrar Resultados" class="q-mt-md" />
    <q-list v-if="filteredResults.length" class="q-mt-md results-list">
      <q-item v-for="result in filteredResults" :key="result.serial_number">
        <q-item-section>
          <div><strong>Name:</strong> <span class="testo">{{ result.name }}</span></div>
          <div><strong>ONU:</strong> <span class="testo">{{ result.onu }}</span></div>
          <div><strong>ONU Distance:</strong> <span class="testo">{{ result.onu_distance }}</span></div>
          <div><strong>Phase State:</strong> <span class="testo">{{ result.phase_state }}</span></div>
          <div><strong>PON:</strong> <span class="testo">{{ result.pon }}</span></div>
          <div><strong>Serial Number:</strong> <span class="testo">{{ result.serial_number }}</span></div>
          <div><strong>Signal:</strong> <span class="testo">{{ result.signal }}</span></div>
          <div><strong>Slot:</strong> <span class="testo">{{ result.slot }}</span></div>
        </q-item-section>
      </q-item>
    </q-list>
    <div v-else class="q-mt-md">Resultados não Encontrados</div>
  </div>
</template>

<script>
export default {
  props: {
    results: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      filter: "",
    };
  },
  computed: {
    filteredResults() {
      return this.results.filter(
        (result) =>
          result.name.toLowerCase().includes(this.filter.toLowerCase()) ||
          result.serial_number.toLowerCase().includes(this.filter.toLowerCase())
      );
    },
  },
};
</script>

<style scoped>
.q-mt-md {
  margin-top: 14px;
}

.testo {
  color: blueviolet !important;
  font-weight: bold;
}
</style>
