<script setup>
import { useDateFormat } from "@vueuse/core";
import { computed } from "vue";
import { useStore } from "vuex";

defineProps({
	flights: {
		type: Array,
		default: () => [],
	},
	loading: {
		type: Boolean,
		default: false,
	},
})

const store = useStore()

const loadingAirports = computed(() => store.state.airports.loading)
const airports = computed(() => store.state.airports.list)

const getAirports = () => {
	store.dispatch('airports/getAirports')
}

const airportToString = (airport_id) => {
	const airport = airports.value?.find(a => a.airport_id === airport_id)

	return `${airport?.name} (${airport?.city}, ${airport?.country})`
}

const statusColor = (status) => {
	switch (status) {
		case 'Заплановано':
			return 'blue'
		case 'Завершено':
			return 'green'
		case 'Відкладено':
			return 'deep-orange'
		case 'В процесі':
			return 'orange'
		case 'Скасовано':
			return 'red'
		default:
			return 'grey'
	}
}

getAirports()
</script>

<template>
	<v-card :flat="true" border>
		<v-card-title>
			<h2 class="text-h6">Flights</h2>
		</v-card-title>
		<v-card-text>
			<v-row v-for="(flight, i) in flights">
				<v-col v-if="i !== 0" cols="12" class="py-0">
					<v-divider class="my-0"/>
				</v-col>
				<v-col>
					<v-list>
						<v-list-item>
							<v-list-item-title>Departure</v-list-item-title>
							<v-list-item-subtitle>{{ useDateFormat(flight.departure_datetime, 'YYYY-MM-DD HH:mm:ss').value }}</v-list-item-subtitle>
						</v-list-item>
						<v-list-item>
							<v-list-item-title>Arrival</v-list-item-title>
							<v-list-item-subtitle>{{ useDateFormat(flight.arrival_datetime, 'YYYY-MM-DD HH:mm:ss').value }}</v-list-item-subtitle>
						</v-list-item>
						<v-list-item>
							<v-list-item-title>Status</v-list-item-title>
							<v-list-item-subtitle>
								<v-chip :color="statusColor(flight.status)">
									{{ flight.status }}
								</v-chip>
							</v-list-item-subtitle>
						</v-list-item>
					</v-list>
				</v-col>
				<v-col cols="8">
					<v-list v-if="!loadingAirports">
						<v-list-item>
							<v-list-item-title>From</v-list-item-title>
							<v-list-item-subtitle>{{ airportToString(flight.flight_route_from_airport_id) }}</v-list-item-subtitle>
						</v-list-item>
						<v-list-item>
							<v-list-item-title>To</v-list-item-title>
							<v-list-item-subtitle>{{ airportToString(flight.flight_route_to_airport_id) }}</v-list-item-subtitle>
						</v-list-item>
						<v-list-item>
							<v-list-item-title>Details</v-list-item-title>
							<v-list-item-subtitle>
								<v-btn :to="{ name: 'flight', params: { id: flight.flight_id }}"
									   variant="tonal" min-height="0" style="height: 32px !important;"
									   color="indigo"
								>
									Flight details
								</v-btn>
							</v-list-item-subtitle>
						</v-list-item>
					</v-list>
				</v-col>
			</v-row>
		</v-card-text>
	</v-card>
</template>