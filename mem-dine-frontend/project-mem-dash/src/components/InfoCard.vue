<script setup lang="ts">
defineProps<{
    title: string
}>()

const emit = defineEmits<{
    select: [title: string]
}>()
</script>

<template>
    <button class="card" type="button" @click="emit('select', title)">
        <span>{{ title }}</span>
    </button>
</template>

<style scoped>
.card {
    box-sizing: border-box;
    display: flex;
    align-items: center;
    width: min(55%, 32rem);
    min-height: 50px;
    padding: 0 12px;
    border: 1.5px solid var(--color-black);
    border-radius: 5px;
    background: var(--color-white);
    color: var(--color-black);
    text-align: left;
    cursor: pointer;
    transition:
        width 750ms ease,
        min-height 750ms ease,
        margin 750ms ease,
        box-shadow 750ms ease;
}

.card:hover,
.card:focus-visible {
    z-index: 1;
    width: min(65%, 38rem);
    min-height: 72px;
    margin-block: 8px;
    box-shadow: 0 5px 14px rgb(0 23 54 / 14%);
}

.card span {
    transition: font-size 750ms ease;
}

.card:hover span,
.card:focus-visible span {
    font-size: 1.25rem;
}

@media (prefers-reduced-motion: reduce) {
    .card,
    .card span {
        transition-duration: 0.01ms;
    }
}
</style>
