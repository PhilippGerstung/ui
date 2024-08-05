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
        <div v-if="currentPrices">
            <div class="card" v-for="item in currentPrices.stations" :key="item.id">
                <div class="card-content">
                    <div class="media">
                        <div class="media-left">
                            <figure class="image is-48x48">
                                <img src="https://cdn-icons-png.flaticon.com/512/481/481233.png"
                                    alt="Placeholder image" />
                            </figure>
                        </div>
                        <div class="media-content" style="overflow-y: clip;">
                            <p class="title is-5">
                                {{ item.name }}
                            </p>
                            <p class="subtitle">{{ item.street }} {{ item.houseNumber }}</p>
                        </div>
                        <div class="media-right">
                            {{ item.e5 }} €
                        </div>
                    </div>
                </div>
            </div>
        </div>
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