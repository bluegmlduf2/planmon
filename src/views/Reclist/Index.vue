<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 추천 일정 -->
      <v-list
        :param-list="reclist"
        :param-show-buttons="false"
        @updateCheckInput="selectRecCheckInput"
      >
        <div slot="search">
          <v-search
            @searchList="searchRecList"
          />
        </div>
        <span
          slot="header"
        >
          추천 일정
        </span>
        <span slot="deleteList" />
      </v-list>
      <div
        class="list-footer"
      >
        <button
          v-if="reclistPage.hasNext"
          type="button"
          class="btn btn-light w-100"
          @click="getRecList"
        >
          +
        </button>
      </div>
    </div>
  </v-layout>
</template>

<script>
/* ============
 * Home Index Page
 * ============
 *
 * The home index page.
 */

import VLayout from '@/layouts/Default.vue';
import VList from '@/components/List.vue';
import VSearch from '@/components/Search.vue';

export default {
  /**
   * The name of the page.
   */
  name: 'ReclistIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VList,
    VSearch,
  },
  /**
   * The properties that the component accepts.
   */
  props: {
    // 메인화면에서 검색한 재검색어
    searchRecWord: {
      default: '',
      type: String,
    },
    // 초기화시 일정을 20개를 표시한다
    get20perpage: {
      default: false,
      type: Boolean,
    },
  },
  data() {
    return {
      searchWord: this.searchRecWord, // 재검색어 (props의 재사용 방지)
    };
  },
  computed: {
    // 선택된 할일리스트 (store에서 값이 변경될때마다 갱신)
    reclist() {
      return this.$store.getters.reclist;
    },
    // 추천일정화면의 페이지네이션 정보
    reclistPage() {
      return this.$store.getters.reclistPage;
    },
  },
  created() {
    this.initRecommendedList(); // 추천 일정 초기화  (최대 5개 호출)
  },

  methods: {
    // 추천 일정 초기화 (기본적으로 10개를 가져오며 홈화면에서 더보기 버튼 클릭시만 20개를 가져온다)
    async initRecommendedList() {
      // 추천일정 초기화를 위한 파라미터
      const param = { get20perpage: this.get20perpage, searchWord: this.searchWord };
      // 사용자 선택값 데이터 초기화
      await this.$store.dispatch('setInitSelection');
      // 추천일정 초기화
      await this.$store.dispatch('setInitRecList', param);
    },
    // 추천 일정 체크박스 선택
    selectRecCheckInput(param) {
      const checkedItem = param;
      checkedItem.listKind = 'rec';
      this.$store.dispatch('updateList', checkedItem);
    },
    // 결과내 재검색 기능
    searchRecList(searchWord) {
      // 결과내 재검색어
      this.searchWord = searchWord;
      // 추천일정 초기화를 위한 파라미터
      const param = { searchWord };
      // 추천일정 초기화
      this.$store.dispatch('setInitRecList', param);
    },
    // 검색 결과 더보기
    getRecList() {
      // 재검색어
      const param = { searchWord: this.searchWord };
      this.$store.dispatch('getRecList', param);
    },
  },

};
</script>
