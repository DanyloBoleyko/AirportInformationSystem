<script setup>
defineProps({
	aircraftType: {
		type: Object,
		required: true,
	},
	selected: {
		type: Boolean,
		default: false,
	},
})
</script>

<template>
	<v-card :color="selected ? 'indigo' : 'grey-lighten-4'" :flat="true">
		<v-img :src="`src/assets/aircrafts/${aircraftType.name}.jpg`" height="256" :cover="true">
			<v-sheet v-if="selected" width="32" height="32" elevation="0"
					 class="d-flex justify-center align-center rounded-circle position-absolute"
					 style="right: 8px; top: 8px"
			>
				<v-icon>mdi-check</v-icon>
			</v-sheet>
		</v-img>

		<v-card-text>
			<h2>{{ aircraftType.name }}</h2>
		</v-card-text>
	</v-card>
</template>