<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 다가오는 일정 -->
      <v-list
        :param-list="todoList"
        :param-show-buttons="true"
        :param-is-add="true"
        @updateCheckInput="selectTodoCheckInput"
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
import ListProxy from '@/proxies/ListProxy';

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
      new ListProxy()
        .getTodoList()
        .then((response) => {
          this.todoList = response.data;
        })
        .catch(() => {
          console.log('Request failed...');
        });
    },
    // 다가오는 일정 체크박스 선택
    selectTodoCheckInput(param) {
      const checkedItem = param;
      checkedItem.listKind = 'todo';
      this.$store.dispatch('updateList', checkedItem);
    },
  },

};
</script>
