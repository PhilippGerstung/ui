<template>

    <section class="hero">
        <div class="hero-body">
            <p class="title">Preisabfrage</p>
            <div class="is-flex is-flex-direction-row">
                <button class="button" @click="tryGetGeoLocation">
                    <span class=" icon is-small">
                        <i class="fas fa-map-marker-alt"></i>
                    </span>
                </button>
                <input class="input" type="text" placeholder="PLZ oder Stadt" v-model="userSearch" />
                <button class="button is-primary">
                    <span class="icon is-small">
                        <i class="fas fa-paper-plane"></i>
                    </span>
                </button>
            </div>
        </div>

        {{ userSearch }}
        {{ geoLocation }}
        {{ geoLocationAvailable }}
        {{ currentPrices }}
    </section>

</template>

<script setup lang="ts">
import { getCurrentPricesForLocation } from '@/api/currentPrices';
import type { LocationPrices } from '@/types/currentPrices';
import { ref } from 'vue';


const userSearch = ref("");
const geoLocationAvailable = ref(true);
const geoLocation = ref<{ latitude: number; longitude: number } | null>(null);
const currentPrices = ref<LocationPrices | null>(null);

const tryGetGeoLocation = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            geoLocationAvailable.value = true;
            geoLocation.value = {
                latitude: position.coords.latitude,
                longitude: position.coords.longitude
            };
            getCurrentPricesData();
        });
    } else {
        geoLocationAvailable.value = false;
        geoLocation.value = null;
    }
};

const getCurrentPricesData = async () => {
    if (!geoLocationAvailable.value || geoLocation.value == null) {
        return;
    }

    // Fetch data from API
    currentPrices.value = await getCurrentPricesForLocation(geoLocation.value.latitude, geoLocation.value.longitude);
}
</script>