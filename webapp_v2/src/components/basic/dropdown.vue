<template>
    <div class="select" :class="multiple ? 'is-multiple' : ''">
        <select>
            <option>Select dropdown</option>
            <option>With options</option>
        </select>
    </div>
</template>

<script setup lang="ts">

defineProps<{
    label: string;
    options: string[];
    multiple?: boolean;
}>()

</script>