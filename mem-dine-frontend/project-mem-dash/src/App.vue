<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import LogIn from './components/LogIn.vue';
</script>

<template>
  <header>
    <LogIn />
  </header>
</template>

<style>
@import './assets/base.css';

@import url('https://googleapis.com');

/* 2. Apply it globally to the body or app container */
#app {
  font-family: 'Poppins', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.link{
  color: var(--color-persona-blue)
}

.link:hover{
  color: var(--color-persona-orange);
}

</style>
