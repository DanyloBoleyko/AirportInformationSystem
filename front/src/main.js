import { createApp } from 'vue'
import App from '@/App.vue'
import 'vuetify/styles'
import routes from '@/routes'
import { createRouter, createWebHistory } from 'vue-router'
import Vuex from 'vuex'
import modules from '@/store'
import vuetify from "@/vuetify.js"
import '@mdi/font/css/materialdesignicons.css'

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const store = new Vuex.Store({
    modules
})

createApp(App)
    .use(vuetify)
    .use(router)
    .use(store)
    .mount('#app')
