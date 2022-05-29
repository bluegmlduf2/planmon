<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 추천 일정 -->
      <v-list
        :param-list="reclist"
        :param-show-buttons="false"
        @updateCheckInput="selectRecCheckInput"
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
          추천 일정
        </span>
        <span slot="deleteList" />
      </v-list>
      <div
        class="list-footer"
      >
        <button
          v-if="reclistPage.hasNext"
          type="button"
          class="btn btn-light w-100"
          @click="$store.dispatch('getRecList')"
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
  name: 'ReclistIndex',

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
    reclist() {
      return this.$store.getters.reclist;
    },
    // 추천일정화면의 페이지네이션 정보
    reclistPage() {
      return this.$store.getters.reclistPage;
    },
  },
  created() {
    this.initRecommendedList(); // 추천 일정 초기화  (최대 5개 호출)
  },

  methods: {
    // 추천 일정 초기화 (기본적으로 10개를 가져오며 홈화면에서 더보기 버튼 클릭시만 20개를 가져온다)
    initRecommendedList() {
      this.$store.dispatch('setInitRecList', this.get20perpage);
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
