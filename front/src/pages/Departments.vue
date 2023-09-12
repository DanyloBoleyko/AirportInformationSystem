<script setup>
import { useStore } from "vuex";
import { computed, ref, watch } from "vue";
import AppTable from "@/components/AppTable.vue";
import { deepCopy } from "@/lib/reactive.js";

const store = useStore()

const loadingDepartments = computed(() => store.state.departments.loading)
const departments = computed(() => store.state.departments.list)

const loadingBrigades = computed(() => store.state.brigades.loading)
const brigades = computed(() => store.state.brigades.list)

const addDepartmentDialog = ref({
	show: false,
	params: {
		name: null,
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

const getDepartments = () => {
	store.dispatch('departments/getDepartments')
}

const deleteDepartment = () => {
	store.dispatch('departments/deleteDepartment', deleteDepartmentDialog.value.params)
		.finally(() => deleteDepartmentDialog.value.show = false)

	getDepartments()
}

const deleteDepartmentSubmit = () => {
	if (!deleteDepartmentDialog.value.valid) return

	deleteDepartment()
}

const validForm = ref(null)

const addDepartment = () => {
	if (!validForm.value) return

	store.dispatch('departments/createDepartment', addDepartmentDialog.value.params)
		.finally(() => addDepartmentDialog.value.show = false)

	getDepartments()
}

const updateDepartment = () => {
	if (!editDepartmentDialog.value.valid) return

	store.dispatch('departments/updateDepartment', editDepartmentDialog.value.params)
		.finally(() => editDepartmentDialog.value.show = false)

	getDepartments()
}

const onDelete = (id) => {
	const brigadesOfDepartment = brigades.value.filter((brigade) => brigade.department_id === id)
	if (brigadesOfDepartment.length > 0) {
		deleteDepartmentDialog.value.params.department_id = id
		deleteDepartmentDialog.value.params.new_department_id = null
		deleteDepartmentDialog.value.show = true
	} else {
		store.dispatch('departments/deleteDepartment', {
			department_id: id,
			new_department_id: null,
		})
		getDepartments()
	}
}

store.dispatch('brigades/getBrigades')
getDepartments()
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
								Add department
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
			<app-table :loading="loadingDepartments || loadingBrigades"
					   :data="departments"
					   :exclude="['department_id']"
			>
				<template #actions="{ row }">
					<v-btn color="indigo" variant="text"
						   @click="editDepartmentDialog.show = true; editDepartmentDialog.params = deepCopy(row)"
					>
						<v-icon>mdi-pencil</v-icon>
					</v-btn>
					<v-btn color="error" variant="text" @click="onDelete(row.department_id)">
						<v-icon>mdi-delete</v-icon>
					</v-btn>
				</template>
			</app-table>

			<v-dialog v-model="editDepartmentDialog.show">
				<v-form v-model="editDepartmentDialog.valid" @submit.prevent="updateDepartment">
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

			<v-dialog v-model="deleteDepartmentDialog.show">
				<v-form v-model="deleteDepartmentDialog.valid" @submit.prevent="deleteDepartmentSubmit">
					<v-card rounded="lg">
						<v-card-title>
							Delete department
						</v-card-title>
						<v-container>
							<v-row>
								<v-col cols="12">
									There are some brigades asign to this department. Please select new department for them.
								</v-col>
								<v-col cols="12">
									<v-select v-model="deleteDepartmentDialog.params.new_department_id"
											  label="New department*"
											  variant="outlined"
											  rounded="lg"
											  density="compact"
											  :items="departments.filter(d => d.department_id !== deleteDepartmentDialog.params.department_id)"
											  item-value="department_id"
											  item-title="name"
											  :rules="[
												(value) => !!value || 'Required',
											  ]"
									></v-select>
								</v-col>
							</v-row>
						</v-container>
						<v-divider/>
						<v-container>
							<v-row>
								<v-col cols="6">
									<v-btn variant="outlined" :block="true" color="indigo"
										   width="100%"
										   @click="deleteDepartmentDialog.show = false"
									>
										Cancel
									</v-btn>
								</v-col>
								<v-col cols="6">
									<v-btn variant="flat" type="submit" :block="true" color="indigo"
										   width="100%"
										   @click="deleteDepartmentDialog.show = false"
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
