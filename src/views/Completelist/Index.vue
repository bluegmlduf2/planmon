<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 완료 일정 -->
      <v-list
        :param-list="completeList"
        :param-show-buttons="false"
        :param-is-add="false"
        @updateCheckInput="selectCompleteCheckInput"
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
          완료된 일정
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
      completeList: [], // 완료 일정 리스트
    };
  },
  created() {
    this.initCompleteList(); // 완료 일정 초기화
  },

  methods: {
    // 완료 일정 초기화
    initCompleteList() {
      this.completeList = [{
        value: '1a',
        text: '첫번째 완료일정',
      }, {
        value: '2a',
        text: '두번째 완료일정',
      },
      ];
    },
    // 완료된 일정 체크박스 선택
    selectCompleteCheckInput(param) {
      const checkedItem = param;
      checkedItem.listKind = 'complete';
      this.$store.dispatch('updateList', checkedItem);
    },
  },

};
</script>
