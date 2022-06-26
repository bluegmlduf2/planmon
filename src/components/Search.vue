<template>
  <div>
    <h4 class="list-search">
      검색
    </h4>
    <div class="input-groupt">
      <button
        class="btn"
        @click="searchList"
      >
        <i
          aria-hidden="true"
          class="fa fa-search"
        />
      </button>
      <input
        v-model="searchWord"
        type="search"
        placeholder="결과 재검색"
        class="form-control"
      >
    </div>
  </div>
</template>

<script>
export default {
  /**
   * The name of the component.
   */
  name: 'Search',
  data() {
    return {
      searchWord: '', // 결과 재검색한 단어
    };
  },
  watch: {
    searchWord(newVal) {
      // 결과내 재검색을 x버튼으로 clear 하거나 검색결과를 공란으로 한 경우
      if (newVal === '') {
        // 부모의 메서드 호출
        this.$emit('searchList', this.searchWord);
      }
    },
  },
  methods: {
    // 결과내 재검색 기능
    searchList() {
      // 부모의 메서드 호출
      this.$emit('searchList', this.searchWord);
    },
  },
};
</script>
