<template>
  <q-page class="q-pa-md">
    <q-card class="q-mb-md">
      <q-card-section>
        <h5 class="texth text-h5">Dados do Usuário</h5>
      </q-card-section>
      <q-card-section>
        <q-list bordered>
          <q-item>
            <q-item-section>
              <q-item-label class="text">Nome</q-item-label>
              <q-item-label class="text" caption>{{ user.name }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>
              <q-item-label class="text">E-mail</q-item-label>
              <q-item-label class="text" caption>{{ user.email }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>

    <q-card>
      <q-card-section>
        <h5 class="texth text-h5">Preferências</h5>
      </q-card-section>
      <q-card-section>
        <q-form @submit="saveSettings">
          <q-toggle class="text"
            v-model="settings.notifications"
            label="Receber notificações"
          />
          <q-btn
            type="submit"
            color="primary"
            label="Salvar Configurações"
            class="q-mt-md"
          />
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import { ref, onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: 'SettingsPage',
  setup() {
    const router = useRouter();
    const token = ref('');
    const user = ref({
      name: 'Usuário não identificado',
      email: 'E-mail não identificado',
    });

    const extractUserInfo = (token) => {
      if (token) {
        try {
          const name = token.split('username')[1].split(',')[0].split('"')[2];
          const email = token.split('email')[1].split(',')[0].split('"')[2];
          return { name, email };
        } catch (error) {
          console.error('Erro ao processar o token:', error);
          return { name: 'Usuário não identificado', email: 'E-mail não identificado' };
        }
      }
      return { name: 'Usuário não identificado', email: 'E-mail não identificado' };
    };

    onBeforeMount(() => {
      const storedToken = localStorage.getItem('user');
      token.value = storedToken ? storedToken : '';
      user.value = extractUserInfo(token.value);
    });

    return {
      user,
      settings: ref({
        notifications: true,
        darkMode: false,
      }),
      saveSettings() {
        this.$q.notify({
          type: 'positive',
          message: 'Configurações salvas com sucesso!',
        });
      },
    };
  },
};
</script>

<style scoped>

.q-card {
  margin-bottom: 20px;
}
</style>
<style scoped>

.text{ 
    color: black;
}

.texth {
    color: black;
    margin-right: 20%;
}
.q-card {
  margin-bottom: 20px;
}

@media screen and (min-width: 1024px) {
 
}

</style>