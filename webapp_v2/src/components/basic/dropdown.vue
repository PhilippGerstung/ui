<template>
    <div class="select" :class="multiple ? 'is-multiple' : ''">
        <select v-model="selected">
            <option v-for="op, i in options" :key="op + i" :value="op" :selected="op === selected">{{ op }}</option>
        </select>
    </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';


defineProps<{
    label: string;
    options: string[];
    multiple?: boolean;
}>()
const emit = defineEmits(["update:modelValue"])

const selected = ref<string | string[]>('');

watch(selected, (newVal) => {
    emit("update:modelValue", newVal);
})

</script>