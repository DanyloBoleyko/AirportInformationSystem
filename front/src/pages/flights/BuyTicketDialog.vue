<script setup>
import { computed, ref, unref } from "vue";
import usePrice from "@/composables/price.js";
import { useStore } from "vuex";

const props = defineProps({
	modelValue: {
		type: Boolean,
		default: false,
	},
	params: {
		type: Object,
	},
	price: {
		type: Number,
		default: 0,
	},
})

const store = useStore()

const fields = ref({
	name: null,
	passport: null,
	age: null,
	gender: null,
	places: [],
})

const emit = defineEmits(['update:modelValue'])

const model = computed({
	get: () => props.modelValue,
	set: (value) => emit('update:modelValue', value),
})

const valid = ref(false)

const addTicket = () => {
	if (!valid.value) return

	fields.value.place = unref(props.params).place
	fields.value.flight_id = unref(props.params).flight_id

	store.dispatch('tickets/buyTickets', fields.value)

	model.value = false
}
</script>

<template>
	<v-dialog v-model="model"
			  max-width="400"
	>
		<v-card rounded="lg">
			<v-card-title>
				Buy tickets
			</v-card-title>
			<v-form v-model="valid" @submit.prevent="addTicket">
				<v-container>
<!--					<v-row>
						<v-col class="text-caption">
							You selected {{ params.places.join(', ') }} places
						</v-col>
					</v-row>-->
					<v-row>
						<v-col cols="12">
							<v-text-field v-model="fields.name"
										  type="name"
										  label="Name*"
										  :rules="[
											(value) => !!value || 'Required',
										  ]"
							>
							</v-text-field>
						</v-col>
						<v-col cols="12">
							<v-text-field v-model="fields.passport"
										  type="text"
										  label="Passport*"
										  :rules="[
											(value) => !!value || 'Required',
										  ]"
							>
							</v-text-field>
						</v-col>
						<v-col cols="6">
							<v-text-field v-model="fields.age"
										  type="number"
										  label="Age*"
										  placeholder="0"
										  min="1"
										  max="160"
										  :rules="[
											(value) => !!value || 'Required',
										  ]"
							>
							</v-text-field>
						</v-col>
						<v-col cols="6">
							<v-select v-model="fields.gender"
									  :items="[{ label: 'Male', value: 'M' }, { label: 'Female', value: 'F' }]"
									  item-title="label"
									  item-value="value"
									  label="Gender"
							>
							</v-select>
						</v-col>
					</v-row>
				</v-container>
				<v-divider/>
				<v-container>
					<v-row>
						<v-col cols="12">
							<v-btn class="w-100" variant="flat" type="submit" :block="true" color="indigo">
								Buy - {{ usePrice(price) }}
							</v-btn>
						</v-col>
					</v-row>
				</v-container>
			</v-form>
		</v-card>
	</v-dialog>
</template>