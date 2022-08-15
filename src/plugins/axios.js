/* ============
 * Axios
 * ============
 *
 * Promise based HTTP client for the browser and node.js.
 * Because Vue Resource has been retired, Axios will now been used
 * to perform AJAX-requests.
 *
 * https://github.com/mzabriskie/axios
 */

import Vue from 'vue';
import Axios from 'axios';
import store from '@/store';
import firebase from '@/plugins/firebase';
import message from '@/assets/js/message';

Axios.defaults.baseURL = process.env.VUE_APP_API_LOCATION; // /api를 서버 요청의 기본경로로한다
Axios.defaults.headers.common.Accept = 'application/json';
// 요청응답 전처리 (권한전달)
Axios.interceptors.request.use(
  async (config) => {
    const { currentUser } = firebase.auth;
    // 파이어베이스 로그인상태일시 액세스 토큰전달
    if (currentUser) {
      const token = await currentUser.getIdToken(false);// Force refresh is false
      // eslint-disable-next-line no-param-reassign
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    Promise.reject(error);
  },
);
// 응답요청 후처리
Axios.interceptors.response.use(
  (response) => response,
  (error) => {
    const ERR_RESPONSE = error.response; // HTTP 에러정보
    const ERR_STATUS = error.response.status; // HTTP 상태코드

    // 400번대 에러, 클라이언트 에러 처리
    if (ERR_STATUS >= 400 && ERR_STATUS <= 499) {
      if (ERR_STATUS === 400 && ERR_RESPONSE?.data) {
        // 400번 에러 서버에서 처리한 클라이언트 에러
        Vue.prototype.$toast.warning(ERR_RESPONSE.data.message);
        // 에러에 따라서 홈화면으로 이동여부
        if (ERR_RESPONSE.data.moveToHome) {
          Vue.router.push({ name: 'home.index' });
        }
      } else if (ERR_STATUS === 401) {
        // 401번 에러, 인증실패
        Vue.prototype.$toast.warning(message.invalidUser);
        // 인증정보가 이상한 경우 로그아웃한다
        store.dispatch('logout');
      } else {
        // 400번대 에러지만 서버에서 처리하지 못한 내용
        Vue.prototype.$toast.warning(message.error400);
        // 홈화면으로 이동
        Vue.router.push({ name: 'home.index' });
      }
    } else if (ERR_STATUS >= 500 && ERR_STATUS <= 599) {
    // 500번대 에러, 서버에러
      if (ERR_STATUS === 500 && ERR_RESPONSE?.data) {
        // 500번 에러 서버에서 처리한 클라이언트 에러
        Vue.prototype.$toast.warning(ERR_RESPONSE.data.message);
      } else {
        // 500번대 에러지만 서버에서 처리하지 못한 내용
        Vue.prototype.$toast.warning(message.error500);
      }
      // 홈화면으로 이동
      Vue.router.push({ name: 'home.index' });
    }
    // 에러반환
    return Promise.reject(error);
  },
);

// Bind Axios to Vue.
Vue.$http = Axios;
Object.defineProperty(Vue.prototype, '$http', {
  get() {
    return Axios;
  },
});
