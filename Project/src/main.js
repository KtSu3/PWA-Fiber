import './assets/main.css';
import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import router from './router';
import { Quasar, Notify, Dialog } from 'quasar';
import '@quasar/extras/material-icons/material-icons.css';
import 'quasar/src/css/index.sass';
import langBR from 'quasar/lang/pt-BR.js';


axios.defaults.timeout = 10000;

const app = createApp(App);
app.use(router);

app.use(Quasar, {
  lang: langBR,
  plugins: { Notify, Dialog },
  config: {},
});

//Service Worker (PWA)
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/Frontend/Project/')
      .then((registration) => {
        console.log('Service Worker registrado com sucesso:', registration);

        // Detectar atualizações no SW
        registration.onupdatefound = () => {
          const installingWorker = registration.installing;
          if (installingWorker) {
            installingWorker.onstatechange = () => {
              if (installingWorker.state === 'installed') {
                if (navigator.serviceWorker.controller) {
                  // console.log('Novo conteúdo disponível, atualize a página.');
                } else {
                  // console.log('Conteúdo foi cacheado para uso offline.');
                }
              }
            };
          }
        };
      })
      .catch((error) => {
        // console.error('Falha ao registrar o Service Worker:', error);
      });
  });
}
app.mount('#app');
