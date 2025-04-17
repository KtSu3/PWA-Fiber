<script>
import CompareButton from "@/components/CompareButton.vue";
import SearchCe from "@/components/SearchCe.vue";
import Title1 from "@/components/Title1.vue";
import PowerVerification from "@/components/PowerVerification.vue";

export default {
  components: {
    SearchCe,
    CompareButton,
    Title1,
    PowerVerification,
  },
};
</script>


<template>
  <div>
    <div class="firstQuery">
      <Title1 class="title"> Verificar Potencias </Title1>
    </div>
    <div class="Component"><PowerVerification></PowerVerification></div>
  </div>
</template>

<style scoped>
.title {
  color: rgb(204, 204, 204);
}
.Component {
  margin-left: 4%;
}
.firstQuery {
  margin-top: 30px;
}

@media screen and (min-width: 1024px) {
 
 .title {
   color: rgb(204, 204, 204);
 }

.Component {
 margin-left: 24vw;
 margin-top: 30px;
}

.abc{
 display: contents;
 margin-top: 40px;
}

}
</style>