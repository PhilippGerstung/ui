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
            <div class="card" v-for="item in currentPricesSorted" :key="item.id">
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
                            <p class="subtitle">
                                <a :href="`https://www.google.com/maps/search/?api=1&query=${item.street} ${item.houseNumber}, ${item.postCode} ${item.place}`"
                                    target="_blank">
                                    {{ item.place }}
                                    {{ item.street }} {{ item.houseNumber }}
                                </a>
                            </p>
                            <p class="subtitle" v-if="geoLocation != null">
                                {{ Math.abs(distance(item.lat, item.lng, geoLocation.latitude,
                                    geoLocation.longitude)).toFixed(1) }}
                                km entfernt
                            </p>
                        </div>
                        <div class="media-right">
                            {{ item[selectedGasType] }} €
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

</template>

<script setup lang="ts">
import { getCurrentPricesForLocation } from '@/api/currentPrices';
import type { GasType, LocationPrices, Station } from '@/types/currentPrices';
import { computed, onMounted, ref } from 'vue';
import { kmDistanceBetweenCoordinates } from "@/helper/geoHelper"
import { selectedGasType } from '@/stores/userSettings';

const userSearch = ref("");
const geoLocationAvailable = ref(true);
const geoLocation = ref<{ latitude: number; longitude: number } | null>(null);
const currentPrices = ref<LocationPrices | null>(null);

const currentPricesSorted = computed<Station[] | null>(() => {
    if (currentPrices.value == null) {
        return null;
    }

    const sorted = [...currentPrices.value.stations].sort((a, b) => {
        return a[selectedGasType.value] - b[selectedGasType.value];
    });
    return sorted;
});

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

const distance = kmDistanceBetweenCoordinates;

onMounted(() => {
    tryGetGeoLocation();
});
</script>