import type { GasType } from "@/types/currentPrices";
import { ref, watch } from "vue";

export const selectedGasType = ref<GasType>("e5");

watch(selectedGasType, (newValue) => {
    // Store the settings in localStorage
    localStorage.setItem("gpv-selectedGasType", newValue);
});


function initValuesFromLocalStorage() {
    const gt = localStorage.getItem("gpv-selectedGasType");
    if (gt && ["diesel", "e5", "e10"].includes(gt)) {
        selectedGasType.value = gt as GasType;
    }
};
initValuesFromLocalStorage();