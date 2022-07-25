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
          :src="userImage"
        >
        <div
          class="btn btn-primary mb-2 uploadUserImage-cont"
        >
          프로필이미지 등록
          <input
            id="uploadUserImage"
            type="file"
            accept="image/jpeg"
            @clikc="updatePhotoUrl('register',$event)"
          >
        </div>
        <button
          type="button"
          class="btn btn-light mb-2"
          @click="updatePhotoUrl('delete')"
        >
          프로필이미지 삭제
        </button>
      </div>
      <div class="user-input-setting d-flex flex-column justify-content-start align-items-center p-1">
        <div class="form-group row mb-4">
          <label
            for="inputEmail3"
            class="col-3 col-form-label"
          >닉네임ㅤ
          </label>
          <div class="col-7">
            <input
              id="inputEmail3"
              v-model="displayName"
              placeholder="닉네임을 입력해주세요"
              type="text"
              class="form-control"
            >
          </div>
          <button
            type="button"
            class="btn btn-light col-2"
            @click="updateDisplayName"
          >
            변경
          </button>
        </div>
        <div class="w-100">
          <button
            type="button"
            class="btn btn-outline-danger w-100"
            @click="deleteUser"
          >
            회원탈퇴
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
import Confirm from '@/components/Confirm.vue';

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
      displayName: '',
    };
  },
  // data와는 다른 함수형 변수
  computed: {
    // 유저정보 (store에서 값이 변경될때마다 갱신)
    user() {
      return this.$store.getters.user;
    },
    // 로딩바 (store에서 값이 변경될때마다 갱신)
    loading() {
      return this.$store.getters.loading;
    },
    // 유저이미지 반환
    userImage() {
      // eslint-disable-next-line global-require
      return this.$store.getters.user.photoUrl ? this.$store.getters.user.photoUrl : require('@/assets/img/user.png');
    },
  },
  created() {
    this.initSetting();
  },
  methods: {
    initSetting() {
      this.displayName = this.user.name;
    },
    // 프로필정보 변경
    updateDisplayName() {
      const payload = { displayName: this.displayName };
      this.$store.dispatch('updateProfile', payload);
    },
    // 프로필사진 변경
    async updatePhotoUrl(args, e) {
      const payload = {};
      if (args === 'register') {
      // 유저 이미지 추가
      // 업로드한 이미지를 blol(이진수 형태의 큰 객체)형식으로 받은 뒤 formData에 넣은뒤 서버에 전송
        const formData = new FormData();
        formData.append('image', e.target.files[0]);
        const { imageUrl } = await this.$store.dispatch('uploadUserImage', formData); // 이미지 업로드
        payload.photoURL = imageUrl;
        // 성공적으로 유저이미지를 등록한 경우 갱신
        if (imageUrl) {
          this.$store.dispatch('updateProfile', payload);
        }
      } else if (args === 'delete') {
      // 유저 이미지 삭제
        payload.photoURL = '';
        this.$store.dispatch('updateProfile', payload);
      }
    },
    // 유저삭제
    deleteUser() {
      this.$toast.info({
        component: Confirm,
        props: {
          buttonName: '삭제',
        },
        listeners: {
          confirmEvent: () => {
            this.$store.dispatch('deleteUser');
          },
        },
      }, { timeout: 7000 });
    },
  },

};
</script>
