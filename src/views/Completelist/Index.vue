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
      // completelist: [], // 완료 일정 리스트
    };
  },
  computed: {
    // 선택된 완료리스트 (store에서 값이 변경될때마다 갱신)
    completelist() {
      return this.$store.getters.completelist;
    },
  },
  created() {
    this.initCompleteList(); // 완료 일정 초기화
  },

  methods: {
    // 완료 일정 초기화
    initCompleteList() {
      // 완료 일정 취득
      this.$store.dispatch('setInitCompleteList');
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
