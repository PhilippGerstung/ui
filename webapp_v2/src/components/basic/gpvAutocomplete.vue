<template>
    <div class="dropdown is-active full-width" :class="cssClasses">
        <div class="dropdown-trigger full-width" @click="showDropdown = true">
            <div class="field full-width">
                <p class="control is-expanded has-icons-right full-width">
                    <input class="input full-width" type="search" placeholder="Search..." v-model="selected" />
                    <!-- <span class="icon is-small is-right"><i class="fas fa-search"></i></span> -->
                </p>
            </div>
        </div>
        <div class="dropdown-menu full-width" id="dropdown-menu" role="menu" v-if="options.length > 0 && showDropdown">
            <div class="dropdown-content full-width">
                <option v-for="op, i in options" :key="op + i" :value="op" :selected="op === selected"
                    class="is-clickable" @click="dropdownOptionClicked(op)">{{ op }}</option>
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
const showDropdown = ref(true);

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

const dropdownOptionClicked = (option: string) => {
    showDropdown.value = false;
    selected.value = option;
}

</script>

<style scoped>
.full-width {
    width: 100%;
}
</style>