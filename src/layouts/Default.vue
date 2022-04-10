<template>
  <!-- <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <router-link
        :to="{ name: 'home.index' }"
        class="navbar-brand"
      >
        Vue 2 Boilerplate
      </router-link>

      <button
        class="navbar-toggler"
        type="button"
        @click="toggleMenu"
      >
        <span class="navbar-toggler-icon" />
      </button>

      <div
        :class="{ show : menuCollapsed}"
        class="collapse navbar-collapse"
      >
        <ul class="navbar-nav mr-auto">
          <router-link
            :to="{ name: 'home.index' }"
            active-class="active"
            class="nav-item"
            tag="li"
          >
            <a class="nav-link">
              Home
            </a>
          </router-link>
          <router-link
            :to="{ name: 'account.index' }"
            active-class="active"
            class="nav-item"
            tag="li"
          >
            <a class="nav-link">
              Account
            </a>
          </router-link>
        </ul>
        <span class="navbar-text">
          <a
            class="btn btn-secondary"
            href="#"
            @click.prevent="logout"
          >
            <i class="fa fa-sign-out" />
          </a>
        </span>
      </div>
    </nav>

    <div class="container pt-4">
      <div class="row">
        <div class="col col-12">
          Content will be placed here
          <slot />
        </div>
      </div>
    </div>
  </div> -->
  <div class="container default-body">
    <div class="row justify-content-md-center default-background mt-md-1 mt-lg-1">
      <div
        :class="{leftmenuactive:isLeftMenuActive}"
        class="col-md-4 default-left p-5"
      >
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
          <div class="overlay-menu">
            <ul>
              <li>
                <router-link :to="{ name: 'home.index' }">
                  Home
                </router-link>
              </li>
              <li>
                <router-link to="#">
                  About
                </router-link>
              </li>
              <li>
                <router-link to="#">
                  News
                </router-link>
              </li>
            </ul>
          </div>
        </div>
        <!-- 왼쪽 타이틀 -->
        <div
          v-if="!isMenuActive"
          class="default-welcome"
        >
          <h1>
            <router-link :to="{ name: 'home.index' }">
              Planmon
            </router-link>
          </h1>
          <p>플랜몬에 오신것을 환영합니다!</p>
        </div>
        <!-- 검색입력 -->
        <div class="search-bar">
          <div class="input-groupt">
            <button class="btn">
              <i
                class="fa fa-search"
                aria-hidden="true"
              />
            </button>
            <input
              type="search"
              class="form-control"
              placeholder="추천 일정 검색"
            >
          </div>
        </div>
        <!-- 검색 조건 -->
        <div
          class="search-condition d-none d-sm-none d-md-block d-lg-block d-xl-block"
          :class="[isConditionActive?'d-block d-sm-block':'d-none d-sm-none']"
        >
          <!-- 검색 조건 국가선택 -->
          <div class="form-group">
            <span class="sm-title">국가선택</span>
            <select
              id="exampleFormControlSelect1"
              v-model="selectedCountry"
              class="form-control"
            >
              <option
                v-for="country in countries"
                :key="country.value"
                :value="country.value"
              >
                {{ country.text }}
              </option>
            </select>
          </div>
          <!-- 검색 조건 입국날짜 선택 -->
          <span class="sm-title">입국날짜</span>
          <div class="input-group entry-date-form">
            <flat-pickr
              id="entryDate"
              v-model="entryDate"
              :config="config"
              class="form-control flat-pickr"
              placeholder="입국날짜를 선택해주세요"
            />
          </div>
        </div>
        <!-- 할일목록 -->
        <div
          v-if="!isMenuActive"
          class="search-todoList d-none d-sm-none d-md-block d-lg-block d-xl-block"
          :class="[isConditionActive?'d-block d-sm-block':'d-none d-sm-none']"
        >
          <div class="search-todoList-title">
            <span class="sm-title">할일 항목</span>
            <span>4/22</span>
          </div>
          <div class="progress">
            <div
              class="progress-bar"
              role="progressbar"
              aria-valuenow="25"
              aria-valuemin="0"
              aria-valuemax="100"
              style="width:25%"
            />
          </div>
          <div class="search-todoList-status">
            <div>
              <router-link :to="{ name: 'completelist.index' }">
                <h3 class="status-total">
                  11
                </h3>
                <p class="status-title">
                  완료된
                </p>
                <p class="status-title-mini">
                  일정
                </p>
              </router-link>
            </div>
            <div>
              <router-link :to="{ name: 'todolist.index' }">
                <h3 class="status-total">
                  11
                </h3>
                <p class="status-title">
                  다가오는
                </p>
                <p class="status-title-mini">
                  일정
                </p>
              </router-link>
            </div>
            <div>
              <router-link :to="{ name: 'alllist.index' }">
                <h3 class="status-total">
                  11
                </h3>
                <p class="status-title">
                  모든
                </p>
                <p class="status-title-mini">
                  일정
                </p>
              </router-link>
            </div>
          </div>
        </div>
        <!-- 모바일화면에서 내 정보 열기 -->
        <div
          class="list-footer d-block d-sm-block d-md-none d-lg-none d-xl-none"
        >
          <button
            type="button"
            class="btn btn-light w-100 mt-4"
            @click="isConditionActive=!isConditionActive"
          >
            {{ isConditionActive?'내 정보 닫기':'내 정보 열기' }}
          </button>
        </div>
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
import korean from 'flatpickr/dist/l10n/ko';
import countriesList from '@/assets/js/countries';

export default {
  /**
   * The name of the layout.
   */
  name: 'DefaultLayout',
  /**
   * The properties that the component accepts.
   */
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
      menuCollapsed: false,
      isMenuActive: false, // NAV메뉴 활성화유무
      isConditionActive: false, // 나의 일정 정보 표시 유무
      entryDate: null, // 입국날짜
      countries: [], // 국가
      selectedCountry: null, // 선택된 국가
      config: {
        wrap: true,
        altFormat: 'Y년 M J',
        altInput: true,
        dateFormat: 'Y-m-d',
        locale: korean.ko,
        disableMobile: 'true', // flatpicker모바일모드끄기
      },
    };
  },
  created() {
    this.initEntyDate(); // 입국날짜 초기화
    this.initCountries(); // 국가 초기화
  },
  /**
   * The methods that the layout can use.
   */
  methods: {
    // 입국날짜 초기화
    initEntyDate() {
      const todayDate = new Date().toISOString().slice(0, 10); // 오늘날짜를 yyyy-mm-dd 형식으로 받는다
      this.entryDate = todayDate;
    },
    // 국가 초기화
    initCountries() {
      this.countries = countriesList;
    },

    /**
     * Will log the user out.
     */
    logout() {
      this.$store.dispatch('auth/logout');
    },

    /**
     * Will toggle the menu.
     */
    toggleMenu() {
      this.menuCollapsed = !this.menuCollapsed;
    },
  },
};
</script>
