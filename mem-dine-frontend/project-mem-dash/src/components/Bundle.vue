<script setup lang="ts">
defineProps<{
    title: string
}>()
</script>

<template>
    <article class="bundle-card">
        <h2 class="bundle-title">{{ title }}</h2>
        <button class="edit-button" type="button" :aria-label="`Edit ${title}`">
            <svg viewBox="0 0 16 16" aria-hidden="true">
                <path d="M11.7 1.3a1 1 0 0 1 1.4 0l1.6 1.6a1 1 0 0 1 0 1.4l-8.9 8.9-3.5.8.8-3.5 8.6-9.2ZM2.9 11.1l-.3 1.3 1.3-.3 7.7-7.7-1-1-7.7 7.7Z" />
            </svg>
            <span>Edit</span>
        </button>
    </article>
</template>

<style scoped>
.bundle-card {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: min(100%, 17rem);
    min-height: 9rem;
    padding: 1rem;
    border: 1px solid #e8dfb8;
    border-radius: 0.5rem;
    background: #fffbea;
    color: var(--color-persona-dark);
    box-shadow: 0 2px 5px rgb(0 23 54 / 12%);
    transition: box-shadow 160ms ease, transform 160ms ease;
}

.bundle-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 12px rgb(0 23 54 / 16%);
}

.bundle-title {
    overflow-wrap: anywhere;
    margin: 0;
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.4;
}

.edit-button {
    display: inline-flex;
    align-items: center;
    align-self: flex-end;
    gap: 0.35rem;
    padding: 0.35rem 0.55rem;
    border: 0;
    border-radius: 0.3rem;
    background: transparent;
    color: inherit;
    font: inherit;
    font-size: 0.8rem;
    cursor: pointer;
}

.edit-button:hover,
.edit-button:focus-visible {
    outline: none;
    background: rgb(0 23 54 / 8%);
}

.edit-button:focus-visible {
    box-shadow: 0 0 0 2px var(--color-persona-blue);
}

.edit-button svg {
    width: 0.9rem;
    height: 0.9rem;
    fill: currentColor;
}

@media (prefers-reduced-motion: reduce) {
    .bundle-card {
        transition: none;
    }
}
</style>