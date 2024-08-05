<template>
  <div>Karte</div>
  <client-only>
    <el-select-v2
      v-model="selectedPlzIndex"
      :options="plzDataWithLabel"
      label="label"
      filterable
      placeholder="Select"
      style="width: 240px"
    >
    </el-select-v2>
  </client-only>

  <div class="card-container" v-if="pricesAtPlz != null">
    <div class="card" v-for="station in pricesAtPlz.stations">
      <div class="card-header">
        {{ station.name }}
        <div v-if="station.isOpen" class="is-open">aktuell geöffnet</div>
        <div v-else class="is-closed">aktuell geschlossen</div>
      </div>
      <div class="card-subheader">
        {{ station.street }} {{ station.houseNumber }}
      </div>
      <div class="card-body">
        <div>
          <div>Diesel {{ station.diesel }} €</div>
          <div>Super {{ station.e5 }} €</div>
          <div>Super (E10) {{ station.e10 }} €</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { loadPlz } from '~/helpers/plz';
import type { ExtendedStationPrices } from '~/server/api/currentPricesAtPostCode.get';
import { type IPlz } from '~/types/plz';

const selectedPlzIndex = ref<number | null>(null);
const plzData = ref<IPlz[]>([]);
const pricesAtPlz = ref<ExtendedStationPrices | null>();

const plzDataWithLabel = computed<IPlz[]>(() => {
  let index = 0;
  return plzData.value.map((plz) => ({
    ...plz,
    label: `${plz.plz} ${plz.city}`,
    value: index++
  }));
});

const selectedPlz = computed<IPlz | null>(() => {
  if (selectedPlzIndex.value === null) {
    return null;
  }
  return plzData.value[selectedPlzIndex.value];
});

watch(selectedPlz, () => {
  getPricesForPlz();
});

const getPricesForPlz = async () => {
  if (!selectedPlz.value) {
    return;
  }
  const response = await $fetch(
    `/api/currentPricesAtPostCode?lat=${selectedPlz.value.lat}&lon=${selectedPlz.value.lon}`
  );
  pricesAtPlz.value = response;
};

onBeforeMount(() => {
  plzData.value = loadPlz();
});
</script>

<style scoped>
.card-container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
  gap: 15px;
}

.card {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 15px;
  border-radius: 10px;
  border: 1px dashed rgb(173, 173, 173);
}

.is-open {
  color: green;
}

.is-closed {
  color: red;
}
</style>
