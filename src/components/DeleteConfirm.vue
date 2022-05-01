<template>
  <div class="container">
    <button
      class="toast-button"
      @click="clicked"
    >
      삭제
    </button>
    <span class="mr-4">?삭제하시겠습니까 </span>
  </div>
</template>

<script>
export default {
  methods: {
    clicked() {
      this.$emit('confirmEvent');
    },
  },
};
</script>
