<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 추천 일정 -->
      <v-list :param-list="recommendedList">
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
        value: '11',
        text: '11111111111111111111111',
      }, {
        value: '22',
        text: '22222222222222222',
      },
      {
        value: '33',
        text: '333333333333333',
      },
      {
        value: '44',
        text: '4444444444444444444444',
      },
      {
        value: '55',
        text: '555555555555555555555',
      },
      {
        value: '66',
        text: '66666666666666666666666',
      },
      ];
    },
  },

};
</script>
