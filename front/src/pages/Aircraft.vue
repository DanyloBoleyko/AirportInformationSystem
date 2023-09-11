<script setup>
import { computed, ref } from "vue";
import { useStore } from "vuex";

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

const getAircraft = () => {
	loading.value = true
	store.dispatch('aircrafts/getAircraft', {
		aircraft_id: parseInt(props.id),
	})
		.then(({ data }) => aircraft.value = data?.[0])
		.finally(() => loading.value = false)
}

const getAircraftTypes = () => {
	store.dispatch('aircrafts/getAircraftTypes')
}

getAircraft()
getAircraftTypes()
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
		<v-row align="baseline">
			<v-col cols="auto">
				<h1>{{ aircraft.name }}</h1>
			</v-col>
			<v-col class="text-body-1">
				<span>{{ aircraftType?.name }}</span>
			</v-col>
		</v-row>
		<v-row>
			<v-col md="7" lg="5">
				<v-card :flat="true" border>
					<v-card-title>
						<h2 class="text-h6">Details</h2>
					</v-card-title>
					<v-card-text>
						<v-row>
							<v-col>
								<v-list>
									<v-list-item>
										<v-list-item-title>Type</v-list-item-title>
										<v-list-item-subtitle>{{ aircraftType.type }}</v-list-item-subtitle>
									</v-list-item>
									<v-list-item>
										<v-list-item-title>Seats</v-list-item-title>
										<v-list-item-subtitle>{{ aircraftType.place_count }}</v-list-item-subtitle>
									</v-list-item>
									<v-list-item>
										<v-list-item-title>Built at</v-list-item-title>
										<v-list-item-subtitle>{{ aircraft.built_date }}</v-list-item-subtitle>
									</v-list-item>
								</v-list>
							</v-col>
							<v-col>
								<v-list>
									<v-list-item>
										<v-list-item-title>Flights</v-list-item-title>
										<v-list-item-subtitle>{{ aircraft.flight_count }}</v-list-item-subtitle>
									</v-list-item>
									<v-list-item>
										<v-list-item-title>Repair count</v-list-item-title>
										<v-list-item-subtitle>{{ aircraft.repair_count }}</v-list-item-subtitle>
									</v-list-item>
								</v-list>
							</v-col>
						</v-row>
					</v-card-text>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>