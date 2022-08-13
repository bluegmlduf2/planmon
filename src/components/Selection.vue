<template>
  <!-- 유저선택정보화면  -->
  <div class="selection-container">
    <!-- 뒤로가기버튼영역 -->
    <div class="d-block d-sm-block d-md-none d-lg-none d-xl-none w-100">
      <div class="row mt-2 mb-3 d-flex align-items-start justify-content-start ml-1">
        <div class="post-back ml-3">
          <span @click="$router.push({name: 'home.index'})">
            <i
              class="fa fa-chevron-left"
              aria-hidden="true"
            />
          </span>
        </div>
      </div>
    </div>
    <!-- 검색 조건 -->
    <div
      class="search-condition"
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
      class="search-todoList"
    >
      <div class="search-todoList-title">
        <span class="sm-title">할일 항목</span>
        <span>{{ `${completelistCount}/${alllistCount}` }}</span>
      </div>
      <div class="progress status_mobile_color">
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
          <router-link
            :to="{ name: 'completelist.index' }"
            class="status_mobile_color"
          >
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
          <router-link
            :to="{ name: 'todolist.index' }"
            class="status_mobile_color"
          >
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
          <router-link
            :to="{ name: 'alllist.index' }"
            class="status_mobile_color"
          >
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
</template>

<script>
import countriesList from '@/assets/js/countries';
import stayStatusList from '@/assets/js/stayStatus';
import message from '@/assets/js/message';
import Flatpickr from '@/components/FlatpickrDefault.vue';

export default {
  /**
   * The name of the component.
   */
  name: 'Selection',

  components: {
    Flatpickr,
  },
  props: {
    // 라우트로 화면이동시 데이터초기화 필요유무를 확인을 위해 전달된 매개변수
    isRoutedRequest: {
      default: false,
      type: Boolean,
    },
  },

  data() {
    return {
      countriesList: [], // 국가 리스트
      stayStatusList: [], // 체류상태 리스트
      searchRecWord: '', // 추천일정검색 단어
    };
  },
  computed: {
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
    this.initSelectionList(); // 나의 일정 설정화면에 필요한 데이터 초기화
    this.initCountries(); // 국가 리스트 초기화
    this.initStayStatus(); // 체류상태 리스트 초기화
  },

  methods: {
    // 나의 일정 설정화면에 필요한 데이터 초기화
    async initSelectionList() {
      // 해당화면을 화면이동으로 표시한 경우 데이터 초기화
      if (this.isRoutedRequest) {
        // 사용자 선택값 데이터 초기화
        await this.$store.dispatch('setInitSelection');
        // 홈화면의 할일일정 초기화 (표시용)
        await this.$store.dispatch('setInitTodoList');
        // 홈화면의 추천일정 초기화 (표시용)
        await this.$store.dispatch('setInitRecList');
      }
    },
    // 국가 초기화
    initCountries() {
      this.countriesList = countriesList;
    },

    // 체류상태 초기화
    initStayStatus() {
      this.stayStatusList = stayStatusList;
    },
  },
};
</script>
