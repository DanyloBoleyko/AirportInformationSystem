import api from "@/lib/api.js";

const state = {
    list: [],
    types_list: [],
    loading: false,
    loadingTypes: false,
}

const actions = {
    async getAircrafts({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/aircrafts/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    },
    async getAircraft({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/aircrafts/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    },
    async getAircraftTypes({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loadingTypes = true
            api.get('/aircrafts/type/list', { params })
                .then((response) => {
                    resolve(response)
                    state.types_list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loadingTypes = false })
        })
    },
}

export default {
    namespaced: true,
    actions
}