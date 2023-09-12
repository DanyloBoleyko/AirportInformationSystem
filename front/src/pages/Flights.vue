<script setup>
import { useStore } from "vuex";
import { computed, ref, watch } from "vue";
import AppTable from "@/components/AppTable.vue";
import { useDateFormat } from "@vueuse/core";

const store = useStore()

const loadingFlights = computed(() => store.state.flights.loading)
const flights = computed(() => store.state.flights.list)

const loadingFlightsByRoute = computed(() => store.state.flights.loadingRoutes)
const flightsByRoute = computed(() => store.state.flights.list_by_routes)

const loadingAirports = computed(() => store.state.airports.loading)
const airports = computed(() => store.state.airports.list)

const airportTitle = (airport) => {
	return `${airport.city}, ${airport.country}`
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

const getFlights = () => {
	store.dispatch('flights/getFlights')
}

const getFlightsByRoutes = () => {
	store.dispatch('flights/getFlightByRoutes')
}

const getAirports = () => {
	store.dispatch('airports/getAirports')
}

const params = ref({
	from_airport: null,
	to_airport: null,
})

watch(params, () => {
	store.dispatch('flights/getFlightByRoutes', params.value)
}, { deep: true, immediate: true })

getFlights()
getFlightsByRoutes()
getAirports()
</script>

<template>
	<v-container v-if="loadingFlights || loadingAirports">
		<v-row>
			<v-col>
				<v-progress-circular indeterminate color="indigo"/>
			</v-col>
		</v-row>
	</v-container>
	<v-container v-else>
		<v-row>
			<v-col>
				<h1>Flights</h1>
			</v-col>
		</v-row>
		<v-row>
			<v-col>
				<v-select v-model="params.from_airport"
						  label="Origin"
						  :items="airports"
						  :item-title="item => airportTitle(item)"
						  item-value="airport_id"
				></v-select>
			</v-col>
			<v-col>
				<v-select v-model="params.to_airport"
						  label="Destination"
						  :items="airports"
						  :item-title="item => airportTitle(item)"
						  item-value="airport_id"
				></v-select>
			</v-col>
		</v-row>
		<v-row>
			<v-col>
				<app-table :loading="loadingFlightsByRoute"
						   :data="flightsByRoute"
						   :exclude="['aircraft_id', 'ticket_price', 'flight_id', 'schedule_id']"
				>
					<template #head:ticket_price_discounted="{ row }">
						Ticket price
					</template>
					<template #cell:ticket_price_discounted="{ row }">
						{{ row.ticket_price_discounted }} €
					</template>

					<template #head:from_airport_id="{ row }">
						Origin point
					</template>
					<template #cell:from_airport_id="{ row }">
						{{ airportTitle(airports.find(airport => airport.airport_id === row.from_airport_id)) }}
					</template>

					<template #head:to_airport_id="{ row }">
						Destination point
					</template>
					<template #cell:to_airport_id="{ row }">
						{{ airportTitle(airports.find(airport => airport.airport_id === row.to_airport_id)) }}
					</template>

					<template #cell:arrival_datetime="{ row }">
						<template v-if="row.arrival_datetime">
							{{ useDateFormat(row.arrival_datetime, 'YYYY-MM-DD HH:mm').value }}
						</template>
					</template>

					<template #cell:departure_datetime="{ row }">
						<template v-if="row.departure_datetime">
							{{ useDateFormat(row.departure_datetime, 'YYYY-MM-DD HH:mm').value }}
						</template>
					</template>

					<template #cell:status="{ row }">
						<v-chip :color="statusColor(row.status)">
							{{ row.status }}
						</v-chip>
					</template>

					<template #actions="{ row }">
						<v-btn variant="text" color="indigo"
							   :to="{ name: 'flight', params: { id: row.flight_id }}"
						>
							Details
						</v-btn>
					</template>
				</app-table>
			</v-col>
		</v-row>
	</v-container>
</template>
