<script>
import CompareButton from "@/components/CompareButton.vue";
import SearchCe from "@/components/SearchCe.vue";
import Title1 from "@/components/Title1.vue";
import SearchCe2 from "@/components/SearchCe2.vue";

export default {
  components: {
    SearchCe,
    CompareButton,
    Title1,
    SearchCe2,
  },
};
</script>

<template>
  <div>
    <div class="firstQuery">
      <Title1 class="title"> Primeira Consulta </Title1>
    </div>
    <div class="Component">
      <SearchCe></SearchCe>
    </div>
<div class="abc">
  <div class="secondQuery">
      <Title1 class="title"> Segunda consulta </Title1>
    </div>
    <div class="Component">
          <SearchCe2></SearchCe2>
      </div>
  </div>
</div>
</template>

<style scoped>

.title{
  color: rgb(204, 204, 204);
}
.firstQuery {
  margin-top: 8%;
}

.secondQuery {
  margin-top: 50px;
}

.compare {
  margin-top: 100px;
  margin-left: 113px;
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