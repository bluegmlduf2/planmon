<template>
  <v-layout :is-left-menu-active="true">
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <div class="d-block d-sm-block d-md-none d-lg-none d-xl-none w-100">
        <div class="row mb-4 d-flex align-items-start justify-content-start ml-1">
          <div class="post-back ml-3">
            <span @click="$router.push({name: 'home.index'})">
              <i
                class="fa fa-chevron-left"
                aria-hidden="true"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="user-image-setting d-flex flex-column justify-content-center align-items-center mb-4">
        <img
          class="profile-img mb-3"
          src="https://placeimg.com/640/480/any"
        >
        <button
          type="button"
          class="btn btn-primary mb-2 w-100"
        >
          프로필이미지 등록
        </button>
        <button
          type="button"
          class="btn btn-light mb-2 w-100"
        >
          프로필이미지 삭제
        </button>
      </div>
      <div class="user-input-setting d-flex flex-column justify-content-start align-items-start mb-4">
        <div class="form-group row">
          <label
            for="inputEmail3"
            class="col-4 col-form-label"
          >닉네임ㅤ
          </label>
          <div class="col-6">
            <input
              id="inputEmail3"
              type="text"
              class="form-control"
            >
          </div>
          <button
            type="button"
            class="btn btn-light col-2"
          >
            변경
          </button>
        </div>
        <div class="form-group row">
          <label
            for="inputEmail3"
            class="col-4 col-form-label"
          >비밀번호
          </label>
          <div class="col-6">
            <input
              id="inputEmail3"
              type="password"
              class="form-control"
            >
          </div>
          <button
            type="button"
            class="btn btn-light col-2"
          >
            변경
          </button>
        </div>
        <div class="row">
          <label
            class="col-4 col-form-label lb-08"
          >새비밀번호ㅤ입력
          </label>
          <div class="col-6 mb-3">
            <input
              id=""
              type="password"
              class="form-control"
            >
          </div>
        </div>
        <div class="row mb-2">
          <label
            class="col-4 col-form-label lb-08"
          >새비밀번호 재입력
          </label>
          <div class="col-6 mb-3">
            <input
              id=""
              type="password"
              class="form-control"
            >
          </div>
        </div>
        <div class="d-flex justify-content-between align-items-center w-100">
          <span>
            탈퇴처리
          </span>
          <button
            type="button"
            class="btn btn-outline-danger"
          >
            탈퇴
          </button>
        </div>
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

export default {
  /**
   * The name of the page.
   */
  name: 'SettingIndex',

  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
  },

  data() {
    return {
    };
  },
  created() {
  },

  methods: {
  },

};
</script>
