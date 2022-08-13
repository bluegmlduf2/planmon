<template>
  <div class="search-bar">
    <div class="input-groupt">
      <button
        class="btn"
        @click="searchRecList"
      >
        <i
          class="fa fa-search"
          aria-hidden="true"
        />
      </button>
      <input
        v-model="searchRecWord"
        type="search"
        class="form-control"
        placeholder="추천 일정 검색"
        @keyup.enter="searchRecList"
      >
    </div>
  </div>
</template>

<script>
import message from '@/assets/js/message';

export default {
  /**
   * The name of the component.
   */
  name: 'SearchRecList',
  data() {
    return {
      searchRecWord: '', // 추천일정검색 단어
    };
  },
  methods: {
    // 추천일정검색기능
    searchRecList() {
      // 검색어가 존재하지않고 추천일정화면이 아닌 경우
      if (this.searchRecWord !== '' && this.$route.path !== '/reclist') {
        // 추천일정 검색과 함께 추천페이지 이동
        this.$router.push({ name: 'reclist.index', params: { searchRecWord: this.searchRecWord } });
      } else if (this.$route.path === '/reclist') {
        // 만약 추천일정화면에서 재검색하는 경우 메세지 표시
        this.$toast.info(message.reSearch);
        this.searchRecWord = '';
      }
    },
  },
};
</script>
