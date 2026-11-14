<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import LogIn from './components/LogIn.vue';
</script>

<template>
  <header>
    <RouterView />
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
  color: var(--color-persona-blue);
  text-decoration: underline;
  font-size: 0.9rem;
  cursor: pointer;
}

.link:hover{
  color: var(--color-persona-orange);
}

.error-message {
  color: #dc2626;
  font-size: 0.85rem;
  margin: 0 0 12px;
  text-align: center;
}

.accept-message{
  color: #006920;
  font-size: 0.85rem;
  margin: 0 0 12px;
  text-align: center;

}

</style>
