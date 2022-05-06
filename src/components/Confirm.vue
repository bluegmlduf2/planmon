<template>
  <div class="container">
    <button
      v-if="isShowButtons"
      class="toast-button"
      @click="cancelClicked"
    >
      취소
    </button>
    <button
      class="toast-button mr-3"
      @click="clicked"
    >
      {{ buttonName }}
    </button>
    <span
      v-if="message"
      class="mr-3"
    >?{{ message }} </span>
    <span
      v-else
      class="mr-3"
    >?{{ buttonName }}하시겠습니까 </span>
  </div>
</template>

<script>
export default {
  props: {
    // 버튼 두개 표시 여부
    buttonName: {
      type: String,
      required: true,
    },
    // 버튼 두개 표시 여부
    message: {
      default: '',
      type: String,
    },
    // 버튼 두개 표시 여부
    isShowButtons: {
      default: false,
      type: Boolean,
    },
  },
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
