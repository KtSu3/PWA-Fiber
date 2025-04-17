<script>
import { useRouter } from "vue-router";
import { onBeforeMount, ref } from "vue";

export default {
  setup() {
    const router = useRouter();
    const token = ref("");

    onBeforeMount(() => {
      const storedToken = localStorage.getItem("user");
      token.value = storedToken ? storedToken : "";
    });

    const account = () => {
      if (token.value) {
        try {
          return token.value.split("username")[1].split(",")[0].split('"')[2];
        } catch (error) {
          console.error("Erro ao processar o token:", error);
          return "Usuário não identificado";
        }
      }
      return "Usuário não identificado";
    };

    const logout = () => {
      localStorage.setItem("user", "");
      router.push("/login");
    };

    return {
      account,
      logout,
    };
  },
};
</script>

<template>
  <div class="account">
    <q-icon
      color="yellow"
      name="person"
      class="input-icon"
      fill="yellow"
      size="30px"
    ></q-icon>
  </div>

  <q-menu>
    <div class="data-account row no-wrap q-pa-md">
      <div class="column"></div>

      <div class="column items-center">
        <q-avatar icon="person" size="72px"></q-avatar>

        <div class="data-highlight text-subtitle1 q-mt-md q-mb-xs">{{ account() }}</div>

        <q-btn color="log" label="Sair" @click="logout" push size="sm" />
      </div>
    </div>
  </q-menu>
</template>

<style>
.data-account {
  color: rgb(5, 24, 46);
}

.data-highlight {
  color: rgb(0, 0, 0);
  font-weight: bold;
}
</style>