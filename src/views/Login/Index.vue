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

      <div class="form-group">
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
      <div class="form-group">
        <input
          id="loginPassWordInput"
          v-model="password"
          type="password"
          placeholder="비밀번호를 입력해주세요"
          autocomplete="current-password"
          class="form-control"
          :class="{ 'is-invalid': false }"
        >
        <div
          class="invalid-feedback"
          for="loginPassWordInput"
        >
          입력하신 비밀번호를 확인해주세요
        </div>
      </div>
      <div
        v-if="isSignup"
        class="form-group"
      >
        <input
          id="loginPassWordReInput"
          type="password"
          placeholder="비밀번호를 재입력해주세요"
          autocomplete="current-password"
          class="form-control"
          :class="{ 'is-invalid': false }"
        >
        <div
          class="invalid-feedback"
          for="loginPassWordReInput"
        >
          입력하신 비밀번호를 확인해주세요
        </div>
      </div>
      <div
        v-if="isSignup"
        class="input-group mb-3"
      >
        <input
          id="emailValidInput"
          type="text"
          class="form-control"
          :class="{ 'is-invalid': false }"
          placeholder="이메일로 전송된 인증번호를 입력해주세요"
          aria-label="emailValidButton"
          aria-describedby="emailValidButton"
        >
        <div class="input-group-append">
          <button
            id="emailValidButton"
            class="btn btn-outline-secondary btn-sm"
            type="button"
          >
            {{ isMailed?"인증":"전송" }}
          </button>
        </div>
        <div
          class="invalid-feedback"
          for="emailValidInput"
        >
          입력하신 인증번호를 확인해주세요
        </div>
      </div>

      <button
        v-if="isSignup"
        type="button"
        class="btn btn-primary w-100"
      >
        회원등록
      </button>
      <button
        v-else
        type="button"
        class="btn btn-primary w-100"
        :disabled="loading"
        @click="onSignin"
      >
        <span
          v-if="loading"
          class="spinner-border spinner-border-sm"
          role="status"
          aria-hidden="true"
        />
        {{ loading?'Loading...':'로그인' }}
      </button>
      <div
        v-if="!isSignup"
        class="login-footer login-footer-top"
      >
        <span
          class="clickable"
          @click="changeView()"
        > 비밀번호를 잊으셨나요?</span>
      </div>
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
      isMailed: false, // 확인메일전송 여부
      email: '',
      password: '',
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
    // 유저정보 (store에서 값이 변경될때마다 갱신)
    error() {
      return this.$store.getters.error;
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
        this.$toast.info('플랜몬에 오신것을 환영합니다', {
          timeout: 2500,
          hideProgressBar: true,
          showCloseButtonOnHover: true,
        });
      }
    },
    error(value) {
      if (value !== null && value !== undefined) {
        this.$toast.error(value.message);
        this.onDismissed();
      }
    },
  },
  methods: {
    changeView() {
      this.isMailed = false;
      this.isSignup = !this.isSignup;
    },
    // 로그인화면 닫기 (자식 컴포넌트에서 props를 변경하지 못해서 부모에게 변경요청)
    closeLogin() {
      this.email = '';
      this.password = '';
      this.isSignup = false;
      this.isMailed = false;
      this.$emit('closeLogin');
    },
    // 로그인
    onSignin() {
      this.$store.dispatch('signUserIn', { email: this.email, password: this.password });
    },
    // 비밀번호초기화
    // eslint-disable-next-line consistent-return
    onResetPassword() {
      if (this.email === '') {
        return this.$store.dispatch('setError', { message: 'Email can not be blank' });
      }
      this.$store.dispatch('resetPasswordWithEmail', { email: this.email });
    },
    onDismissed() {
      this.$store.dispatch('clearError');
    },
  },
};
</script>
