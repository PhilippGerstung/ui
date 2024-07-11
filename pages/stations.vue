<template>Tankstellen

    <div>{{stations}}</div>
</template>
<script setup lang="ts">
import type { IStation } from '~/types/stations';

const stations = ref<IStation[]>([]);

const loadStations = async () => {
  const response = await useFetch('/api/stations');
  if(response.data.value != null) stations.value = response.data.value;
  else stations.value = [];
};

onMounted(() => {
  loadStations();
});
</script>