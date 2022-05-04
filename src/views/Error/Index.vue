<template>
  <div class="container-fluid">
    <div
      class="d-flex justify-content-center align-items-center flex-column"
      style="min-height:100vh;"
    >
      <div class="h1 mb-4">
        페이지를 찾을 수 없습니다
      </div>
      <div class="h5 mb-3 text-center text-secondary font-weight-light">
        입력한 주소가 잘못되었거나, 사용이 일시 중단되어 요청하신 페이지를 찾을 수 없습니다<br>서비스 이용에 불편을 드려 죄송합니다
      </div>
      <div class="h5 font-weight-normal">
        <router-link
          :to="{ name: 'home.index' }"
          style="color:rgb(0,191,255);"
        >
          <span>여기</span>
        </router-link>를 클릭해서 홈화면으로 이동해주세요
      </div>
    </div>
  </div>
</template>

<script>
/* ============
 * Error Index Page
 * ============
 *
 * The Error index page.
 */

export default {
  /**
   * The name of the page.
   */
  name: 'ErrorIndex',
};
</script>
