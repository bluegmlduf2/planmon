/* ============
 * Main File
 * ============
 *
 * Will initialize the application.
 */

import Vue from 'vue';

/* ============
 * Plugins
 * ============
 *
 * Import and bootstrap the plugins.
 * bootstrap 4.6 버전
 */

import './plugins/vuex';
import './plugins/axios';
import firebase from './plugins/firebase';
import { i18n } from './plugins/vue-i18n';
import { router } from './plugins/vue-router';
import './plugins/vuex-router-sync';
import './plugins/bootstrap';
import './plugins/font-awesome';
import './plugins/register-service-worker';
import './plugins/flatpickr';
import './plugins/vue-toastification';

/* ============
 * Styling
 * ============
 * http://stylus-lang.com/
 */

import './assets/stylus/app.styl';

/* ============
 * Main App
 * ============
 *
 * Last but not least, we import the main application.
 */

import App from './App.vue';
import store from './store';

Vue.config.productionTip = false;

let app;

firebase.onAuthStateChanged(firebase.auth, (user) => {
  if (user) {
    // 기존 로그인 정보가 있을시 유저정보 기존 유저정보 갱신
    store.dispatch('autoSignIn', user);
  } else {
    // 유저로그인 정보가 없을때 항상 이메일 로그인인지 확인한다
    // 이메일인증부분
    store.dispatch('signInWithEmailLink');
  }

  // 로그인, 로그아웃시 뷰객체를 1회만 생성, 1회만 실행
  if (!app) {
  /* eslint-disable no-new */
    app = new Vue({
    /**
     * Bind the Vue instance to the HTML.
     */
      el: '#app',

      /**
     * The localization plugin.
     */
      i18n,

      /**
     * The router.
     */
      router,

      /**
     * The Vuex store.
     */
      store,

      created() {
        // 최초화면표시, 화면새로고침시, 로그인 로그아웃시 최초실행(전역초기값)
        // 사용자 선택사항 초기화
        store.dispatch('setInitSelection');
      },
      /**
     * Will render the application.
     *
     * @param {Function} h Will create an element.
     */
      render: (h) => h(App),
    });
  }
});
