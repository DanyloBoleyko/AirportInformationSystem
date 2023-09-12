<script setup>
import { computed, ref } from "vue";
import { useStore } from "vuex";
import AircraftDetailsCard from "@/pages/aircraft/AircraftDetailsCard.vue";
import AircraftFlightsCard from "@/pages/aircraft/AircraftFlightsCard.vue";

const props = defineProps({
	id: {
		type: String,
		default: null,
	},
})

const store = useStore()

const loading = ref(false)
const aircraft = ref(null)

const loadingAircraftTypes = computed(() => store.state.aircrafts.loadingTypes)
const aircraftTypes = computed(() => store.state.aircrafts.types_list)
const aircraftType = computed(() => aircraftTypes.value?.find(t => t.aircraft_type_id === aircraft.value?.aircraft_type_id))

const loadingFlights = ref(false)
const flights = ref([])

const getAircraft = () => {
	loading.value = true
	store.dispatch('aircrafts/getAircraft', {
		aircraft_id: parseInt(props.id),
	})
		.then(({ data }) => aircraft.value = data?.[0])
		.finally(() => loading.value = false)
}

const getFlights = () => {
	loadingFlights.value = true
	store.dispatch('flights/getFlights', {
		aircraft_id: parseInt(props.id),
		with_schedule: true,
		with_route: true,
	})
		.then(({ data }) => flights.value = data)
		.finally(() => loadingFlights.value = false)
}

const getAircraftTypes = () => {
	store.dispatch('aircrafts/getAircraftTypes')
}

getAircraft()
getAircraftTypes()
getFlights()
</script>

<template>
	<v-container v-if="loading || loadingAircraftTypes">
		<v-row>
			<v-col>
				<v-progress-circular indeterminate color="indigo"/>
			</v-col>
		</v-row>
	</v-container>

	<v-container v-else-if="aircraft === null">
		<v-row>
			<v-col>
				<h1>404</h1>
			</v-col>
		</v-row>
	</v-container>

	<v-container v-else>
		<v-row>
			<v-col md="9" lg="7">
				<v-row align="baseline" class="mb-2">
					<v-col cols="auto">
						<h1>{{ aircraft.name }}</h1>
					</v-col>
					<v-col class="text-body-1">
						<span>{{ aircraftType?.name }}</span>
					</v-col>
				</v-row>
				<aircraft-details-card :aircraft="aircraft"
									   :aircraft-type="aircraftType"
									   :loading="loading || loadingAircraftTypes"
				/>
				<aircraft-flights-card :flights="flights" class="mt-4"
									   :loading="loadingFlights"/>
			</v-col>
			<v-col v-if="$vuetify.display.mdAndUp" class="h-100">
				<v-img src="/src/assets/sky2.jpg"
					   height="calc(100vh - 64px - 32px)"
					   class="rounded-lg"
					   :cover="true"
				/>
			</v-col>
		</v-row>
	</v-container>
</template>