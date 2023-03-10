<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Data Stories Lead Generation</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav mx-5">
              <li class="nav-item">
                <RouterLink class="menu-item" to="/">Home</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink class="menu-item" to="/settings">Settings</RouterLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>

    <RouterView />
</template>

<style scoped>
header {
  width: 100vw;
}

.menu-item {
  margin: 0 1rem;
  text-decoration: none;
  color: darkgray;
}

.router-link-active {
  color: black;
}

</style>
