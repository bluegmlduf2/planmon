<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 모든 일정 -->
      <v-list
        :param-list="alllist"
        :param-show-buttons="true"
        @updateCheckInput="selectAllCheckInput"
      >
        <div slot="search">
          <v-search
            @searchList="searchAllList"
          />
        </div>
        <span
          slot="header"
        >
          모든 일정
        </span>
      </v-list>
      <div
        class="list-footer"
      />
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
  name: 'AlllistIndex',

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
    alllist() {
      return this.$store.getters.alllist;
    },
  },
  created() {
    this.initAllList(); // 모든 일정 초기화  (최대 5개 호출)
  },

  methods: {
    // 추천 일정 초기화
    async initAllList() {
      // 사용자 선택값 데이터 초기화
      await this.$store.dispatch('setInitSelection');
      // 모든 일정 취득
      await this.$store.dispatch('setInitAllList');
    },
    // 모든 일정 체크박스 선택
    selectAllCheckInput(param) {
      const checkedItem = param;
      // 체크한 대상이 할일일정인지 완료일정인지 구분
      checkedItem.listKind = checkedItem.hidden ? 'all_complete' : 'all_todo';
      this.$store.dispatch('updateList', checkedItem);
    },
    // 결과내 재검색 기능
    searchAllList(searchWord) {
      // 결과내 재검색어
      this.searchWord = searchWord;
      // 모든일정 초기화를 위한 파라미터
      const param = { searchWord };
      // 할일일정 초기화
      this.$store.dispatch('setInitAllList', param);
    },
  },
};
</script>
