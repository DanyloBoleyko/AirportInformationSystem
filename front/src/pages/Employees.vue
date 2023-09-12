<script setup>
import { useStore } from "vuex";
import { computed, ref, watch } from "vue";
import AppTable from "@/components/AppTable.vue";

const store = useStore()

const params = ref({
	department_id: null,
	department_name: null,
})

const loadingEmployees = computed(() => store.state.employees.loading)
const employees = computed(() => store.state.employees.list)

const loadingDepartments = computed(() => store.state.departments.loading)
const departments = computed(() => store.state.departments.list)

const loadingProfessions = computed(() => store.state.professions.loading)
const professions = computed(() => store.state.professions.list)

watch(params, () => {
	store.dispatch('employees/getEmployees', params.value)
}, { deep: true, immediate: true })

const addEmployeeDialog = ref({
	show: false,
	params: {
		name: null,
		gender: null,
		birth_date: null,
		work_experience: 0,
		children: 0,
		profession: null,
		department: null,
		address: null,
		telephone: null,
	},
	options: {
		gender: [
			{ label: 'Male', value: 'M' },
			{ label: 'Female', value: 'F' }
		],
	}
})

const validForm = ref(null)

const addEmployee = () => {
	if (!validForm.value) return
	store.dispatch('employees/addEmployee', addEmployeeDialog.value.params)
		.finally(() => addEmployeeDialog.value.show = false)
}

store.dispatch('departments/getDepartments')
store.dispatch('professions/getProfessions')
</script>

<template>
	<v-row>
		<v-col>
			<v-row class="mb-4">
				<v-col cols="8" lg="4">
					<v-select v-model="params.department_id" :items="departments"
							  item-title="name" item-value="department_id"
							  :loading="loadingDepartments"
							  label="Department"
							  placeholder="Any"
					/>
				</v-col>
				<v-spacer/>
				<v-col cols="auto">
					<v-dialog v-model="addEmployeeDialog.show"
							  max-width="400"
					>
						<template #activator="{ props }">
							<v-btn v-bind="props"
								   height="44"
								   color="indigo"
							>
								<v-icon icon="mdi-plus" class="mr-2"/>
								Add employee
							</v-btn>
						</template>
						<v-card rounded="lg">
							<v-card-title>
								Add employee
							</v-card-title>
							<v-form v-model="validForm" @submit.prevent="addEmployee">
								<v-container>
									<v-row>
										<v-col cols="12">
											<v-text-field v-model="addEmployeeDialog.params.name"
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
											<v-text-field v-model="addEmployeeDialog.params.birth_date"
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
											<v-select v-model="addEmployeeDialog.params.gender"
													  label="Gender*"
													  :items="addEmployeeDialog.options.gender"
													  item-title="label" item-value="value"
													  :rules="[
														(value) => !!value || 'Required',
													  ]"
											/>
										</v-col>
										<v-col cols="6">
											<v-text-field v-model="addEmployeeDialog.params.work_experience"
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
											<v-text-field v-model="addEmployeeDialog.params.children"
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

										<v-col cols="6">
											<v-select v-model="addEmployeeDialog.params.profession"
													  label="Profession*"
													  :items="professions"
													  item-title="name" item-value="professionID"
													  :rules="[
														(value) => !!value || 'Required',
													  ]"
											/>
										</v-col>

										<v-col cols="6">
											<v-select v-model="addEmployeeDialog.params.department"
													  label="Department*"
													  :items="departments"
													  item-title="name" item-value="detaprtmentID"
													  :rules="[
														(value) => !!value || 'Required',
													  ]"
											/>
										</v-col>

										<v-col cols="12">
											<v-text-field v-model="addEmployeeDialog.params.address"
														  label="Address*"
														  variant="outlined"
														  rounded="lg"
														  density="compact"
														  :rules="[
															(value) => !!value || 'Required',
														  ]"
											>
											</v-text-field>
										</v-col>

										<v-col cols="12">
											<v-text-field v-model="addEmployeeDialog.params.telephone"
														  label="Telephone*"
														  variant="outlined"
														  rounded="lg"
														  density="compact"
														  :rules="[
															(value) => !!value || 'Required',
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
											<v-btn class="w-100" variant="flat" type="submit" :block="true" color="indigo">
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
			<app-table :loading="loadingEmployees"
					   :data="employees"
					   :exclude="['manager_of_department']"
			/>
		</v-col>
	</v-row>
</template>
