<template>
  <div class="container">
    <q-page class="q-pa-md">
      <q-card class="q-mt-md">
        <q-card-section class="background">
          <div class="text text-h6 background">Perguntas Frequentes</div>
        </q-card-section>
        
        <q-card-section>
          <q-expansion-item class="text background" group="faq" icon="help" label="Como faço para resetar minha senha?">
            <q-card>
              <q-card-section class="text background">
                Para resetar sua senha entre em contato com NOC, pois login é o mesmo do ixc
              </q-card-section>
            </q-card>
          </q-expansion-item>
          
          <q-expansion-item class="text background" group="faq" icon="help" label="O aplicativo está travando, o que fazer?">
            <q-card>
              <q-card-section class="text background">
                Tente reiniciar o aplicativo ou instalar novamente.
              </q-card-section>
            </q-card>
          </q-expansion-item>
          
          <q-expansion-item class="text background" group="faq" icon="help" label="Como entro em contato com o suporte?">
            <q-card>
              <q-card-section class="text background">
                Solicite contato com NOC referente ao aplicativo
              </q-card-section>
            </q-card>
          </q-expansion-item>
        </q-card-section>
      </q-card>
    </q-page>
  </div>
</template>

<script>
export default {
  name: "HelpPage"
};
</script>

<style>
.text {
    color: black;
}

.developed {
    font-size: 12px;
    color: gray;
    text-align: center;
    margin-top: 20px;
}

.name {
    font-weight: bold;
}
</style>
