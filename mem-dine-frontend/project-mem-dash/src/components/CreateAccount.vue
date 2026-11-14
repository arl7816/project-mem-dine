
<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { userService, type ApiErrorResponse } from '../../api/services/userService'

const router = useRouter()

// Reactive form values
const username = ref('')
const password = ref('')
const confirmPassword = ref('')

// Reactive error message
const errorMessage = ref('')

function hasConfirmInformationIsEntered(): any{
    return username.value.trim() && password.value && confirmPassword.value; 
}

function checkPasswordLength(){
    return password.value.length >= 12 && password.value.length <= 1024
}

function doPasswordsMatch(){
    return password.value === confirmPassword.value; 
}

function sendToLogInPage(){
    router.push({
        name: 'login',
        query: {
            accept: 'Account Created. Please Attempt a sign in'
        }
    });
}

async function completeCreateAccount() {
    // Reset previous error
    errorMessage.value = ''

    // step 1: confirm info is inputted correctly
    if (hasConfirmInformationIsEntered() == false){
        errorMessage.value = "Please complete all fields."
        return
    }

    // step 2: confirm password strength
    if (checkPasswordLength() == false){
        errorMessage.value = "Password must be between 12 and 1024 characters"
        return
    }

    // step 2: confirm passwords match
    if (doPasswordsMatch() == false){
        errorMessage.value = "Passwords must match"
        return
    }

    // step 3: attempt to create the user
    const response = await userService.createUser({
        username: username.value,
        password: password.value
    }); 

    // step 4: confirm it worked, if not, report issue
    if (!response || response.status !== 'success') {
        const errorData = response?.data as ApiErrorResponse
        errorMessage.value = errorData?.error ?? 'Something went wrong.'
        return
    }


    // step 5: send them to the log in page as this must have worker
    sendToLogInPage();
}
</script>

<template>
    <div class="page-container">
        <div class="log-in-box">

            <div class="sign-in-fields">
                <h1 class="title">Create Account</h1>

                <div class="input-fields">
                    <input
                        v-model="username"
                        type="text"
                        placeholder="Username"
                        class="text-input"
                        @keydown.enter="completeCreateAccount"
                    >

                    <input
                        v-model="password"
                        type="password"
                        placeholder="Password"
                        class="text-input"
                        @keydown.enter="completeCreateAccount"
                    >

                    <input
                        v-model="confirmPassword"
                        type="password"
                        placeholder="Confirm Password"
                        class="text-input"
                        @keydown.enter="completeCreateAccount"
                    >
                </div>

                <!-- Error message -->
                <p v-if="errorMessage" class="error-message" role="alert">
                    {{ errorMessage }}
                </p>

                <RouterLink class="link" to="/">Sign In</RouterLink>
            </div>

            <div class="button-container">
                <input
                    type="button"
                    value="Create"
                    class="log-in-button"
                    @click="completeCreateAccount"
                >
            </div>

        </div>
    </div>
</template>


<style scoped>
/* Main Container Layout */
.log-in-box {
    position: relative;
    /* Allows absolute positioning for the button container */
    display: flex;
    flex-direction: column;
    justify-content: center;
    /* Centers the fields vertically */
    align-items: center;
    /* Centers the fields horizontally */

    border: 1.5px solid var(--color-persona-dark, #001222);
    /* Fallback dark color */
    width: 584px;
    height: 433px;
    border-radius: 51px;
    box-sizing: border-box;
    padding: 40px;
}

/* Center Content Stack */
.sign-in-fields {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.title {
    font-size: 2rem;
    font-weight: normal;
    margin-bottom: 24px;
    font-family: sans-serif;
}

/* Form Fields */
.input-fields {
    display: flex;
    flex-direction: column;
    gap: 12px;
    /* Spacing between Username and Password */
    width: 100%;
    max-width: 500px;
    /* Adjust width to match image constraints */
    margin-bottom: 16px;
}

.text-input {
    width: 100%;
    height: 32px;
    padding: 4px 12px;
    border: 1px solid var(--color-soft-gray);
    /* Gray borders matching the image */
    border-radius: 6px;
    box-sizing: border-box;
    font-size: 0.9rem;
}

.text-input::placeholder {
    color: var(--color-soft-gray);
    /* Soft gray placeholder text */
}

/* Button Positioning & Styling */
.button-container {
    position: absolute;
    bottom: 24px;
    right: 24px;
}

.log-in-button {
    background-color: var(--color-persona-blue);
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

.log-in-button:hover {
    background-color: var(--color-persona-orange);
    transform: scale(1.05);
}

.page-container {
    display: grid;
    place-items: center;
    /* Centers horizontally and vertically */
    min-height: 100vh;
    /* Forces container to fill 100% of the viewport height */
    margin: 0;
    /* Prevents default browser padding/margin scrollbars */
    background-color: #ffffff;
    /* Optional: background color for the screen */
}

</style>
