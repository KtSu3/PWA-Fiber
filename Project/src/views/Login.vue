<template>
  <main id="container">
    <q-form @submit.prevent="handleSubmit" id="LoginForm">
      <div id="form_header">
        <img
          src="../components/icons/imgs/font-removebg-preview.png"
          alt="Logo"
          class="logo"
        />
        <q-icon id="mode_icon" name="moon" @click="toggleMode" />
      </div>

      <div id="inputs">
        <div class="input-box">
          <q-input v-model="username" label="Email" required>
            <template v-slot:prepend>
              <q-icon color="yellow" name="person" class="input-icon"> </q-icon>
            </template>
          </q-input>
        </div>

        <div class="input-box">
          <q-input v-model="password" label="Senha" type="password" required>
            <template v-slot:prepend>
              <q-icon color="yellow" name="lock" class="input-icon"> </q-icon>
            </template>
          </q-input>
        </div>
      </div>

      <div v-if="errorMessage" id="errorMessage">{{ errorMessage }}</div>
      
      <q-btn
        class="text-primary"
        label="Login"
        id="login_button"
        @click="handleSubmit"
        color="log"
      />
      
    </q-form>
    
  </main>
</template>

<script>
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    async handleSubmit() {
      if (!this.username || !this.password) {
        this.errorMessage = "Por favor, preencha todos os campos.";
        return;
      }

      try {
        const loginResponse = await axios.post(
          "URL Login",
          {
            email: this.username,
            password: this.password,
          }
        );

        // Verificar se o login foi bem-sucedido
        if (loginResponse.status === 200 && loginResponse.data.user) {
          const user = loginResponse.data.user;

          // Salvar o usuário no localStorage
          localStorage.setItem("user", JSON.stringify(user));

          return this.router.push({ name: "index" });
        } else {
          throw new Error("Usuário ou senha inválidos.");
        }
      } catch (error) {
        console.error("Erro no login:", error);
        this.errorMessage = "Erro ao tentar fazer login. Tente novamente.";
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400&display=swap");

.logo {
  display: flex;
  margin: auto;
  max-width: 100%;
  height: auto;
}

* {
  font-family: "Poppins", sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#container {
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: var(--color-gradient);
  padding: 20px;
}

#LoginForm {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 450px;
  background-color: #053499f1;
  padding: 35px;
  border-radius: 8px;
  gap: 20px;
  box-shadow: 15px 15px 50px rgba(0, 0, 0, 0.781);
  margin-left: 27px;
}

#form_header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

#form_header h1 {
  font-size: 32px;
}

#errorMessage {
  color: rgb(0, 0, 0);
}

#login_button {
  font-size: 18px;
}

@media screen and (max-width: 500px) {
  #LoginForm {
    padding: 20px;
    gap: 1px;
    margin-right: 15%;
    margin-right: 10%;
  }

  #form_header h1 {
    font-size: 28px;
  }

  #login_button {
    font-size: 20px;
  }
}

@media screen and (min-width: 1024px) {
  #container {
    padding: 40px;
  }

  #LoginForm {
    width: 400px;
    padding: 30px;
    gap: 30px;
  }

  #form_header h1 {
    font-size: 40px;
  }

  #login_button {
    font-size: 20px;
  }
}
</style>