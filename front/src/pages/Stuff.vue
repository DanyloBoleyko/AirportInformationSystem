<script setup>
const tabs = [
	{
		title: "Employees",
		route: {
			name: "employees",
		},
	},
	{
		title: "Brigades",
		route: {
			name: "brigades",
		},
	},
	{
		title: "Departments",
		route: {
			name: "departments",
		},
	},
]
</script>

<template>
	<v-container>
		<v-container class="pa-4 mb-4">
			<v-row>
				<v-tabs color="indigo" height="44">
					<v-tab v-for="tab in tabs" :key="tab.title" :to="tab.route">
						{{ tab.title }}
					</v-tab>
				</v-tabs>
				<v-divider class="ma-0"/>
			</v-row>
		</v-container>
		<router-view/>
	</v-container>
</template>