<script setup>
import { useDateFormat } from "@vueuse/core";
import { ref } from "vue";
import { useStore } from "vuex";
import usePrice from "@/composables/price.js";

const props = defineProps({
	flight: {
		type: Object,
		required: true,
	},
	aircraft: {
		type: Object,
		required: true,
	},
	schedule: {
		type: Object,
		required: true,
	},
	freePlaces: {
		type: Array,
		default: () => [],
	}
})

const store = useStore()

const loadingAircraftType = ref(false)
const aircraftType = ref(null)

const getAircraftType = () => {
	loadingAircraftType.value = true
	store.dispatch('aircrafts/getAircraftTypes', {
		aircraft_type_id: props.aircraft.aircraft_type_id,
	})
		.then(({ data }) => {
			aircraftType.value = data?.[0]
		})
		.finally(() => loadingAircraftType.value = false)
}

getAircraftType()
</script>

<template>
	<v-card :flat="true" border>
		<v-card-title>Information</v-card-title>

		<v-card-text>
			<v-row>
				<v-col>
					<v-list>
						<v-list-item>
							<v-list-item-title>Departure</v-list-item-title>
							<v-list-item-subtitle>{{
									useDateFormat(flight.departure_datetime, 'YYYY-MM-DD HH:mm').value
								}}
							</v-list-item-subtitle>
						</v-list-item>
						<v-list-item>
							<v-list-item-title>Arrival</v-list-item-title>
							<v-list-item-subtitle>{{
									useDateFormat(flight.arrival_datetime, 'YYYY-MM-DD HH:mm').value
								}}
							</v-list-item-subtitle>
						</v-list-item>
						<v-list-item v-if="!loadingAircraftType">
							<v-list-item-title>Airplane</v-list-item-title>
							<v-list-item-subtitle>{{ aircraft.name }}, {{ aircraft.aircraft_type_name }}</v-list-item-subtitle>
						</v-list-item>
					</v-list>
				</v-col>
				<v-col>
					<v-list>
						<v-list-item>
							<v-list-item-title>Ticket price</v-list-item-title>
							<v-list-item-subtitle>{{ usePrice(schedule?.ticket_price_discounted) }}</v-list-item-subtitle>
						</v-list-item>
						<v-list-item>
							<v-list-item-title>Places</v-list-item-title>
							<v-list-item-subtitle>{{ aircraft.aircraft_type_place_count }}</v-list-item-subtitle>
						</v-list-item>
						<v-list-item>
							<v-list-item-title>Free places</v-list-item-title>
							<v-list-item-subtitle>{{ freePlaces.length }}</v-list-item-subtitle>
						</v-list-item>
					</v-list>
				</v-col>
			</v-row>
		</v-card-text>
	</v-card>
</template>