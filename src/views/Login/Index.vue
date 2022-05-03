<template>
  <div
    v-if="isLoginStatus"
    class="login-bg"
  >
    <div class="login-cont">
      <div class="text-right w-100 pr-1">
        <h5>
          <i
            class="fa fa-times"
            aria-hidden="true"
            @click="closeLogin()"
          />
        </h5>
      </div>
      <div class="login-title mt-4 mb-2">
        <h2>{{ isSignup ? "회원등록":"로그인" }}</h2>
        <p>이메일로 {{ isSignup ? "회원등록":"로그인" }}합니다</p>
      </div>
      <!-- 이메일 입력 -->
      <div
        class="form-group"
        :disabled="loading"
      >
        <input
          id="loginEmailInput"
          v-model="email"
          type="email"
          placeholder="이메일을 입력해주세요"
          class="form-control"
          :class="{ 'is-invalid': false }"
        >
        <div
          class="invalid-feedback"
          for="loginEmailInput"
        >
          입력하신 이메일을 확인해주세요
        </div>
      </div>
      <!-- 로그인/회원등록 버튼 -->
      <button
        type="button"
        class="btn btn-primary w-100"
        :disabled="loading"
        @click="onSigninEmailLink"
      >
        <span
          v-if="loading"
          class="spinner-border spinner-border-sm"
          role="status"
          aria-hidden="true"
        />
        {{ loading?'인증중입니다':isSignup?'이메일로 회원등록':'이메일로 로그인' }}
      </button>
      <button
        type="button"
        class="btn btn-secondary w-100 mt-2"
        :disabled="loading"
        @click="onSigninGoogle"
      >
        <span
          v-if="loading"
          class="spinner-border spinner-border-sm"
          role="status"
          aria-hidden="true"
        />
        {{ loading?'인증중입니다':isSignup?'구글계정으로 회원등록':'구글계정으로 로그인' }}
      </button>
      <div class="login-footer">
        <span>{{ isSignup ? "로그인화면은":"아직 회원이 아니신분은" }}</span>
        <span
          class="clickable"
          @click="changeView()"
        > 여기를 클릭해주세요</span>
      </div>
    </div>
  </div>
</template>

<script>
import message from '@/assets/js/message';

export default {
  /**
   * The name of the component.
   */
  name: 'Login',

  /**
   * The properties that the component accepts.
   */
  props: {
    isLogin: {
      type: Boolean,
      required: true,
      default: false,
    },
  },

  data() {
    return {
      isSignup: false, // 회원등록 여부
      email: '',
      // deleteButtonActive: false, // 삭제상태 활성화
    };
  },
  // data와는 다른 함수형 변수
  computed: {
    // 로그인화면 열기 (props로 받아온 초기값 설정)
    isLoginStatus() {
      return this.isLogin;
    },
    // 유저정보 (store에서 값이 변경될때마다 갱신)
    user() {
      return this.$store.getters.user;
    },
    // 로딩바 (store에서 값이 변경될때마다 갱신)
    loading() {
      return this.$store.getters.loading;
    },
  },
  // 해당 computed들이 변하는가 감시, 변할때 작동
  watch: {
    user(value) {
      // computed의 user가 초기화때 한번 로그인때 한번 2번 실행되기때문에 isLoginStatus를 추가
      if (value !== null && value !== undefined && this.isLoginStatus) {
        this.closeLogin();
        this.$toast.info(message.welcome);
      }
    },
  },
  methods: {
    changeView() {
      this.email = '';
      this.isSignup = !this.isSignup;
    },
    // 로그인화면 닫기 (자식 컴포넌트에서 props를 변경하지 못해서 부모에게 변경요청)
    closeLogin() {
      this.email = '';
      this.isSignup = false;
      this.$emit('closeLogin');
    },
    // 로그인
    onSigninEmailLink() {
      this.$store.dispatch('signUserInEmailLink', { email: this.email });
    },
    // 구글 계정으로 로그인
    onSigninGoogle() {
      this.$store.dispatch('signUserInGoogle');
    },
  },
};
</script>
