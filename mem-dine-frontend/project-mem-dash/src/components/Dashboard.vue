
<script setup lang="ts">


</script>

<template>
    <div class="header">
        <div class="title">
            Placeholder text
        </div>
        
        <div class="button-container">
            <input type="button" value="Log Out" class="log-out-button">
        </div>

    </div>

    <div class="main-body">
        <div class="card">
            <p>Card 1</p>
        </div>
        <div class="card">
            <p>Card 2</p>
        </div>
        <div class="card">
            <p>Card 3</p>
        </div>
    </div>

    <div class="footer">

    </div>
</template>


<style scoped>

.main-body{
    display: flex;
    flex-direction: column;
    justify-content: center; /* Horizontal centering */
    align-items: center;     /* Vertical centering */
    height: 100vh;           /* Container needs a defined height */
    gap: 1vh; 
}

.card{
    border: 1.5px solid var(--color-black);
    border-radius: 5px;
    min-width: 25%;
    min-height: 50px;
    align-items: center 
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

</style>
