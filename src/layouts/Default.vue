<template>
  <div class="container default-body">
    <Login
      :is-login="isLoginActive"
      @closeLogin="isMenuActive=false,isLoginActive=false"
    />
    <div class="row justify-content-md-center default-background mt-md-1 mt-lg-1">
      <div
        :class="{leftmenuactive:isLeftMenuActive,'mb-5':isMenuActive}"
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
          <div
            :class="{'overlay-menu':!isConditionActive&&userIsAuthenticated}"
          >
            <ul>
              <li>
                <router-link :to="{ name: 'home.index' }">
                  Home
                </router-link>
              </li>
              <li>
                <a
                  v-if="userIsAuthenticated"
                  href="#"
                  @click="onLogout"
                >
                  로그아웃
                </a>
                <a
                  v-else
                  href="#"
                  @click="isLoginActive = true"
                >
                  로그인
                </a>
              </li>
              <li v-if="userIsAuthenticated">
                <router-link :to="{ name: 'setting.index' }">
                  설정
                </router-link>
              </li>
              <li v-if="userIsAuthenticated">
                <router-link :to="{ name: 'write.index' }">
                  글쓰기
                </router-link>
              </li>
              <li v-if="userIsAuthenticated">
                <router-link :to="{ name: 'mylist.index' }">
                  내가 작성한 일정
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
          <p><span v-if="!!user">{{ !!user.name?user.name:user.email }}님<br></span> 플랜몬에 오신것을 환영합니다!</p>
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
          :class="[isConditionActive?'d-block d-sm-block':'d-none d-sm-none']"
        >
          <div class="search-todoList-title">
            <span class="sm-title">할일 항목</span>
            <span>{{ `${completelist.length}/${alllist}` }}</span>
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
                  {{ completelist.length }}
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
                  {{ todolist.length }}
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
                  {{ alllist }}
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
import countriesList from '@/assets/js/countries';
import stayStatusList from '@/assets/js/stayStatus';
import message from '@/assets/js/message';
import Login from '@/views/Login/Index.vue';
import Flatpickr from '@/components/FlatpickrDefault.vue';

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
      menuCollapsed: false,
      isLoginActive: false, // 로그인화면 활성화유무
      isMenuActive: false, // NAV메뉴 활성화유무
      isConditionActive: false, // 나의 일정 정보 표시 유무
      countriesList: [], // 국가 리스트
      stayStatusList: [], // 체류상태 리스트
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
    // 선택된 TODO리스트 (store에서 값이 변경될때마다 갱신)
    todolist() {
      return this.$store.getters.selection.todolist;
    },
    // 선택된 완료리스트 (store에서 값이 변경될때마다 갱신)
    completelist() {
      return this.$store.getters.selection.completelist;
    },
    // 선택된 모든리스트의 길이 (store에서 값이 변경될때마다 갱신)
    alllist() {
      return this.$store.getters.selection.todolist.length + this.$store.getters.selection.completelist.length;
    },
    // 선택된 모든리스트의 길이 (store에서 값이 변경될때마다 갱신)
    progressPercent() {
      // eslint-disable-next-line no-mixed-operators
      const percent = this.completelist.length / this.alllist * 100;
      return percent;
    },
  },

  created() {
    this.initCountries(); // 국가 리스트 초기화
    this.initStayStatus(); // 체류상태 리스트 초기화
    this.$store.dispatch('setInitSelection'); // 초기선택값 데이터 초기화
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

    // 로그아웃
    onLogout() {
      this.isMenuActive = false; // nav메뉴 닫기
      this.$store.dispatch('logout');
      this.$toast.info(message.logout);
      this.$router.go(this.$router.currentRoute);
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
