/* ============
 * Vuex Store
 * ============
 *
 * The store of the application.
 *
 * http://vuex.vuejs.org/en/index.html
 */

import Vuex from 'vuex';
import createLogger from 'vuex/dist/logger';

// Modules
import list from './list';
import selection from './selection';
import post from './post';
import commemt from './commemt';
import commentreply from './commentreply';
import user from './user';
import image from './image';
import shared from './shared';

const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
  /**
   * Assign the modules to the store.
   */
  modules: {
    list,
    selection,
    post,
    user,
    image,
    shared,
    commemt,
    commentreply,
  },

  /**
   * If strict mode should be enabled.
   */
  // state의 값을 변경하는것을 mutation내에서만 가능하게 한다 (true)
  // 나의 경우는 Default.vue에서 사용하기때문에 false
  // production 모드에서 기본이 false
  strict: false,

  /**
   * Plugins used in the store.
   */
  plugins: debug ? [createLogger()] : [],
});
