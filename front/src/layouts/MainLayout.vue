<script setup>
import AppHeader from "@/components/AppHeader.vue";
</script>

<template>
	<v-layout full-height>
		<app-header/>

		<v-main style="min-height: 100vh" class="bg-blue-grey-lighten-5">
			<v-container class="pa-0 h-100 bg-white">
				<router-view/>
			</v-container>
		</v-main>
	</v-layout>
</template>

<style scoped>

</style>