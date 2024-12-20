import { createRouter, createWebHistory } from "vue-router";
import store from "@/store";
import HomeView from "../views/HomeView.vue";
import Login from "@/views/Login.vue";
import Error404 from "@/views/Error404.vue";
import Callback from "@/views/Callback.vue";

// user
import user_profile from "@/views/user_profile.vue";
import user_setting from "@/views/user_setting.vue";
import user_notice from "@/views/user_notice.vue";

// Color
import color_index from "@/views/color_index.vue";
import color_detail from "@/views/color_detail.vue";
import color_test from "@/views/color_test.vue";
import color_result from "@/views/color_result.vue";
import color_retest from "@/views/color_retest.vue";
import color_test_auto from "@/views/color_test_auto.vue";

// Closet
import closet_index from "@/views/closet_index.vue";
import closet_detail from "@/views/closet_detail.vue";
import closet_new from "@/views/closet_new.vue";
import closet_trash from "@/views/closet_trash.vue";
import closet_new_outfit from "@/views/closet_new_outfit.vue";
import closet_outfit_index from "@/views/closet_outfit_index.vue";
import closet_outfit_detail from "@/views/closet_outfit_detail.vue";

// Social
import social_index from "@/views/social_index.vue";
import social_collect from "@/views/social_collect.vue";
import social_new from "@/views/social_new.vue";
import social_edit from "@/views/social_edit.vue";
import social_follow_list from "@/views/social_follow_list.vue";

// suggest
import suggest_index from "@/views/suggest_index.vue";
import suggest_detail from "@/views/suggest_detail.vue";
import suggest_recommend from "@/views/suggest_recommend.vue";
import suggest_results from "@/views/suggest_results.vue";

// buy
import buy_result from "@/views/buy_result.vue";
import buy_suggest from "@/views/buy_suggest.vue";
import buy_detail from "@/views/buy_detail.vue";
import buy_index from "@/views/buy_index.vue";

// todo
import todo_index from "@/views/todo_index.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
  },
  {
    path: "/user_profile",
    name: "user_profile",
    component: user_profile,
    meta: { requiresAuth: true },
  },
  {
    path: "/user_setting",
    name: "user_setting",
    component: user_setting,
    meta: { requiresAuth: true },
  },
  {
    path: "/callback",
    name: "Callback",
    component: Callback,
  },
  {
    path: "/Login",
    name: "Login",
    component: Login,
  },
  {
    path: "/:catchAll(.*)",
    name: "Error404",
    component: Error404,
  },
  {
    path: "/color_index",
    name: "color_index",
    component: color_index,
    meta: { requiresAuth: true },
  },
  {
    path: "/color_detail/:id",
    name: "color_detail",
    component: color_detail,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: "/color_test",
    name: "color_test",
    component: color_test,
    meta: { requiresAuth: true },
  },
  {
    path: "/color_result/:id",
    name: "color_result",
    component: color_result,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: "/color_retest",
    name: "color_retest",
    component: color_retest,
    meta: { requiresAuth: true },
  },
  {
    path: "/color_test_auto",
    name: "color_test_auto",
    component: color_test_auto,
    meta: { requiresAuth: true },
  },
  {
    path: "/closet_index",
    name: "closet_index",
    component: closet_index,
    meta: { requiresAuth: true },
  },
  {
    path: "/closet_detail/:id",
    name: "closet_detail",
    component: closet_detail,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: "/closet_new",
    name: "closet_new",
    component: closet_new,
    meta: { requiresAuth: true },
  },
  {
    path: "/closet_trash",
    name: "closet_trash",
    component: closet_trash,
    meta: { requiresAuth: true },
  },
  {
    path: "/closet_new_outfit",
    name: "closet_new_outfit",
    component: closet_new_outfit,
    meta: { requiresAuth: true },
  },
  {
    path: "/closet_outfit_index",
    name: "closet_outfit_index",
    component: closet_outfit_index,
    meta: { requiresAuth: true },
  },
  {
    path: "/closet_outfit_detail/:id",
    name: "closet_outfit_detail",
    component: closet_outfit_detail,
    props: true,
    meta: { requiresAuth: true },
  },
  {
    path: "/social_index",
    name: "social_index",
    component: social_index,
  },
  {
    path: "/social_collect",
    name: "social_collect",
    component: social_collect,
  },
  {
    path: "/social_new",
    name: "social_new",
    component: social_new,
    meta: { requiresAuth: true },
  },
  {
    path: "/social_edit/:id",
    name: "social_edit",
    component: social_edit,
    props: true,
    //meta: { requiresAuth: true },
  },
  {
    path: "/social_follow_list",
    name: "social_follow_list",
    component: social_follow_list,
  },
  {
    path: "/user_notice",
    name: "user_notice",
    component: user_notice,
  },
  {
    path: "/suggest_index",
    name: "suggest_index",
    component: suggest_index,
  },
  {
    path: "/suggest_detail/:id",
    name: "suggest_detail",
    component: suggest_detail,
    props: true,
  },
  {
    path: "/suggest_recommend",
    name: "suggest_recommend",
    component: suggest_recommend,
  },
  {
    path: "/suggest_results",
    name: "suggest_results",
    component: suggest_results,
  },
  {
    path: "/buy_index",
    name: "buy_index",
    component: buy_index,
  },
  {
    path: "/buy_suggest",
    name: "buy_suggest",
    component: buy_suggest,
  },
  {
    path: "/buy_detail/:id",
    name: "buy_detail",
    props: true,
    component: () => import("@/views/buy_detail.vue"),
  },
  {
    path: "/buy_result",
    name: "buy_result",
    component: buy_result,
  },
  {
    path: "/todo_index",
    name: "todo_index",
    component: todo_index,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!store.getters["auth/isAuthenticated"]) {
      try {
        await store.dispatch("auth/initializeAuth");
        if (store.getters["auth/isAuthenticated"]) {
          next();
        } else {
          next("/login");
        }
      } catch (error) {
        console.error("Authentication error:", error);
        next("/login"); 
      }
    } else {
      next(); 
    }
  } else {
    next();
  }
});


export default router;
