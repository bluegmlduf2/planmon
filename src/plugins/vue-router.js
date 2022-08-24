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
import message from '@/assets/js/message';
import globalFunc from '@/plugins/globalFunc';

// 공통함수사용
Vue.use(globalFunc);
// 라우터의 경로설정 등록
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
    // 권한이 필요한 화면에서 로그인하지않은 경우 홈으로 이동
    next({ name: 'home.index' });
  } else if (to.name === 'write.index') {
    // 글쓰기 화면에 이동전 필수입력값 확인
    // eslint-disable-next-line no-use-before-define
    setWriteRouter(to, from, next);
  } else {
    // 문제가 없는 경우 화면이동
    next();
  }
});

// 글쓰기 화면 이동관련 라우터
function setWriteRouter(to, from, next) {
  // || {}은 객체의 destructing의 null에 대비
  const { country, stayStatus } = to.params.selection || {};
  if (!from.name) {
    // 글쓰기화면에서 새로고침하면 홈화면으로
    next({ name: 'home.index' });
  } else if (!country || !stayStatus) {
    // 국가나 체류상태를 선택하지 않은 경우 유저일정설정화면 이동
    Vue.prototype.$toast.warning(message.emptyWriteCondition);
    // 모바일화면 유무
    if (Vue.prototype.isMobile()) {
      // 모바일화면인 경우 나의 일정 설정화면으로 이동
      // Redirected 에러때문에 push사용
      router.push({ path: 'selection' });
    }
  } else {
    // 글쓰기 화면이동에 문제가 없으면 글쓰기 화면으로이동
    next();
  }
}

Vue.router = router;

export default {
  router,
};
