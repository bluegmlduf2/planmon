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
// 응답요청 전처리
Axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      store.dispatch('auth/logout');
    }

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
