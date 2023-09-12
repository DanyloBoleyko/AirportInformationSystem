<script setup>
import { computed } from "vue";
import { pythonCaseToCapitalizedWords } from "@/lib/writing.js";

const props = defineProps({
	data: {
		type: Array,
		required: true
	},
	loading: {
		type: Boolean,
		default: false
	},
	height: {
		type: String,
		default: "auto"
	},
	exclude: {
		type: Array,
		default: () => []
	},
	order: {
		type: Array,
		default: () => []
	}
})

const columns = computed(() => {
	let cols = Object.keys(props.data?.[0] || {})
	return cols.filter(col => !props.exclude.includes(col))
})

const orderIndexes = computed(() => {
	const result = props.order
	while (result.length < columns.value.length) {
		result.push(result.length)
	}
	return result
})
</script>

<template>
	<v-row v-if="loading" class="border rounded" align="center" justify="center"
		   no-gutters
		   :style="{ height: height }"
	>
		<v-progress-circular indeterminate color="primary"/>
	</v-row>
	<v-row v-else-if="columns.length === 0" no-gutters>
		<v-alert type="info" :style="{ height: height }">
			No data
		</v-alert>
	</v-row>
	<v-table v-else class="border rounded" :style="{ height: height }">
		<thead>
			<tr>
				<th v-for="(column, i) in columns" :key="column"
					class="text-no-wrap"
					:style="{ order: orderIndexes[i] }"
				>
					<slot :name="'head:' + column">
						{{ pythonCaseToCapitalizedWords(column) }}
					</slot>
				</th>
				<th v-if="$slots.actions" class="text-no-wrap"/>
			</tr>
		</thead>
		<tbody>
			<tr v-for="row in props.data" :key="row.id">
				<td v-for="(column, i) in columns" :key="column"
					:style="{ order: orderIndexes[i] }"
					class="text-no-wrap"
				>
					<slot :name="'cell:' + column" :row="row">
						{{ row[column] }}
					</slot>
				</td>
				<td v-if="$slots.actions" align="right" class="text-no-wrap">
					<slot name="actions" :row="row"/>
				</td>
			</tr>
		</tbody>
	</v-table>
</template>
