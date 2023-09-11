<script setup>
import { useStore } from "vuex";
import { computed, ref, watch } from "vue";
import AppTable from "@/components/AppTable.vue";
import AircraftTypeCard from "@/components/AircraftTypeCard.vue";

const store = useStore()

const loadingAircrafts = computed(() => store.state.aircrafts.loading)
const aircrafts = computed(() => store.state.aircrafts.list)

const loadingAircraftTypes = computed(() => store.state.aircrafts.loadingTypes)
const aircraftTypes = computed(() => store.state.aircrafts.types_list)

const getAircrafts = () => {
	store.dispatch('aircrafts/getAircrafts', {
		aircraft_type_id: selectedType.value,
	})
}

const getAircraftTypes = () => {
	store.dispatch('aircrafts/getAircraftTypes')
}

const addAircraft = () => {
	store.dispatch('aircrafts/addAircraft')
		.then(() => getAircrafts())
}

const selectedType = ref(1)

getAircraftTypes()

watch(selectedType, () => {
	getAircrafts()
}, { immediate: true })
</script>

<template>
	<v-container>
		<v-row>
			<v-col>
				<v-item-group v-model="selectedType" mandatory>
					<v-row>
						<v-col v-for="type in aircraftTypes" :key="type.aircraft_type_id">
							<v-item v-slot="{ isSelected, toggle }" :value="type.aircraft_type_id">
								<aircraft-type-card :aircraft-type="type"
													:selected="isSelected"
													@click="toggle"
								/>
							</v-item>
						</v-col>
					</v-row>
				</v-item-group>
			</v-col>
		</v-row>
		<v-row>
			<v-col>
				<app-table :loading="loadingAircrafts"
						   :data="aircrafts"
						   :exclude="['aircraft_id', 'aircraft_type_id']"
				>
					<template #actions="{ row }">
						<v-btn color="indigo" variant="text" :to="{ name: 'aircraft', params: { id: row.aircraft_id }}">
							Details
						</v-btn>
					</template>
				</app-table>
			</v-col>
		</v-row>
	</v-container>
</template>
