<template>
    <q-page>
      <div class="form q-pa-md">
        <q-card class="">
          <q-card-section class="button teste text-h6">
            Consultar Fibra
          </q-card-section>
  
          <q-dialog v-model="isModalOpen" persistent>
            <q-card style="min-width: 80vw; min-height: 60vh;">
              <q-card-section>
                />
                <q-list v-if="filteredResults.length" bordered separator class="q-mt-md">
                  <q-item v-for="(item, index) in filteredResults" :key="index" clickable>
                    <q-item-section>
                      <q-item-label>
                        <strong class="data-highlight">Fibra: </strong>
                        <span class="data-highlight">{{ item.Fibra }}</span>
                      </q-item-label>
                      <q-item-label>
                        <strong class="data-highlight">OLT: </strong>
                        <span class="data-highlight">{{ item.OLT }}</span>
                      </q-item-label>
                      <q-item-label>
                        <strong class="data-highlight">ONU: </strong>
                        <span class="data-highlight">{{ item.Onu }}</span>
                      </q-item-label>
                      <q-item-label>
                        <strong class="data-highlight">Rx power: </strong>
                        <span :class="{ 'text-red': isRxPowerHigh(item['Rx power']) }" class="data-highlight">
                          {{ item['Rx power'] }}
                        </span>
                      </q-item-label>
                    </q-item-section>
                  </q-item>
                </q-list>
  
                <div v-else class="q-mt-md">
                  <q-banner color="warning" class="q-my-md">
                    Nenhum resultado encontrado.
                  </q-banner>
                </div>
              </q-card-section>
  
         
              <q-card-actions align="right">
                <q-btn label="Salvar" color="yellow" @click="saveData" />
              </q-card-actions>
            </q-card>
          </q-dialog>
  
          <q-card-section class="text teste">
            <q-form>
              <q-select
                v-model="form.host_name"
                label="Região"
                :options="host_name"
                option-label="name"
                option-value="value"
                emit-value
                map-options
                outlined
                dense
                class="q-mb-md"
                @update:model-value="fetchFibers"
              />
              <q-select
                v-model="form.fibra"
                label="Fibra"
                :options="fibra"
                option-label="fibra"
                option-value="fibra"
                emit-value
                map-options
                outlined
                dense
                class="text q-mb-md"
                :disable="!fibra.length"
              />
              <div class="button q-mt-md">
                <q-btn label="Pesquisar" @click="getFibers" color="yellow" :loading="isLoading" />
              </div>
              <div>
                <q-spinner v-if="isLoading" color="blue" size="50px" class="q-mt-lg" />
              </div>
            </q-form>
          </q-card-section>
        </q-card>
      </div>
    </q-page>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import axios from 'axios';
  import { useQuasar } from 'quasar';
  
  export default {
    setup() {
      const $q = useQuasar();
      const form = ref({ host_name: null, fibra: null });
      const host_name = ref([
        { value: "picarras", name: "Piçarras", alias: "SC-PCX-A001-SW01-OLT-C600" },
        { value: "penha", name: "Penha", alias: "SC-PEN-SW01-OLT-C600" },
        { value: "barra_do_sul", name: "Barra do Sul", alias: "SC-BDSL-SW01-OLT-C650" },
        { value: "morretes", name: "Morretes", alias: "SC-MRT-SW01-OLT-C610" },
        { value: "barra_velha", name: "Barra Velha", alias: "SC-BVH-SW01-OLT-C600" },
        { value: "navegantes", name: "Navegantes", alias: "SC-NVG-SW01-OLT-C610" }
      ]);
      const user = JSON.parse(localStorage.getItem("user"));
      const fibra = ref([]);
      const isModalOpen = ref(false);
      const results = ref([]);
      const isLoading = ref(false);
      const filter = ref('');
      const status = ref('Sucesso');
      const count = ref(0);
  
      const fetchFibers = async () => {
        if (!form.value.host_name) return;
        isLoading.value = true;
        try {
          const response = await axios.get(`API Urls/${form.value.host_name}`);
          fibra.value = response.data.map(item => item.fibra);
          form.value.fibra = null;
        } catch (error) {
          console.error("Erro ao buscar fibras:", error);
        } finally {
          isLoading.value = false;
        }
      };
      const getFibers = async () => {
        if (!form.value.host_name || !form.value.fibra) return;
  
        const selectedHost = host_name.value.find(item => item.value === form.value.host_name);
        const oltAlias = selectedHost ? selectedHost.alias : null;
  
        if (!oltAlias) {
          console.error("Alias não encontrado para a região selecionada.");
          return;
        }
        isLoading.value = true;
        try {
          const response = await axios.get(`API Urls/fiber`, {
            params: {
              user: user.username,
              fiber: form.value.fibra,
              olt: oltAlias
            },
            timeout: 99990
          });
  
          results.value = response.data.Data[0].Onus.map(onu => ({
            Fibra: response.data.Data[0].Fibra,
            OLT: response.data.Data[0].OLT,
            Onu: onu.Onu,
            'Rx power': onu['Rx power']
          }));
          count.value = results.value.length;
          isModalOpen.value = true;
        } catch (error) {
          status.value = 'Erro';
        } finally {
          isLoading.value = false;
        }
      };
  
      const isRxPowerHigh = (rxPower) => {
        const rxPowerValue = parseFloat(rxPower);
        return !isNaN(rxPowerValue) && rxPowerValue < -24.0;
      };

      const saveData = () => {
        console.log("Dados salvos:", results.value);

        $q.notify({
          message: 'Dados salvos com sucesso!',
          color: 'positive',
          position: 'top'
        });

        isModalOpen.value = false;
      };

      const filteredResults = computed(() => {
        if (!filter.value) return results.value;
        return results.value.filter(item =>
          item.Onu.toLowerCase().includes(filter.value.toLowerCase())
        );
      });
  
      return {
        form,
        host_name,
        fibra,
        isModalOpen,
        results,
        filter,
        status,
        count,
        filteredResults,
        isLoading,
        fetchFibers,
        getFibers,
        isRxPowerHigh,
        saveData
      };
    }
  };
  </script>
  
  <style scoped>
  .form {
    width: 300px;
  }
  .teste {
    background-color: #dfdfdfa4;
  }
  .text {
    color: black;
  }
  .button {
    text-align: center;
  
  }
  .data-highlight {
    color: #000000;
  }
  .text-red {
    color: red;
  }
  </style>