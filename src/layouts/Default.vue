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
        <!-- 모바일용 NAV메뉴 컴포넌트-->
        <NavMenu
          :is-for-mobile-nav="true"
          :user-is-authenticated="userIsAuthenticated"
          :is-menu-active="isMenuActive"
          @closeMenuActive="isMenuActive=false"
          @openLoginActive="isLoginActive=true"
        />
        <!-- 추천검색입력 -->
        <form class="form-inline my-2 my-lg-0">
          <input
            v-model="searchRecWord"
            class="form-control mr-sm-2"
            type="search"
            placeholder="추천 일정 검색"
            aria-label="Search"
            @keyup.enter="searchRecList"
          >
          <button
            class="btn btn-outline-light my-2 my-sm-0"
            @click="searchRecList"
          >
            <i
              class="fa fa-search"
              aria-hidden="true"
            />
          </button>
        </form>
      </div>
    </nav>
    <!-- 모바일 NAV바 종료-->
    <div class="row justify-content-md-center default-background mt-md-1 mt-lg-1">
      <div
        :class="{leftmenuactive:isLeftMenuActive,'mb-5':isMenuActive}"
        class="col-md-4 default-left p-5"
      >
        <!-- 데스크탑용 NAV 시작-->
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
            <!-- 데스크탑용 NAV메뉴 컴포넌트-->
            <NavMenu
              :is-for-mobile-nav="false"
              :user-is-authenticated="userIsAuthenticated"
              :is-menu-active="isMenuActive"
              @closeMenuActive="isMenuActive=false"
              @openLoginActive="isLoginActive=true"
            />
          </div>
        </div>
        <!-- 데스크탑용 NAV 종료-->
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
        <!-- 검색 조건 -->
        <div
          class="search-condition d-none d-sm-none d-md-block d-lg-block d-xl-block"
        >
          <!-- 검색 조건 국가선택 -->
          <div class="form-group">
            <span class="sm-title">국가선택</span>
            <select
              v-model="country"
              class="form-control"
            >
              <option
                value="null"
                selected
                disabled
              >
                국가를 선택해주세요
              </option>
              <option
                v-for="e in countriesList"
                :key="e.value"
                :value="e.value"
              >
                {{ e.text }}
              </option>
            </select>
          </div>
          <!-- 검색 조건 체류상태 선택 -->
          <div class="form-group">
            <span class="sm-title">체류상태</span>
            <select
              v-model="stayStatus"
              class="form-control"
            >
              <option
                value="null"
                selected
                disabled
              >
                체류상태를 선택해주세요
              </option>
              <option
                v-for="e in stayStatusList"
                :key="e.value"
                :value="e.value"
              >
                {{ e.text }}
              </option>
            </select>
          </div>
          <!-- 검색 조건 입국날짜 선택 -->
          <span class="sm-title">입국날짜</span>
          <div class="input-group entry-date-form">
            <Flatpickr
              placeholder="입국날짜를 선택해주세요"
            />
          </div>
          <small
            class="form-text entry-date-form-small"
          >체류중인 경우에만 선택</small>
        </div>
        <!-- 할일목록 -->
        <div
          v-if="!isMenuActive"
          class="search-todoList d-none d-sm-none d-md-block d-lg-block d-xl-block"
        >
          <div class="search-todoList-title">
            <span class="sm-title">할일 항목</span>
            <span>{{ `${completelistCount}/${alllistCount}` }}</span>
          </div>
          <div class="progress">
            <div
              class="progress-bar"
              role="progressbar"
              aria-valuenow="25"
              aria-valuemin="0"
              aria-valuemax="100"
              :style="{'width':progressPercent+'%'}"
            />
          </div>
          <div class="search-todoList-status">
            <div>
              <router-link :to="{ name: 'completelist.index' }">
                <h3 class="status-total">
                  {{ completelistCount }}
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
                  {{ todolistCount }}
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
                  {{ alllistCount }}
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
import countriesList from '@/assets/js/countries';
import stayStatusList from '@/assets/js/stayStatus';
import message from '@/assets/js/message';
import Login from '@/views/Login/Index.vue';
import Flatpickr from '@/components/FlatpickrDefault.vue';
import NavMenu from '@/components/NavMenu.vue';
import Spinner from '@/components/Spinner.vue';

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
    Flatpickr,
    Spinner,
    NavMenu,
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
      countriesList: [], // 국가 리스트
      stayStatusList: [], // 체류상태 리스트
      searchRecWord: '', // 추천일정검색 단어
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
    // 선택한 항목 리스트 (갱신도 필요하기에 setter(mutation)도 등록)
    country: {
      get() {
        return this.$store.getters.selection.country;
      },
      set(value) {
        if (!this.user) {
          this.$toast.info(message.localStorageAlert);
        }
        this.$store.dispatch('addSelection', { country: value });
      },
    },
    stayStatus: {
      get() {
        return this.$store.getters.selection.stayStatus;
      },
      set(value) {
        if (!this.user) {
          this.$toast.info(message.localStorageAlert);
        }
        this.$store.dispatch('addSelection', { stayStatus: value });
      },
    },
    // 선택된 할일 리스트의 수
    todolistCount() {
      return this.$store.getters.todolistCount;
    },
    // 선택된 완료 리스트의 수
    completelistCount() {
      return this.$store.getters.completelistCount;
    },
    // 선택된 모든리스트의 수
    alllistCount() {
      return this.todolistCount + this.completelistCount;
    },
    // 선택된 모든리스트의 길이
    progressPercent() {
      // eslint-disable-next-line no-mixed-operators
      const percent = this.completelistCount / this.alllistCount * 100;
      return percent || 0;
    },
  },

  created() {
    this.initCountries(); // 국가 리스트 초기화
    this.initStayStatus(); // 체류상태 리스트 초기화
  },
  /**
   * The methods that the layout can use.
   */
  methods: {
    // 국가 초기화
    initCountries() {
      this.countriesList = countriesList;
    },

    // 체류상태 초기화
    initStayStatus() {
      this.stayStatusList = stayStatusList;
    },

    // 추천일정검색기능
    searchRecList() {
      // 검색어가 존재하지않고 추천일정화면이 아닌 경우
      if (this.searchRecWord !== '' && this.$route.path !== '/reclist') {
        // 추천일정 검색과 함께 추천페이지 이동
        this.$router.push({ name: 'reclist.index', params: { searchRecWord: this.searchRecWord } });
      } else if (this.$route.path === '/reclist') {
        // 만약 추천일정화면에서 재검색하는 경우 메세지 표시
        this.$toast.info(message.reSearch);
        this.searchRecWord = '';
      }
    },
  },
};
</script>
