<script setup lang="ts">
</script>

<template>
    <!-- General log in box -->
    <div class="log-in-box center">
        <!-- sign in portion -->
        <div class="sign-in-fields">
            <label>Sign In</label>
            <!-- Input fields-->
            <div class="input-fields">
                <input placeholder="Username">
                <input placeholder="Password">
            </div>
            <RouterLink class="link" to="/create-account">Create Account</RouterLink>
        </div>
        <!-- log in button -->
        <div>
            <input type="button" value="Log In" class="log-in-button">
        </div>
    </div>
</template>

<style scoped>
.log-in-box{
    border: 1.5px solid var(--color-persona-dark);
    width: 584px;
    height: 433px;
    border-radius: 51px;
}

.input-fields{
    display: grid;
}

.center{
    display: grid;
    place-items: center;
}

.log-in-button{
    background-color: var(--color-persona-blue);
    border: 0.5px solid var(--color-persona-dark);
    border-radius: 100px;
    padding: 12px 20px; 
    height: 48px;
    width: 87px; 

    text-align: center;
    font-size: 1rem;
}

.log-in-button:hover{
    background-color: var(--color-persona-orange);
    transform: scale(1.05);
    cursor: pointer; 
}

</style>