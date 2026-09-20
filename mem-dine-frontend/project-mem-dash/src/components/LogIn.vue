<script setup lang="ts">
// If needed, import RouterLink here depending on your project setup
</script>

<template>
  <!-- General log in box -->
  <div class="log-in-box">
    <!-- sign in portion (centered vertically and horizontally) -->
    <div class="sign-in-fields">
      <h1 class="title">Sign In</h1>
      <!-- Input fields-->
      <div class="input-fields">
        <input type="text" placeholder="Username" class="text-input">
        <input type="password" placeholder="Password" class="text-input">
      </div>
      <RouterLink class="link" to="/create-account">Create Account</RouterLink>
    </div>
    
    <!-- log in button wrapper (pushed to the bottom right) -->
    <div class="button-container">
      <input type="button" value="Log In" class="log-in-button">
    </div>
  </div>
</template>

<style scoped>
/* Main Container Layout */
.log-in-box {
  position: relative; /* Allows absolute positioning for the button container */
  display: flex;
  flex-direction: column;
  justify-content: center; /* Centers the fields vertically */
  align-items: center;    /* Centers the fields horizontally */
  
  border: 1.5px solid var(--color-persona-dark, #001222); /* Fallback dark color */
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
  gap: 12px; /* Spacing between Username and Password */
  width: 100%;
  max-width: 500px; /* Adjust width to match image constraints */
  margin-bottom: 16px;
}

.text-input {
  width: 100%;
  height: 32px;
  padding: 4px 12px;
  border: 1px solid var(--color-soft-gray); /* Gray borders matching the image */
  border-radius: 6px;
  box-sizing: border-box;
  font-size: 0.9rem;
}

.text-input::placeholder {
  color: var(--color-soft-gray); /* Soft gray placeholder text */
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
</style>
