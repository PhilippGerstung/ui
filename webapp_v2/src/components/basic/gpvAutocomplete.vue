<template>
    <div class="dropdown is-active" :class="cssClasses">
        <div class="dropdown-trigger">
            <div class="field">
                <p class="control is-expanded has-icons-right">
                    <input class="input" type="search" placeholder="Search..." v-model="selected" />
                    <!-- <span class="icon is-small is-right"><i class="fas fa-search"></i></span> -->
                </p>
            </div>
        </div>
        <div class="dropdown-menu" id="dropdown-menu" role="menu">
            <div class="dropdown-content">
                <option v-for="op, i in options" :key="op + i" :value="op" :selected="op === selected">{{ op }}</option>
            </div>
        </div>
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