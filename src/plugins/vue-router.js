/* ============
 * Vue Router
 * ============
 *
 * The official Router for Vue.js. It deeply integrates with Vue.js core
 * to make building Single Page Applications with Vue.js a breeze.
 *
 * http://router.vuejs.org/en/index.html
 */

import Vue from 'vue';
import VueRouter from 'vue-router';
import routes from '@/routes';
import store from '@/store';

Vue.use(VueRouter);

export const router = new VueRouter({
  mode: 'history',
  routes,
  scrollBehavior() {
    // 새로고침 후 항상 최상단 표시
    return { top: 0 };
  },
});
router.beforeEach((to, from, next) => {
  if (to.matched.some((m) => m.meta.auth) && !store.getters.user) {
    // 로그인한 상태가 아니라면 홈화면을 표시
    next({
      name: 'home.index',
    });
  } else {
    next();
  }
});

Vue.router = router;

export default {
  router,
};
