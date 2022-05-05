<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 추천 일정 -->
      <v-list
        :param-list="recommendedList"
        :param-show-buttons="false"
        :param-is-add="true"
        @updateCheckInput="selectRecCheckInput"
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
          추천 일정
        </span>
        <span slot="deleteList" />
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
  name: 'ReclistIndex',

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
      recommendedList: [], // 추천 일정 리스트
    };
  },
  created() {
    this.initRecommendedList(); // 추천 일정 초기화  (최대 5개 호출)
  },

  methods: {
    // 추천 일정 초기화
    initRecommendedList() {
      this.recommendedList = [{
        value: '1a',
        text: '첫번째 추천일정',
      }, {
        value: '2a',
        text: '두번째 추천일정',
      },
      {
        value: '3a',
        text: '세번째 추천일정',
      },
      {
        value: '4a',
        text: '네번째 추천일정',
      },
      ];
    },
    // 추천 일정 체크박스 선택
    selectRecCheckInput(param) {
      const checkedItem = param;
      checkedItem.listKind = 'rec';
      this.$store.dispatch('updateList', checkedItem);
    },
  },

};
</script>
