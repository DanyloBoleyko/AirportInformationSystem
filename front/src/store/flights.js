import api from "@/lib/api.js";

const state = {
    list: [],
    list_by_routes: [],
    loading: false,
    loadingRoutes: false,
}

const actions = {
    async getFlights({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/flights/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    },
    async getFlight({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/flights/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    },
    async getFlightByRoutes({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loadingRoutes = true
            api.get('/flights/route/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list_by_routes = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loadingRoutes = false })
        })
    },
    async getSchedule({ state }, params) {
        return new Promise((resolve, reject) => {
            api.get('/flights/schedule/list', { params })
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => { reject(error) })
        })
    }
}

export default {
    namespaced: true,
    actions
}