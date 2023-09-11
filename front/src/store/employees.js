import api from "@/lib/api.js";

const state = {
    list: [],
    loading: false,
}

const actions = {
    async getEmployees({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/employees/list', { params })
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => {
                    reject(error)
                })
                .finally(() => {
                    state.loading = false
                })
        })
    },

    async addEmployee({ state }, payload) {
        return new Promise((resolve, reject) => {
            state.loading = true
            console.log(payload)
            api.post('/employees/add', payload)
                .then((response) => {
                    console.log(payload)
                    resolve(response)
                    state.list.push(response.data)
                })
                .catch((error) => {
                    console.log(error)
                    reject(error)
                })
                .finally(() => {
                    state.loading = false
                })
        })
    }
}

export default {
    namespaced: true,
    actions,
    state,
}