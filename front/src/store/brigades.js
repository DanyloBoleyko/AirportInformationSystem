import api from "@/lib/api.js";

const state = {
    list: [],
    loading: false,
}

const actions = {
    async getBrigades({ state }, params) {
        return new Promise((resolve, reject) => {
            state.loading = true
            api.get('/brigades/list', { params })
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
    }
}

export default {
    namespaced: true,
    actions,
    state
}