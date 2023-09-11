import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { mdi, aliases } from "vuetify/iconsets/mdi"

export default createVuetify({
    components,
    directives,
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
        },
    },
    defaults: {
        global: {},
        VBtn: {
            elevation: 0,
            flat: true,
            class: 'text-capitalize font-weight-medium',
            rounded: "lg",
            minWidth: 44,
            style: {height: '44px'}
        },
        VSelect: {
            variant: 'outlined',
            clearable: true,
            density: 'compact',
            rounded: "lg",
            clearIcon: 'mdi-close',
            hideDetails: 'auto',
        },
        VAlert: {
            variant: 'tonal',
            rounded: 'lg',
        },
        VTable: {
            rounded: 'lg',
            class: 'rounded-lg'
        },
        VTextField: {
            variant: 'outlined',
            rounded: "lg",
            density: 'compact',
            hideDetails: 'auto',
        },
        VCard: {
            rounded: 'lg',
        },
        VCardTitle: {
            class: 'bg-indigo text-h6 py-3'
        },
        VDialog: {
            rounded: 'lg',
            maxWidth: 400,
        },
        VTab: {
            rounded: 't-lg',
            class: 'text-capitalize font-weight-medium',
        }
    },
})