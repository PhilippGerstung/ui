<template>
    <div class="card">
        <header class="card-header">
            <p class="card-header-title">Impressum</p>
        </header>
        <div class="card-content">
            <div class="content">
                <p>Anbieter:<br />Philipp Gerstung<br />Lutherstr. 7<br />67059 Ludwigshafen am Rhein</p>
                <p>Kontakt:<br />E-Mail: philipp.a.gerstung+gpv@gmail.com<br /></p>
                <p>Bei redaktionellen Inhalten:</p>
                <p>Verantwortlich nach § 55 Abs.2 RStV<br />Philipp Gerstung<br />Lutherstr. 7<br />67059 Ludwigshafen
                    am Rhein</p>
            </div>
            <div class="content">
                <p>App-Version: {{ appVersion }}</p>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';


const appVersion = ref(APP_VERSION)
</script>