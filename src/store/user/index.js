import firebase from '@/plugins/firebase';

export default {
  state: {
    user: null,
  },
  mutations: {
    setUser(state, payload) {
      state.user = payload;
    },
  },
  actions: {
    // 이메일 로그인 및 회원등록
    signUserInEmailLink({ commit }, payload) {
      commit('setLoading', true);
      commit('clearError');
      firebase.sendSignInLinkToEmail(firebase.auth, payload.email, firebase.actionCodeSettings)
        .then(
          // 이메일 링크를 성공적으로 보냄
          () => {
            // 이메일 링크 인증전까지 임시로 메일정보를 입력(이메일 로그인 완료시 삭제됨)
            window.localStorage.setItem('emailForSignIn', payload.email);
            commit('setLoading', false);
          },
        )
        .catch(
          (error) => {
            const err = error;
            let message = '로그인에 실패하였습니다';
            switch (err.code) {
              case 'auth/invalid-email':
                message = '유효하지 않은 이메일입니다';
                break;
              case 'auth/wrong-password':
                message = '비밀번호가 일치하지 않습니다';
                break;
              case 'auth/invalid-credential':
                message = '유효하지 않은 접근입니다';
                break;
              default:
                break;
            }
            err.message = message;
            commit('setLoading', false);
            commit('setError', err);
          },
        );
    },
    // 구글 계정으로 로그인 및 회원등록
    signUserInGoogle({ commit }) {
      commit('setLoading', true);
      commit('clearError');
      firebase.signInWithPopup(firebase.auth, new firebase.GoogleAuthProvider())
        .then(
          (user) => {
            commit('setLoading', false);
            const newUser = {
              id: user.uid,
              name: user.displayName,
              email: user.email,
              photoUrl: user.photoURL,
            };
            commit('setUser', newUser);
          },
        )
        .catch(
          (error) => {
            commit('setLoading', false);
            commit('setError', error);
            console.log(error);
          },
        );
    },
    // 자동 로그인 상태
    autoSignIn({ commit }, payload) {
      commit('setUser', {
        id: payload.uid,
        name: payload.displayName,
        email: payload.email,
        photoUrl: payload.photoURL,
      });
    },
    // 로그아웃
    logout({ commit }) {
      firebase.signOut(firebase.auth);
      commit('setUser', null);
    },
  },
  getters: {
    user(state) {
      return state.user;
    },
  },
};
