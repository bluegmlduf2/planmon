<template>
  <div
    v-if="spinner"
    class="loader-background"
  >
    <div class="regot-loader">
      <div class="regot regot1" />
      <div class="regot regot2" />
      <div class="regot regot3" />
      <div class="regot regot4" />
    </div>
  </div>
</template>

<script>
export default {
  /**
   * The name of the component.
   */
  name: 'Spinner',
  computed: {
    // 요청대기 스피너 초기값반환
    spinner() {
      return this.$store.getters.spinner;
    },
  },
};
</script>
