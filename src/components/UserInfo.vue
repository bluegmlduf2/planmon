<template>
  <div class="d-flex justify-content-between align-items-center mb-2">
    <div class="d-flex align-items-center">
      <img
        class="profile-img"
        src="https://placeimg.com/640/480/any"
      >
      <div class="d-flex flex-column align-items-start ml-2">
        <p><b>사용자명</b></p>
        <p class="font-light-color">
          2022년 12월 19일
        </p>
      </div>
    </div>
    <div>
      <div
        v-if="paramShowButtons"
        class="post-update-buttons font-light-color"
      >
        <span class="mr-2">
          수정
        </span>
        <span>
          삭제
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  /**
   * The name of the component.
   */
  name: 'UserInfo',
  /**
   * The properties that the component accepts.
   */
  props: {
    // 로그인 상태에 따른 수정,삭제버튼의 표시여부
    paramShowButtons: {
      default: true,
      type: Boolean,
      required: true,
    },
  },
};
</script>
