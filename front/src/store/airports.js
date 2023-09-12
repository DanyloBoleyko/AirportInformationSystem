import api from "@/lib/api.js";

const state = {
    list: [],
    loading: false,
}

const actions = {
    async getAirports({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/airports/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    },
    async getAirport({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/airports/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    },
}

export default {
    namespaced: true,
    actions
}