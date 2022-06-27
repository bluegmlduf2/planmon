<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 내가 작성한 일정 -->
      <v-list
        :param-list="myList"
        :param-show-buttons="false"
        :param-show-checkbox="false"
      >
        <div slot="search">
          <v-search
            @searchList="searchMyList"
          />
        </div>
        <span
          slot="header"
        >
          내가 작성한 일정
        </span>
      </v-list>
      <div
        class="list-footer"
      >
        <button
          v-if="mylistPage.hasNext"
          type="button"
          class="btn btn-light w-100"
          @click="getMyList"
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
  name: 'MylistIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VList,
    VSearch,
  },
  data() {
    return {
      searchWord: '', // 재검색어
    };
  },
  computed: {
    // 선택된 모든리스트
    myList() {
      return this.$store.getters.mylist;
    },
    // 내가 작성한 일정화면의 페이지네이션 정보
    mylistPage() {
      return this.$store.getters.mylistPage;
    },
  },

  created() {
    this.initMyList(); // 내 일정 초기화  (최대 5개 호출)
  },

  methods: {
    // 내 일정 초기화
    async initMyList() {
      // 사용자 선택값 데이터 초기화
      await this.$store.dispatch('setInitSelection');
      // 나의 일정 취득
      await this.$store.dispatch('setInitMyList');
    },
    // 모든 일정 체크박스 선택
    selectAllCheckInput(param) {
      const checkedItem = param;
      // 체크한 대상이 할일일정인지 완료일정인지 구분
      checkedItem.listKind = checkedItem.hidden ? 'all_complete' : 'all_todo';
      this.$store.dispatch('updateList', checkedItem);
    },
    // 결과내 재검색 기능
    searchMyList(searchWord) {
      // 결과내 재검색어
      this.searchWord = searchWord;
      // 내가 작성한 일정 초기화를 위한 파라미터
      const param = { searchWord };
      // 할일일정 초기화
      this.$store.dispatch('setInitMyList', param);
    },
    // 검색 결과 더보기
    getMyList() {
      // 재검색어가 존재할 경우
      if (this.searchWord) {
        const param = { searchWord: this.searchWord };
        this.$store.dispatch('getMyList', param);
      } else {
        // 재검색어가 존재하지 않을 경우
        this.$store.dispatch('getMyList');
      }
    },
  },
};
</script>
