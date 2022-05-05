<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 모든 일정 -->
      <v-list
        :param-list="allList"
        :param-show-buttons="true"
        :param-is-add="true"
        @updateCheckInput="selectAllCheckInput"
      >
        <div slot="search">
          <v-search>
            <input
              slot="searchBtn"
              type="search"
              placeholder="결과 재검색"
              class="form-control"
            >
          </v-search>
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
      allList: [], // 추천 일정 리스트
    };
  },
  created() {
    this.initAllList(); // 추천 일정 초기화  (최대 5개 호출)
  },

  methods: {
    // 추천 일정 초기화
    initAllList() {
      this.allList = [{
        value: '1a',
        text: '첫번째 할일일정',
      }, {
        value: '2a',
        text: '두번째 완료일정',
        hidden: true,
      },
      ];
    },
    // 모든 일정 체크박스 선택
    selectAllCheckInput(param) {
      const checkedItem = param;
      // 체크한 대상이 할일일정인지 완료일정인지 구분
      checkedItem.listKind = checkedItem.hidden ? 'complete' : 'todo';
      this.$store.dispatch('updateList', checkedItem);
    },
  },

};
</script>
