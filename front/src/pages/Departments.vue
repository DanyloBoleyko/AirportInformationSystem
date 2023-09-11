<script setup>
import { useStore } from "vuex";
import { computed, ref, watch } from "vue";
import AppTable from "@/components/AppTable.vue";

const store = useStore()

const loadingDepartments = computed(() => store.state.departments.loading)
const departments = computed(() => store.state.departments.list)

const addDepartmentDialog = ref({
	show: false,
	params: {
		name: null,
		gender: null,
		birth_date: null,
		work_experience: 0,
		children: 0,
		profession: null,
		department: null,
	},
	options: {
		gender: [
			{ label: 'Male', value: 'M' },
			{ label: 'Female', value: 'F' }
		],
	}
})

const editDepartmentDialog = ref({
	valid: null,
	show: false,
	params: {
		department_id: null,
		name: null,
	},
})

const deleteDepartmentDialog = ref({
	valid: null,
	show: false,
	params: {
		department_id: null,
		new_department_id: null,
	},
})

const validForm = ref(null)

const addDepartment = () => {
	if (!validForm.value) return
	store.dispatch('employees/addEmployee', addDepartmentDialog.value.params)
		.finally(() => addDepartmentDialog.value.show = false)
}

store.dispatch('departments/getDepartments')
store.dispatch('professions/getProfessions')
</script>

<template>
	<v-row>
		<v-col>
			<v-row class="mb-4">
				<v-spacer/>
				<v-col cols="auto">
					<v-dialog v-model="addDepartmentDialog.show"
							  max-width="400"
					>
						<template #activator="{ props }">
							<v-btn v-bind="props"
								   height="44"
								   color="indigo"
							>
								<v-icon icon="mdi-plus" class="mr-2"/>
								Add department
							</v-btn>
						</template>
						<v-card rounded="lg">
							<v-card-title>
								Add employee
							</v-card-title>
							<v-form v-model="validForm" @submit.prevent="addDepartment">
								<v-container>
									<v-row>
										<v-col cols="12">
											<v-text-field v-model="addDepartmentDialog.params.name"
														  label="Name*"
														  variant="outlined"
														  rounded="lg"
														  density="compact"
														  :rules="[
															(value) => !!value || 'Required',
														  ]"
											>
											</v-text-field>
										</v-col>
										<v-col cols="6">
											<v-text-field v-model="addDepartmentDialog.params.birth_date"
														  label="Birth date*"
														  type="date"
														  variant="outlined"
														  rounded="lg"
														  density="compact"
														  :rules="[
															(value) => !!value || 'Required',
														  ]"
											>
											</v-text-field>
										</v-col>
										<v-col cols="6">
											<v-select v-model="addDepartmentDialog.params.gender"
													  label="Gender*"
													  :items="addDepartmentDialog.options.gender"
													  item-title="label" item-value="value"
													  :rules="[
														(value) => !!value || 'Required',
													  ]"
											/>
										</v-col>
										<v-col cols="6">
											<v-text-field v-model="addDepartmentDialog.params.work_experience"
														  type="number"
														  label="Work experience*"
														  variant="outlined"
														  rounded="lg"
														  density="compact"
														  min="0"
														  max="120"
														  :rules="[
															(value) => value !== null || 'Required',
															(value) => value >= 0 || 'Must be greater than 0',
															(value) => value <= 120 || 'Must be less than 120',
														  ]"
											>
												<template #append-inner>
													<span class="text-grey">years</span>
												</template>
											</v-text-field>
										</v-col>

										<v-col cols="6">
											<v-text-field v-model="addDepartmentDialog.params.children"
														  type="number"
														  label="Children*"
														  variant="outlined"
														  rounded="lg"
														  density="compact"
														  min="0"
														  max="120"
														  :rules="[
															(value) => value !== null || 'Required',
															(value) => value >= 0 || 'Must be greater than 0',
															(value) => value <= 120 || 'Must be less than 120',
														  ]"
											>
											</v-text-field>
										</v-col>
									</v-row>
								</v-container>
								<v-divider/>
								<v-container>
									<v-row>
										<v-col cols="12">
											<v-btn variant="flat" type="submit" :block="true" color="indigo">
												Add
											</v-btn>
										</v-col>
									</v-row>
								</v-container>
							</v-form>
						</v-card>
					</v-dialog>
				</v-col>


			</v-row>
			<app-table :loading="loadingDepartments"
					   :data="departments"
					   :exclude="['department_id']"
			>
				<template #actions="{ row }">
					<v-btn color="indigo" variant="text"
						   @click="editDepartmentDialog.show = true; editDepartmentDialog.params = row"
					>
						<v-icon>mdi-pencil</v-icon>
					</v-btn>
					<v-btn color="error" variant="text" @click="deleteDepartmentDialog.show = true">
						<v-icon>mdi-delete</v-icon>
					</v-btn>
				</template>
			</app-table>

			<v-dialog v-model="editDepartmentDialog.show">
				<v-form v-model="editDepartmentDialog.valid">
					<v-card rounded="lg">
						<v-card-title>
							Edit department
						</v-card-title>
						<v-container>
							<v-row>
								<v-col cols="12">
									<v-text-field v-model="editDepartmentDialog.params.name"
												  label="Name*"
												  variant="outlined"
												  rounded="lg"
												  density="compact"
												  :rules="[
											(value) => !!value || 'Required',
										  ]"
									></v-text-field>
								</v-col>
							</v-row>
						</v-container>
						<v-divider/>
						<v-container>
							<v-row>
								<v-col cols="6">
									<v-btn variant="outlined" :block="true" color="indigo"
										   width="100%"
										   @click="editDepartmentDialog.show = false"
									>
										Cancel
									</v-btn>
								</v-col>
								<v-col cols="6">
									<v-btn variant="flat" type="submit" :block="true" color="indigo"
										   width="100%"
										   @click="editDepartmentDialog.show = false"
									>
										Save
									</v-btn>
								</v-col>
							</v-row>
						</v-container>
					</v-card>
				</v-form>
			</v-dialog>
		</v-col>
	</v-row>
</template>
