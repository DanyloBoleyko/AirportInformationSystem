<script setup>
defineProps({
	aircraftType: {
		type: Object,
		default: null,
	},
	aircraft: {
		type: Object,
		default: null,
	},
	loading: {
		type: Boolean,
		default: false,
	},
})
</script>

<template>
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
				<v-col/>
			</v-row>
		</v-card-text>
	</v-card>
</template>