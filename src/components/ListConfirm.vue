<template>
  <div class="container">
    <button
      class="toast-button"
      @click="cancelClicked"
    >
      취소
    </button>
    <button
      class="toast-button mr-3"
      @click="clicked"
    >
      삭제
    </button>
    <span class="mr-3">?삭제하시겠습니까 </span>
  </div>
</template>

<script>
export default {
  methods: {
    clicked() {
      this.$emit('confirmEvent');
    },
    cancelClicked() {
      this.$emit('cancelEvent');
    },
  },
};
</script>
