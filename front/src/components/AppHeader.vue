<script setup>
const menu = [
	{
		title: "Home",
		route: {
			name: "home",
		},
	},
	{
		title: "Stuff",
		route: {
			name: "stuff",
		},
	},
	{
		title: "Aircrafts",
		route: {
			name: "aircrafts",
		},
	},
	{
		title: "Flights",
		route: {
			name: "flights",
		},
	},
]
</script>

<template>
	<v-app-bar class="px-6" color="indigo-darken-4" :flat="true">
		<v-row align="center">
			<v-col cols="auto" class="font-weight-bold">
				✈️ JetLuxe Terminals
			</v-col>

			<v-col>
				<v-row :dense="true">
					<v-col v-for="m in menu" :key="m.title" cols="auto">
						<v-btn variant="text"
							   :to="m.route"
							   :active="$route.name === m.route.name"
							   class="text-capitalize font-weight-bold"
						>
							{{ m.title }}
						</v-btn>
					</v-col>
				</v-row>
			</v-col>
		</v-row>
	</v-app-bar>
</template>
