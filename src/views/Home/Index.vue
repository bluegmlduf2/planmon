<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4 add-padding-bottom"
    >
      <!-- 다가오는 일정 -->
      <v-list :param-list="todoList">
        <span
          slot="header"
          @click="$router.push({name: 'todolist.index'})"
        >
          다가오는 일정
        </span>
      </v-list>
      <div
        class="list-footer"
      >
        <button
          type="button"
          class="btn btn-light w-100"
          @click="$router.push({name: 'todolist.index'})"
        >
          +
        </button>
      </div>
      <hr>
      <!-- 추천 일정 -->
      <v-list :param-list="recommendedList">
        <span
          slot="header"
          @click="$router.push({name: 'reclist.index'})"
        >
          추천 일정
        </span>
      </v-list>
      <div
        class="list-footer"
      >
        <button
          type="button"
          class="btn btn-light w-100"
          @click="$router.push({name: 'reclist.index'})"
        >
          +
        </button>
      </div>
      <button class="btn btn-purple add-task">
        글쓰기
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

  data() {
    return {
      todoList: [], // 다가오는 일정 리스트
      recommendedList: [], // 추천 일정 리스트
    };
  },
  created() {
    this.initTodoList(); // 다가오는 일정 초기화 (최대 5개 호출)
    this.initRecommendedList(); // 추천 일정 초기화  (최대 5개 호출)
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
      ];
    },
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
      ];
    },
  },

};
</script>
