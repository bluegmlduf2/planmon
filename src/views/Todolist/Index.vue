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
      >
        <button
          v-if="todolistPage.hasNext"
          type="button"
          class="btn btn-light w-100"
          @click="$store.dispatch('getTodoList')"
        >
          +
        </button>
      </div>
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
  /**
   * The properties that the component accepts.
   */
  props: {
    // 초기화시 일정을 20개를 표시한다
    get20perpage: {
      default: false,
      type: Boolean,
    },
  },
  computed: {
    // 선택된 할일리스트 (store에서 값이 변경될때마다 갱신)
    todolist() {
      return this.$store.getters.todolist;
    },
    // 할일일정화면의 페이지네이션 정보
    todolistPage() {
      return this.$store.getters.todolistPage;
    },
  },
  created() {
    this.initTodoList(); // 할일 일정 초기화 (최대 5개 호출)
  },
  methods: {
    // 할일 일정 초기화
    async initTodoList() {
      // 사용자 선택값 데이터 초기화
      await this.$store.dispatch('setInitSelection');
      // 로그인상태일시 나의 할일 일정 취득
      await this.$store.dispatch('setInitTodoList', this.get20perpage);
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
