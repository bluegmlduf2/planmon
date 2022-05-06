<template>
  <div class="container">
    <span
      v-if="confirmMessage"
      class="mr-3 confirm-message"
    >{{ confirmMessage }}<br><br></span>
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
      v-if="!confirmMessage"
      class="mr-3"
    >?{{ buttonName }}하시겠습니까</span>
  </div>
</template>

<script>
export default {
  props: {
    // 확인 버튼명
    buttonName: {
      type: String,
      required: true,
    },
    // 사용자 지정 확인메세지
    confirmMessage: {
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
