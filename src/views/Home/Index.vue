<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
      :class="{'add-padding-bottom':user}"
    >
      <!-- 할일 일정 -->
      <v-list
        :param-list="todolist"
        :param-show-buttons="true"
        :param-is-home="true"
        @updateCheckInput="selectTodoCheckInput"
      >
        <span
          slot="header"
          class="cursor-pointer"
          @click="$router.push({name: 'todolist.index', params: {get20perpage:true}})"
        >
          다가오는 일정
        </span>
      </v-list>
      <div
        class="list-footer"
      >
        <button
          v-if="todolistCount > 9"
          type="button"
          class="btn btn-light w-100"
          @click="$router.push({name: 'todolist.index', params: {get20perpage:true}})"
        >
          +
        </button>
      </div>
      <hr>
      <!-- 추천 일정 -->
      <v-list
        :param-list="reclist"
        :param-show-buttons="false"
        :param-is-home="true"
        @updateCheckInput="selectRecCheckInput"
      >
        <span
          slot="header"
          class="cursor-pointer"
          @click="$router.push({name: 'reclist.index', params: {get20perpage:true}})"
        >
          추천 일정
        </span>
      </v-list>
      <div
        class="list-footer"
      >
        <button
          v-if="reclistCount > 9"
          type="button"
          class="btn btn-light w-100"
          @click="$router.push({name: 'reclist.index', params: {get20perpage:true}})"
        >
          +
        </button>
      </div>
      <button
        v-if="user"
        class="btn btn-purple btn-option home-write-position"
        @click="$router.push({name: 'write.index'})"
      >
        <b>
          글쓰기
        </b>
      </button>
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
  name: 'HomeIndex',
  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    VList,
  },
  computed: {
    // 유저정보 (store에서 값이 변경될때마다 갱신)
    user() {
      return this.$store.getters.user;
    },
    // 할일일정 리스트 (store에서 값이 변경될때마다 갱신)
    todolist() {
      return this.$store.getters.todolist;
    },
    // 추천일정 리스트 (store에서 값이 변경될때마다 갱신)
    reclist() {
      return this.$store.getters.reclist;
    },
    // 현재화면에 표시하고있는 할일일정 리스트 길이
    todolistCount() {
      return this.$store.getters.todolistCount;
    },
    // 현재화면에 표시하고있는 추천일정 리스트 길이
    reclistCount() {
      return this.$store.getters.reclistCount;
    },
  },
  created() {
    // 홈버튼 및 배너클릭으로 홈화면으로 돌아갈때 할일일정과 추천일정을 초기화한다
    this.initHomeList();
  },
  methods: {
    // 홈버튼 및 배너클릭으로 홈화면으로 돌아갈때 할일일정과 추천일정을 초기화한다
    async initHomeList() {
      // 사용자 선택값 데이터 초기화
      await this.$store.dispatch('setInitSelection');
      // 홈화면의 할일일정 초기화 (표시용)
      await this.$store.dispatch('setInitTodoList');
      // 홈화면의 추천일정 초기화 (표시용)
      await this.$store.dispatch('setInitRecList');
    },
    // 다가오는 일정 체크박스 선택
    selectTodoCheckInput(param) {
      const checkedItem = param;
      checkedItem.listKind = 'todo';
      this.$store.dispatch('updateList', checkedItem);
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
