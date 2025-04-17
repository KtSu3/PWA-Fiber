<script>
import ButtonReturn from './ButtonReturn.vue';
ButtonReturn
</script>

<template>
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <router-link to="index"></router-link>
          </q-avatar>        
        </q-toolbar-title>
        <slot></slot>        
      </q-toolbar>
    </q-header>
</template>
