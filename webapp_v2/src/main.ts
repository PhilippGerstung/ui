import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import dropdown from './components/basic/dropdown.vue'


const app = createApp(App);
app.component('dropdown', dropdown);
app.use(router);
app.mount('#app');
