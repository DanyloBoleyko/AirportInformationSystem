const routes = [
    {
        path: '',
        component: () => import('./layouts/MainLayout.vue'),
        children: [
            {
                path: '',
                name: 'home',
                component: () => import('./pages/Home.vue')
            },
            {
                path: '/stuff',
                name: 'stuff',
                redirect: '/employees',
                component: () => import('./pages/Stuff.vue'),
                children: [
                    {
                        path: '/employees',
                        name: 'employees',
                        component: () => import('./pages/Employees.vue')
                    },
                    {
                        path: '/brigades',
                        name: 'brigades',
                        component: () => import('./pages/Brigades.vue')
                    },
                    {
                        path: '/departments',
                        name: 'departments',
                        component: () => import('./pages/Departments.vue')
                    },
                ]
            },
            {
                path: '/aircraft/:id/',
                name: 'aircraft',
                component: () => import('./pages/Aircraft.vue'),
                props: route => ({ id: parseInt(route.params.id) || undefined })
            },
            {
                path: '/aircrafts',
                name: 'aircrafts',
                component: () => import('./pages/Aircrafts.vue')
            },
            { path: '/:pathMatch(.*)*', name: '404', component: () => import('./pages/NotFound.vue') }
        ]
    }
]

export default routes