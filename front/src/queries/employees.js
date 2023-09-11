import { useQuery } from "@tanstack/vue-query";
import { EmployeesService } from "@/api/index.js";

export function getEmployees() {
    return useQuery({
        queryKey: ['employees'],
        queryFn: async (context) => {
            EmployeesService.getEmployeesEmployeesListGet({
                departmentId: context.queryKey[1].departmentId,
                positionId: context.queryKey[1].positionId,
            })
        }
    })
}