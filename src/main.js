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

/* eslint-disable no-new */
new Vue({
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

  // 파이어 베이스 인증정보 새로고침마다 갱신
  created() {
    firebase.onAuthStateChanged(firebase.auth, (user) => {
      if (user) {
        this.$store.dispatch('autoSignIn', user);
      }
    });
  },
  /**
   * Will render the application.
   *
   * @param {Function} h Will create an element.
   */
  render: (h) => h(App),
});
