<template>

    <section class="hero">
        <div class="hero-body">
            <p class="title">Preisabfrage</p>
            <p class="subtitle">
                <input class="input" type="text" placeholder="PLZ oder Stadt" v-model="userSearch" />
            </p>
        </div>

        {{ userSearch }}
    </section>

</template>

<script setup lang="ts">
import { ref } from 'vue';


const userSearch = ref("");
</script>