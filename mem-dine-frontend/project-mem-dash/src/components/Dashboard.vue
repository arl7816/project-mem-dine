
<script setup lang="ts">
import { ref, watch } from 'vue'
import InfoCard from './InfoCard.vue'
import { useRouter } from 'vue-router'
import { userService } from '../../api/services/userService.ts';

const router = useRouter();

const cards = ['Card 1', 'Card 2', 'Card 3']
const selectedCard = ref<string | null>(null)
const detailsDialog = ref<HTMLDialogElement | null>(null)

watch(selectedCard, (title) => {
    if (title) {
        detailsDialog.value?.showModal()
    }
})

function closeDetails() {
    detailsDialog.value?.close()
}

function clearSelection() {
    selectedCard.value = null
}

// TODO: this method still needs to be finished later
async function logOut(){
    const response = await userService.logout(); 

    if (response.status = 'success'){
        router.push({
            name: 'login',
            query: {
                accept: 'You have been logged out'
            }
        })   
    }
}

</script>

<template>
    <div class="header">
        <div class="title">
            Placeholder text
        </div>
        
        <div class="button-container">
            <input type="button" value="Log Out" class="log-out-button"
            @click="logOut">
        </div>

    </div>

    <div class="main-body">
        <InfoCard
            v-for="card in cards"
            :key="card"
            :title="card"
            @select="selectedCard = $event"
        />
    </div>

    <dialog
        ref="detailsDialog"
        class="details-dialog"
        aria-labelledby="details-title"
        @click.self="closeDetails"
        @close="clearSelection"
    >
        <button class="close-button" type="button" aria-label="Close details" @click="closeDetails">
            &times;
        </button>
        <h2 id="details-title">{{ selectedCard }}</h2>
        <div class="description">
            <p>This is a description</p>
        </div>
        <div class="links">
            <p>Links <span aria-hidden="true">&#128279;</span></p>
            <a href="#link-1" @click.prevent>Link 1</a>
            <a href="#link-2" @click.prevent>Link 2</a>
        </div>
    </dialog>

    <div class="footer">

    </div>
</template>


<style scoped>

.main-body{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    gap: 1vh;
}

.title {
    font-size: 2rem;
    font-weight: normal;
    margin-bottom: 24px;
    font-family: sans-serif;
}

.button-container {
    position: absolute;
    bottom: 24px;
    right: 24px;
}

.header{
    border-bottom: 2px solid var(--color-black);
    padding-bottom: 50px;
    width: 100%; 
    position: fixed;
}

.footer{
    border-top: 2px solid var(--color-black);
    padding-top: 70px;
    width: 100%;
    bottom: 0;
    left: 0; 
    position: fixed;
}

.log-out-button {
    background-color: var(--color-white);
    border: 1.5px solid var(--color-persona-dark);
    border-radius: 100px;
    height: 48px;
    width: 96px;
    text-align: center;
    font-size: 1rem;
    font-weight: 500;
    box-sizing: border-box;
    cursor: pointer;
}

.details-dialog {
    box-sizing: border-box;
    width: min(90vw, 32rem);
    max-width: none;
    padding: 2rem 1rem 1.5rem;
    overflow: visible;
    border: 0;
    background: var(--color-white);
    color: var(--color-black);
}

.details-dialog::backdrop {
    background: rgb(0 0 0 / 45%);
}

.close-button {
    position: absolute;
    top: 0.4rem;
    right: 0.5rem;
    border: 0;
    background: transparent;
    color: var(--color-persona-dark);
    font-size: 1.75rem;
    line-height: 1;
    cursor: pointer;
}

.details-dialog h2 {
    margin: 0 0 1.5rem;
    padding: 0 0 0.15rem 0.35rem;
    border-bottom: 1px solid var(--color-black);
    font-size: 1.5rem;
    font-weight: 400;
}

.description {
    display: flex;
    min-height: 11rem;
    align-items: center;
    padding: 0.4rem;
    border: 1.5px solid var(--color-persona-dark);
    border-radius: 9px;
}

.description p {
    margin: 0;
}

.links {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.25rem;
    padding: 0 0.2rem;
}

.links p {
    margin: 0;
}

.links a {
    color: #0085a3;
    font-style: italic;
    text-decoration: underline;
}

</style>
