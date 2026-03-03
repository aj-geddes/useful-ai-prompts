# Vue Router 4

## Vue Router 4

```typescript
// router/index.ts
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: () => import("@/views/Home.vue"),
    meta: { title: "Home" },
  },
  {
    path: "/login",
    component: () => import("@/views/Login.vue"),
    meta: { title: "Login", requiresGuest: true },
  },
  {
    path: "/dashboard",
    component: () => import("@/views/Dashboard.vue"),
    meta: { title: "Dashboard", requiresAuth: true },
    children: [
      {
        path: "users",
        component: () => import("@/views/Users.vue"),
        meta: { title: "Users" },
      },
      {
        path: "analytics",
        component: () => import("@/views/Analytics.vue"),
        meta: { title: "Analytics" },
      },
    ],
  },
  {
    path: "/users/:id",
    component: () => import("@/views/UserDetail.vue"),
    meta: { title: "User Details", requiresAuth: true },
  },
  {
    path: "/:pathMatch(.*)*",
    component: () => import("@/views/NotFound.vue"),
    meta: { title: "Not Found" },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

// Navigation guards
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  // Update page title
  document.title = (to.meta.title as string) || "App";

  // Check authentication
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/login");
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next("/dashboard");
  } else {
    next();
  }
});

export default router;

// main.ts
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

createApp(App).use(router).mount("#app");
```
