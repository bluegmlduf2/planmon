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
    // 회원등록
    signUserUp({ commit }, payload) {
      commit('setLoading', true);
      commit('clearError');
      firebase.createUserWithEmailAndPassword(firebase.auth, payload.email, payload.password)
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
    // 로그인
    signUserIn({ commit }, payload) {
      commit('setLoading', true);
      commit('clearError');
      firebase.signInWithEmailAndPassword(firebase.auth, payload.email, payload.password)
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
    // 자동 로그인 상태
    autoSignIn({ commit }, payload) {
      commit('setUser', {
        id: payload.uid,
        name: payload.displayName,
        email: payload.email,
        photoUrl: payload.photoURL,
      });
    },
    // 비밀번호 재설정
    resetPasswordWithEmail({ commit }, payload) {
      const { email } = payload;
      commit('setLoading', true);
      firebase.sendPasswordResetEmail(firebase.auth, email)
        .then(
          () => {
            commit('setLoading', false);
            console.log('Email Sent');
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
