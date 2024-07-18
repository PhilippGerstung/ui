<template>
  <div class="full-height">
    Tankstellen
    <ag-grid
      :columnDefs="colDef"
      :rowData="stations"
      style="height: 500px"
    ></ag-grid>
  </div>
</template>
<script setup lang="ts">
import type { IStation } from '~/types/stations';
import type { ColDef } from 'ag-grid-community';

const stations = ref<IStation[]>([]);

const colDef: ColDef<IStation>[] = [
  {
    field: 'uuid',
    headerName: 'UUID'
  },
  {
    field: 'name',
    headerName: 'Name'
  }
];

const loadStations = async () => {
  const response = await useFetch('/api/stations');
  if (response.data.value != null) stations.value = response.data.value;
  else stations.value = [];
};

onMounted(() => {
  loadStations();
});
</script>

<style lang="scss" scoped>
.full-height {
  height: 100%;
  display: flex;
  flex-direction: column;
}
</style>
