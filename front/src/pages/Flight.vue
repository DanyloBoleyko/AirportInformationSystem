<script setup>
import { computed, ref, watch } from "vue";
import { useStore } from "vuex";
import AircraftDetailsCard from "@/pages/aircraft/AircraftDetailsCard.vue";
import FlightInfoCard from "@/pages/flights/FlightInfoCard.vue";
import BuyTicketDialog from "@/pages/flights/BuyTicketDialog.vue";

const props = defineProps({
	id: {
		type: Number,
		default: null,
	},
})

const store = useStore()

const loading = ref(false)
const flight = ref(null)

const loadingAircraft = ref(false)
const aircraft = ref(null)

const loadingTickets = ref(false)
const tickets = ref([])

const loadingSchedule = ref(false)
const schedule = ref(null)

const places = ref([])
const selectedPlaces = ref([])

const buyTicketDialog = ref({
	show: false,
	params: {
		places: [],
		flight_id: null,
	},
})

const ticketPrice = ref(0)

const getSchedule = () => {
	store.dispatch('flights/getSchedule', {
		schedule_id: flight.value.schedule_id,
	})
		.then(({ data }) => {
			schedule.value = data?.[0]

			ticketPrice.value = schedule.value?.ticket_price_discounted || 0
		})
		.finally(() => loadingSchedule.value = false)
}

const getAircraft = () => {
	store.dispatch('aircrafts/getAircraft', {
		aircraft_id: flight.value.aircraft_id,
		with_types: true,
	})
		.then(({ data }) => {
			aircraft.value = data?.[0]

			places.value = Array.from({ length: aircraft.value?.aircraft_type_place_count || 0 }, (_, i) => i + 1)
		})
		.finally(() => loadingAircraft.value = false)
}

const getTickets = () => {
	loadingTickets.value = true
	store.dispatch('tickets/getTickets', {
		flight_id: flight.value.flight_id,
	})
		.then(({ data }) => {
			tickets.value = data
		})
		.finally(() => loadingTickets.value = false)
}

const getFlight = () => {
	loading.value = true
	loadingAircraft.value = true
	loadingSchedule.value = true
	store.dispatch('flights/getFlight', {
		flight_id: props.id,
	})
		.then(({ data }) => {
			flight.value = data?.[0]

			buyTicketDialog.value.params.flight_id = flight.value.flight_id

			getAircraft()
			getTickets()
			getSchedule()
		})
		.finally(() => loading.value = false)
}

const isPlaceBought = (place) => {
	return !!tickets.value.find(ticket =>
		ticket.place_number === place
		&& (ticket.status === 'Підтверджено'
			|| ticket.status === 'Куплено')
	) || false
}

const placeColor = (place) => {
	if (isPlaceBought(place)) {
		return 'grey'
	} else if (selectedPlaces.value.includes(place)) {
		return 'success'
	} else {
		return 'indigo'
	}
}

const selectPlace = (place) => {
	if (selectedPlaces.value.includes(place)) {
		selectedPlaces.value = selectedPlaces.value.filter(p => p !== place)
	} else {
		selectedPlaces.value.push(place)
	}
}

const buyTicket = (place) => {
	buyTicketDialog.value.show = true
	buyTicketDialog.value.params.place = place
}

getFlight()
</script>

<template>
	<v-container v-if="loading || loadingAircraft || loadingSchedule">
		<v-row>
			<v-col>
				<v-progress-circular indeterminate color="indigo"/>
			</v-col>
		</v-row>
	</v-container>

	<v-container v-else-if="flight === null">
		<v-row>
			<v-col>
				<h1>404</h1>
			</v-col>
		</v-row>
	</v-container>

	<v-container v-else>
		<v-row>
			<v-col cols="12" md="6" lg="5" xl="4">
				<flight-info-card :flight="flight"
								  :aircraft="aircraft"
								  :schedule="schedule"
								  :free-places="places.filter(p => !isPlaceBought(p))"
								  class="position-sticky"
								  style="top: calc(64px + 16px)"
				/>
			</v-col>
			<v-col>
<!--				<v-img src="/src/assets/sky1.jpg" :cover="true" class="rounded-lg">-->
					<v-row justify="center">
						<v-col v-if="aircraft.aircraft_type_type === 'Вузькофюзеляжний'"
							   class="border shadow-big"
							   style="max-width: 400px; padding-block: 92px; padding-inline: 24px; border-radius: 12%"
						>
							<v-row justify="center">
								<v-col v-for="place in places" :key="place"
									   cols="2" class="d-flex justify-center"
									   :style="{
								marginRight: (place % 6) - 2 === 0 || (place % 6) - 4 === 0 ? '24px' : 0,
								maxWidth: `${100 / 7}% !important`,
								flex: `0 0 ${100 / 7}% !important`,
							}"
								>
									<v-btn :color="placeColor(place)"
										   :disabled="isPlaceBought(place)"
										   @click="buyTicket(place)"
									>
										{{ place }}
									</v-btn>
								</v-col>
							</v-row>
						</v-col>
						<v-col v-else-if="aircraft.aircraft_type_type === 'Широкофюзеляжний'"
							   class="border"
							   style="max-width: 600px; padding-block: 92px; padding-inline: 24px; border-radius: 12%"
						>
							<v-row justify="center">
								<v-col v-for="place in places" :key="place"
									   cols="2" class="d-flex justify-center"
									   :style="{
								marginRight: (place % 8) - 2 === 0 || (place % 8) - 6 === 0 ? '24px' : 0,
								maxWidth: `${100 / 9}% !important`,
								flex: `0 0 ${100 / 9}% !important`,
							}"
								>
									<v-btn :color="placeColor(place)"
										   :disabled="isPlaceBought(place)"
										   @click="buyTicket(place)"
									>
										{{ place }}
									</v-btn>
								</v-col>
							</v-row>
						</v-col>
					</v-row>
<!--				</v-img>-->
			</v-col>
		</v-row>
		<!--		<v-row>
					<v-spacer/>
					<v-col cols="auto">
						<v-btn color="success" :disabled="selectedPlaces.length === 0" @click="buyTickets">
							<v-icon icon="mdi-ticket-confirmation" class="mr-2"/>
							Buy ticket
						</v-btn>
					</v-col>
				</v-row>-->


		<buy-ticket-dialog v-model="buyTicketDialog.show"
						   :params="buyTicketDialog.params"
						   :price="ticketPrice"
		/>
	</v-container>
</template>

<style>
.shadow-big {
	box-shadow: 0 0 64px rgba(0, 0, 0, 0.25);
	background: linear-gradient(90deg, #FFFFFF 0%, rgba(0, 0, 0, .10) 50%, #FFFFFF 100%), #FFFFFF;
}
</style>