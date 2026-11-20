<script setup lang="ts">
import { ref } from 'vue';
import Bundle from './Bundle.vue';

const bundles = ref([
    "bundle 1", "bundle 2", "bundle 3"
])

</script>

<template>
    <div class="bundles">
        <Bundle 
            v-for="bundle in bundles"
            :key="bundle"
            :title="bundle"
        />
    </div>
</template>

<style scoped>

.bundles{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    align-content: center;
    gap: 5px;
    justify-content: center;
    min-height: 100vh;
}

</style>