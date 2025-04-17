<template>
  <q-input
    outlined
    color="yellow"
    v-model="searchBox"
    label="Digite a CE para buscar"
    debounce="300"
    class="custom-input"
  >
    <template v-slot:append>
      <q-btn
        label="Buscar"
        color="yellow"
        :loading="isLoading"
        @click="fetchData"
      />
    </template>
  </q-input>

  <q-spinner v-if="isLoading" color="blue" size="50px" class="q-mt-lg" />

  <q-dialog v-model="isModalOpen" persistent>
    <q-card style="min-width: 80vw; min-height: 60vh">
      <q-card-section>
        <div class="data-highlight text-h6">Totais por Status:</div>
        <q-list bordered class="q-mt-md">
          <q-item v-for="(count, status) in statusCounts" :key="status">
            <q-item-section>
              <q-item-label>
                <strong class="data-highlight">Status: </strong>
                <span class="data-highlight">{{ status }} - </span>
                <span class="data-highlight">{{ count }}</span>
              </q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <q-card-section>
        <q-input
          v-model="filter"
          label="Filtrar por Cliente"
          placeholder="Digite o nome do cliente"
          clearable
        />
        <q-list
          v-if="filteredResults.length"
          bordered
          separator
          class="q-mt-md"
        >
          <q-item
            v-for="(item, index) in filteredResults"
            :key="index"
            clickable
          >
            <q-item-section>
              <q-item-label>
                <strong class="data-highlight">Cliente: </strong>
                <span class="data-highlight">{{ item.name }}</span>
              </q-item-label>
              <q-item-label>
                <strong class="data-highlight">SLOT: </strong>
                <span class="data-highlight">{{ item.slot }}</span>
              </q-item-label>
              <q-item-label>
                <strong class="data-highlight">PON: </strong>
                <span class="data-highlight">{{ item.pon }}</span>
              </q-item-label>
              <q-item-label>
                <strong class="data-highlight">ONU: </strong>
                <span class="data-highlight">{{ item.onu }}</span>
              </q-item-label>
              <q-item-label>
                <strong class="data-highlight"> Distância ONU: </strong>
                <span class="data-highlight">{{ item.onu_distance }}</span>
              </q-item-label>
              <q-item-label>
                <strong class="data-highlight">Status: </strong>
                <span class="data-highlight">{{ item.status }}</span>
              </q-item-label>
              <q-item-label>
                <strong class="data-highlight">Potencia Anterior: </strong>
                <span
                  class="data-highlight"
                  :class="{
                    'text-negative': isSignalDifferenceCritical(
                      item.signal_old,
                      item.signal_new
                    ),
                  }"
                >
                  {{ item.signal_old }}
                </span>
              </q-item-label>
              <q-item-label>
                <strong class="data-highlight">Potencia Atual: </strong>
                <span
                  class="data-highlight"
                  :class="{
                    'text-negative': isSignalDifferenceCritical(
                      item.signal_old,
                      item.signal_new
                    ),
                  }"
                >
                  {{ item.signal_new }}
                </span>
              </q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <div v-else class="q-mt-md">
          <q-banner color="warning" class="q-my-md">
            Sem Alterações na CE.
          </q-banner>
        </div>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn
          flat
          label="Salvar"
          color="secondary"
          v-close-popup
          @click="saveData"
        />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { ref, computed } from "vue";
import { useQuasar } from "quasar";
import axios from "axios"; // Importando Axios

export default {
  name: "SearchCe",
  setup() {
    const searchBox = ref("");
    const isLoading = ref(false);
    const resultData = ref([]);
    const isModalOpen = ref(false);
    const filter = ref("");
    const $q = useQuasar();

    // Computar totais por status
    const statusCounts = computed(() => {
      return resultData.value.reduce((acc, item) => {
        if (item.status) {
          acc[item.status] = (acc[item.status] || 0) + 1;
        }
        return acc;
      }, {});
    });

    const fetchData = async () => {
      if (!searchBox.value || !searchBox.value.trim()) {
        $q.notify({
          message: "Por favor, insira uma CE para buscar.",
          color: "red",
          position: "top",
        });
        return;
      }

      isLoading.value = true;
      resultData.value = [];

      try {
        const user = JSON.parse(localStorage.getItem("user"));
        if (!user || !user.username) {
          throw new Error("Usuário não encontrado ou mal formatado no localStorage.");
        }

        const url1 = `https://example${encodeURIComponent(
          searchBox.value
        )}&user=${encodeURIComponent(user.username)}`;

        const url2 = `URLS Example`;

        const postData = [
          {
            search: searchBox.value.trim(),
            user: user.username.trim(),
          },
        ];

        // Primeira requisição (GET) com Axios 
        const response1 = await axios.get(url1);
        resultData.value = Array.isArray(response1.data.data) ? response1.data.data : [];
        console.log("Dados recebidos da primeira API:", resultData.value);

        // Segunda requisição (POST) com Axios e timeout
        try {
          const response2 = await axios.post(url2, postData, {
            headers: {
              "Content-Type": "application/json",
            }
          
          });

          console.log("Dados recebidos da segunda API:", response2.data);
        } catch (postError) {
          console.error("Erro na segunda requisição (POST):", postError);
          $q.notify({
            message: "Erro ao enviar dados de busca, mas a consulta foi realizada.",
            color: "orange",
            position: "top",
          });
        }

        if (resultData.value.length > 0) {
          isModalOpen.value = true;
        } else {
          $q.notify({ message: "Nenhum resultado encontrado.", color: "orange", position: "top" });
        }
      } catch (error) {
        console.error("Erro durante a requisição:", error);
        $q.notify({ message: error.message, color: "red", position: "top" });
      } finally {
        isLoading.value = false;
      }
    };

    const filteredResults = computed(() =>
      resultData.value.filter((item) =>
        item.name?.toLowerCase().includes(filter.value.trim().toLowerCase())
      )
    );

    const saveData = async () => {
      if (resultData.value.length === 0) {
        $q.notify({ message: "Nenhum dado para salvar.", color: "red", position: "top" });
        return;
      }

      try {
        isModalOpen.value = false;
        $q.notify({ message: "Dados salvos com sucesso!", color: "green", position: "top" });
      } catch (error) {
        console.error("Erro durante o salvamento:", error);
        $q.notify({ message: error.message, color: "red", position: "top" });
      }
    };

    return {
      searchBox,
      isLoading,
      resultData,
      isModalOpen,
      filter,
      filteredResults,
      statusCounts,
      fetchData,
      saveData,
    };
  },
};
</script>

<style scoped>
.q-mt-md {
  margin-top: 16px;
}

.data-highlight {
  color: rgb(0, 0, 0);
  font-weight: bold;
}

.custom-input {
  background-color: rgba(199, 200, 201, 0.842);
  max-width: 300px;
  width: 100%;
  margin-left: 50px;
}

.text-negative {
  color: red;
}
</style>