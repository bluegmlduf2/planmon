<template>
  <div class="container default-body">
    <Spinner />
    <Login
      :is-login="isLoginActive"
      @closeLogin="isMenuActive=false,isLoginActive=false"
    />
    <!-- 모바일 NAV바 시작-->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark d-md-none d-lg-none d-xl-none">
      <router-link
        class="navbar-brand"
        :to="{ name: 'home.index'}"
      >
        Planmon
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon" />
      </button>

      <div
        id="navbarSupportedContent"
        class="collapse navbar-collapse"
      >
        <!-- 모바일용 NAV메뉴 -->
        <NavMenu
          :is-for-mobile-nav="true"
          :user-is-authenticated="userIsAuthenticated"
          :is-menu-active="isMenuActive"
          @closeMenuActive="isMenuActive=false"
          @openLoginActive="isLoginActive=true"
        />
        <!-- 추천검색입력 -->
        <SearchRecList class="w-100 mt-2 mb-2" />
      </div>
    </nav>
    <!-- 데스크탑 왼쪽화면 -->
    <div class="row justify-content-md-center default-background mt-md-1 mt-lg-1">
      <div
        :class="{leftmenuactive:isLeftMenuActive,'mb-5':isMenuActive}"
        class="col-md-4 default-left p-5"
      >
        <!-- 데스크탑용 NAV -->
        <!-- 햄버거버튼 -->
        <div
          class="button_container"
          :class="{active:isMenuActive}"
          @click="isMenuActive=!isMenuActive"
        >
          <span class="top-bar" />
          <span class="middle-bar" />
          <span class="bottom-bar" />
        </div>
        <!-- 햄버거버튼 오버레이 -->
        <div
          class="overlay"
          :class="[isMenuActive?'open':'']"
        >
          <div>
            <!-- 데스크탑용 NAV메뉴 -->
            <NavMenu
              :is-for-mobile-nav="false"
              :user-is-authenticated="userIsAuthenticated"
              :is-menu-active="isMenuActive"
              @closeMenuActive="isMenuActive=false"
              @openLoginActive="isLoginActive=true"
            />
          </div>
        </div>
        <!-- 왼쪽 타이틀 -->
        <div
          v-if="!isMenuActive"
          class="default-welcome"
        >
          <h1>
            <router-link
              :to="{ name: 'home.index' }"
            >
              Planmon
            </router-link>
          </h1>
          <p><span v-if="!!user">{{ !!user.name?user.name:user.email }}님<br></span> 플랜몬에 오신것을 환영합니다!</p>
        </div>
        <!-- 검색입력 -->
        <div class="search-bar">
          <div class="input-groupt">
            <button
              class="btn"
              @click="searchRecList"
            >
              <i
                class="fa fa-search"
                aria-hidden="true"
              />
            </button>
            <input
              v-model="searchRecWord"
              type="search"
              class="form-control"
              placeholder="추천 일정 검색"
              @keyup.enter="searchRecList"
            >
          </div>
        </div>
        <!-- 유저선택정보 -->
        <Selection />
      </div>
      <slot name="default-right-body" />
    </div>
  </div>
</template>

<script>
/* ============
 * Default Layout
 * ============
 *
 * Used for the home and account pages.
 *
 * Layouts are used to store a lot of shared code.
 * This way the app stays clean.
 */
// eslint-disable-next-line import/extensions
import Login from '@/views/Login/Index.vue';
import NavMenu from '@/components/NavMenu.vue';
import Spinner from '@/components/Spinner.vue';
import Selection from '@/components/Selection.vue';

export default {
  /**
   * The name of the layout.
   */
  name: 'DefaultLayout',
  /**
   * The properties that the component accepts.
   */
  components: {
    Login,
    Spinner,
    NavMenu,
    Selection,
  },
  props: {
    // 왼쪽메뉴 표시여부
    isLeftMenuActive: {
      default: false,
      type: Boolean,
    },
  },
  /**
   * The data that can be used by the page.
   *
   * @returns {Object} The view-model data.
   */
  data() {
    return {
      isLoginActive: false, // 로그인화면 활성화유무
      isMenuActive: false, // NAV메뉴 활성화유무
    };
  },

  computed: {
    // 유저 인증정보 (store에서 갱신된 유저인증정보 취득)
    userIsAuthenticated() {
      return this.$store.getters.user !== null && this.$store.getters.user !== undefined;
    },
    // 유저정보 (store에서 값이 변경될때마다 갱신)
    user() {
      return this.$store.getters.user;
    },
  },
};
</script>
