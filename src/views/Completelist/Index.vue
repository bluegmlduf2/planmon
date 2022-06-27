<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 완료 일정 -->
      <v-list
        :param-list="completelist"
        :param-show-buttons="true"
        @updateCheckInput="selectCompleteCheckInput"
      >
        <div slot="search">
          <v-search
            @searchList="searchCompleteList"
          />
        </div>
        <span
          slot="header"
        >
          완료된 일정
        </span>
      </v-list>
      <div
        class="list-footer"
      >
        <button
          v-if="completelistPage.hasNext"
          type="button"
          class="btn btn-light w-100"
          @click="getCompleteList"
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
  name: 'CompetelistIndex',

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
    // 선택된 완료리스트 (store에서 값이 변경될때마다 갱신)
    completelist() {
      return this.$store.getters.completelist;
    },
    // 완료일정화면의 페이지네이션 정보
    completelistPage() {
      return this.$store.getters.completelistPage;
    },
  },
  created() {
    this.initCompleteList(); // 완료 일정 초기화
  },

  methods: {
    // 완료 일정 초기화
    async initCompleteList() {
      // 사용자 선택값 데이터 초기화
      await this.$store.dispatch('setInitSelection');
      // 완료 일정 취득
      await this.$store.dispatch('setInitCompleteList');
    },
    // 완료된 일정 체크박스 선택
    selectCompleteCheckInput(param) {
      const checkedItem = param;
      checkedItem.listKind = 'complete';
      this.$store.dispatch('updateList', checkedItem);
    },
    // 결과내 재검색 기능
    searchCompleteList(searchWord) {
      // 결과내 재검색어
      this.searchWord = searchWord;
      // 완료일정 초기화를 위한 파라미터
      const param = {
        get20perpage: false,
        searchWord,
      };
      // 할일일정 초기화
      this.$store.dispatch('setInitCompleteList', param);
    },
    // 검색 결과 더보기
    getCompleteList() {
      // 재검색어가 존재할 경우
      if (this.searchWord) {
        const param = { searchWord: this.searchWord };
        this.$store.dispatch('getCompleteList', param);
      } else {
        // 재검색어가 존재하지 않을 경우
        this.$store.dispatch('getCompleteList');
      }
    },
  },

};
</script>
