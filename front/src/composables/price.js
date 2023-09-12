import { unref } from "vue";

export default function usePrice(price) {
    return `${((unref(price) || 0) / 100).toFixed(2)} €`
}