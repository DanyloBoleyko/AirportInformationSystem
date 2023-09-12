import api from "@/lib/api.js";

const state = {
    list: [],
    loading: false,
}

const actions = {
    async getTickets({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/tickets/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    },
    async buyTickets({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.post('/tickets/buy', params)
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    }
}

export default {
    namespaced: true,
    actions
}