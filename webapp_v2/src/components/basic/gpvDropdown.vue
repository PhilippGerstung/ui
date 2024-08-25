<template>
    <div class="select" :class="cssClasses">
        <select v-model="selected">
            <option v-for="op, i in options" :key="op + i" :value="op" :selected="op === selected">{{ op }}</option>
        </select>
    </div>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue';


const props = defineProps<{
    label: string;
    options: string[];
    multiple?: boolean;
    loading?: boolean;
}>()
const emit = defineEmits(["update:modelValue"])

const selected = ref<string | string[]>('');

watch(selected, (newVal) => {
    emit("update:modelValue", newVal);
})

const cssClasses = computed<string>(() => {
    return [
        'select',
        props.multiple ? 'is-multiple' : '',
        props.loading ? 'is-loading' : ''
    ].join(' ');
})

</script>