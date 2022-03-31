<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 다가오는 일정 -->
      <v-list :param-list="todoList">
        <div slot="search">
          <v-search>
            <input
              slot="searchBtn"
              type="search"
              placeholder="결과 내 재검색"
              class="form-control"
            >
          </v-search>
        </div>
        <span
          slot="header"
        >
          다가오는 일정
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
  name: 'TodolistIndex',

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
      todoList: [], // 다가오는 일정 리스트
    };
  },
  created() {
    this.initTodoList(); // 다가오는 일정 초기화 (최대 5개 호출)
  },

  methods: {
    // 다가오는 일정 초기화
    initTodoList() {
      this.todoList = [{
        value: '1',
        text: '일본11111111111111111111111111111111111',
      }, {
        value: '2',
        text: '미국222222222222',
      },
      {
        value: '3',
        text: '중국33333333333333333333',
      },
      {
        value: '4',
        text: '4444444444444444444444',
      },
      {
        value: '5',
        text: '555555555555555555555',
      },
      {
        value: '6',
        text: '66666666666666666666666',
      },
      ];
    },
  },

};
</script>
