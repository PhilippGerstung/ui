import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import dropdown from './components/basic/gpvDropdown.vue'
import autocomplete from './components/basic/gpvAutocomplete.vue'



const app = createApp(App);
app.component('gpvDropdown', dropdown);
app.component('gpvAutocomplete', autocomplete);
app.use(router);
app.mount('#app');
