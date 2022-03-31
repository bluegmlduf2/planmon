<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 추천 일정 -->
      <v-list :param-list="recommendedList">
        <div slot="search">
          <h4 class="list-search">
            검색
          </h4>
          <div class="input-groupt">
            <button class="btn">
              <i
                aria-hidden="true"
                class="fa fa-search"
              />
            </button><input
              type="search"
              placeholder="결과 내 재검색"
              class="form-control"
            >
          </div>
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
