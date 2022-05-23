<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 할일 일정 -->
      <v-list
        :param-list="todolist"
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
      // todolist: [], // 할일 일정 리스트
    };
  },
  computed: {
    // 유저정보 (store에서 값이 변경될때마다 갱신)
    user() {
      return this.$store.getters.user;
    },
    // 유저 선택 정보
    selection() {
      return this.$store.getters.selection;
    },
    // 선택된 할일리스트 (store에서 값이 변경될때마다 갱신)
    todolist() {
      return this.$store.getters.todolist;
    },
  },
  created() {
    this.initTodoList(); // 할일 일정 초기화 (최대 5개 호출)
  },
  methods: {
    // 할일 일정 초기화
    initTodoList() {
      // 로그인상태일시 나의 할일 일정 취득
      this.$store.dispatch('setInitTodoList');
    },
    // 할일 일정 체크박스 선택
    selectTodoCheckInput(param) {
      const checkedItem = param;
      checkedItem.listKind = 'todo';
      this.$store.dispatch('updateList', checkedItem);
    },
  },

};
</script>
