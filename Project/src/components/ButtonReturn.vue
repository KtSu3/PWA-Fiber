<script>
import { useRouter } from 'vue-router';
import { QIcon } from 'quasar';

export default {
  components: {
    QIcon
  },
  setup() {
    const router = useRouter();

    const back = () => {
      router.back();
    };
    return {
      back
    }
  }
}
</script>

<template v-slot:prepend>
  <div class="q-pa-md q-gutter-sm return icon">
    <q-icon
      color="yellow"
      name="arrow_back"
      class="input-icon"
      @click="back"
      size="30px"
    ></q-icon>
  </div>
</template>

<style>
.return {
  margin-right: 260px;
 
}

.icon {
  max-width: 40px;
  
}
</style>