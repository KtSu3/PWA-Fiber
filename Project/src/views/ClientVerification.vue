<script>
import SearchClient from '@/components/SearchClient.vue';
import Title1 from '@/components/Title1.vue';


export default {
  components: {
    SearchClient,
    Title1
    
  },
};

</script>

<template>

<div class="verification">
    <Title1 class="title">Verificar Historico do Cliente</Title1>

    <div class="Teste">
      <SearchClient></SearchClient>
    </div>
    

</div>

</template>

<style scoped>

.title {
  color: rgb(204, 204, 204);
}
.verification{
    margin-top: 8%;
}

.Teste {
  margin-left: 4%;
}

@media screen and (min-width: 1024px) {
 
 .title {
   color: rgb(204, 204, 204);
 }

.Teste {
 margin-left: 24vw;
 margin-top: 30px;
}

.abc{
 display: contents;
 margin-top: 40px;
}

}
</style>