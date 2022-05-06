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
        :param-is-add="true"
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
          내가 작성한 일정
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
      myList: [], // 내 일정 리스트
    };
  },
  created() {
    this.initMyList(); // 내 일정 초기화  (최대 5개 호출)
  },

  methods: {
    // 내 일정 초기화
    initMyList() {
      this.myList = [{
        value: '1a',
        text: '첫번째 할일일정',
        hidden: true,
      }, {
        value: '2a',
        text: '두번째 완료일정',
        hidden: true,
      }, {
        value: '3a',
        text: '세번째 완료일정',
        hidden: true,
      },
      ];
    },
  },

};
</script>
