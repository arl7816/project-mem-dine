<script setup lang="ts">
import { ref } from 'vue';
import Bundle from './Bundle.vue';

const bundles = ref([
    "bundle 1", "bundle 2", "bundle 3"
])

const draggingIndex = ref<number | null>(null)

function startBundleDrag(index: number, event: DragEvent) {
    draggingIndex.value = index
    event.dataTransfer?.setData('text/plain', String(index))
    if (event.dataTransfer) {
        event.dataTransfer.effectAllowed = 'move'
    }
}

function dropBundle(targetIndex: number) {
    const sourceIndex = draggingIndex.value
    if (sourceIndex === null || sourceIndex === targetIndex) return

    const bundle = bundles.value[sourceIndex]
    if (bundle === undefined) return

    bundles.value.splice(sourceIndex, 1)
    const newIndex = sourceIndex < targetIndex ? targetIndex - 1 : targetIndex
    bundles.value.splice(newIndex, 0, bundle)
    draggingIndex.value = null
}

</script>

<template>
    <div class="bundles">
        <Bundle
            v-for="(bundle, index) in bundles"
            :key="bundle"
            :title="bundle"
            :class="{ 'is-dragging': draggingIndex === index }"
            draggable="true"
            @dragover.prevent
            @dragstart="startBundleDrag(index, $event)"
            @drop.prevent="dropBundle(index)"
            @dragend="draggingIndex = null"
        />
    </div>
</template>

<style scoped>

.bundles{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    align-content: center;
    gap: 10px;
    justify-content: center;
    min-height: 100vh;
}

</style>