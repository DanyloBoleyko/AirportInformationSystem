import api from "@/lib/api.js";

const state = {
    list: [],
    loading: false,
}

const actions = {
    async getDepartments({ state }) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/departments/list')
                .then((response) => {
                    resolve(response)
                    state.list = response.data
                })
                .catch((error) => { reject(error) })
                .finally(() => { state.loading = false })
        })
    },
    async createDepartment({ state }, payload) {
        return new Promise((resolve, reject) => {
            api.post('/departments/add', payload)
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => { reject(error) })
        })
    },
    async updateDepartment({ state }, payload) {
        return new Promise((resolve, reject) => {
            api.put('/departments/update', payload)
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => { reject(error) })
        })
    },
    async deleteDepartment({ state }, payload) {
        return new Promise((resolve, reject) => {
            api.delete('/departments/delete', { data: payload })
                .then((response) => {
                    resolve(response)
                })
                .catch((error) => { reject(error) })
        })
    }
}

export default {
    namespaced: true,
    actions,
    state
}