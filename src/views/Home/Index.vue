<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4 add-padding-bottom"
    >
      <!-- 할일 일정 -->
      <v-list
        :param-list="todolist"
        :param-show-buttons="false"
        :param-is-add="true"
        @updateCheckInput="selectTodoCheckInput"
      >
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
          type="button"
          class="btn btn-light w-100"
          @click="$router.push({name: 'todolist.index'})"
        >
          +
        </button>
      </div>
      <hr>
      <!-- 추천 일정 -->
      <v-list
        :param-list="recommendedList"
        :param-show-buttons="false"
        :param-is-add="true"
        @updateCheckInput="selectRecCheckInput"
      >
        <span
          slot="header"
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
      <button
        v-if="this.$store.getters.user"
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

  data() {
    return {
      recommendedList: [], // 추천 일정 리스트
    };
  },
  computed: {
    // 선택된 할일리스트 (store에서 값이 변경될때마다 갱신)
    todolist() {
      return this.$store.getters.todolist;
    },
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
      {
        value: '5a',
        text: '다섯번째 추천일정',
      },
      {
        value: '6a',
        text: '여섯번째 추천일정',
      }];
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
