import Vue from 'vue';
import firebase from '@/plugins/firebase';
import firebaseError from '@/assets/js/firebaseError';
import message from '@/assets/js/message';
import { router } from '@/plugins/vue-router';

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
            Vue.prototype.$toast.info(message.sendEmail, {
              timeout: 4000,
            });
            // 이메일 링크 인증전까지 임시로 메일정보를 입력(이메일 로그인 완료시 삭제됨)
            window.localStorage.setItem('emailForSignIn', payload.email);
          },
        )
        .catch(
          (error) => {
            Vue.prototype.$toast.error(firebaseError(error));
          },
        ).finally(() => {
          commit('setLoading', false);
        });
    },
    // 구글 계정으로 로그인 및 회원등록
    signUserInGoogle({ commit }) {
      commit('setLoading', true);
      commit('clearError');
      firebase.signInWithPopup(firebase.auth, new firebase.GoogleAuthProvider())
        .then(
          (result) => {
            const { user } = result;
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
            Vue.prototype.$toast.error(firebaseError(error));
          },
        ).finally(() => {
          commit('setLoading', false);
        });
    },
    // 이메일 링크 인증
    signInWithEmailLink() {
      // 로그인 이메일링크가 인증되었는지 확인, 인증되었다면 true
      if (firebase.isSignInWithEmailLink(firebase.auth, window.location.href)) {
        // 인증메일을 보낸 기기와 로그인 기기가 다른지 확인
        const email = window.localStorage.getItem('emailForSignIn');
        if (email) {
          // 인증이 완료되면 로그인 유저정보 취득
          firebase.signInWithEmailLink(firebase.auth, email, window.location.href)
            .then(() => {
              // 임시적으로 저장해뒀던 로그인 이메일 삭제
              window.localStorage.removeItem('emailForSignIn');
              Vue.prototype.$toast.info(message.welcome);
            })
            .catch((error) => {
              // 처음에 렌더링이 2회 실행되면서 아래의 에러가 발생한다.
              // 해당 에러는 묵시적으로 제외하고 그외의 에러가 발생시 경고메세지로 표시
              if (error.code !== 'auth/invalid-action-code') {
                Vue.prototype.$toast.error(firebaseError(error));
              }
            });
        }
      }
    },
    // 사용자 프로필 업데이트
    updateProfile({ commit }, payload) {
      commit('setLoading', true);
      commit('clearError');
      // 사용자 프로필 업데이트
      const { currentUser } = firebase.auth;
      firebase.updateProfile(currentUser, payload).then(() => {
        Vue.prototype.$toast.info(message.changeUserInfo);
        commit('setUser', {
          name: payload.displayName ? payload.displayName : currentUser.displayName,
          photoUrl: payload.photoURL ? payload.photoURL : currentUser.photoURL,
        });
      }).catch((error) => {
        Vue.prototype.$toast.error(firebaseError(error));
      }).finally(() => {
        commit('setLoading', false);
      });
    },
    // 유저 삭제
    deleteUser({ commit }) {
      commit('setLoading', true);
      commit('clearError');
      // 유저 삭제
      firebase.deleteUser(firebase.auth.currentUser).then(() => {
        Vue.prototype.$toast.info(message.deleteUser);
        commit('setUser', null);
        router.push({ name: 'home.index' });
      }).catch((error) => {
        Vue.prototype.$toast.error(firebaseError(error));
      }).finally(() => {
        commit('setLoading', false);
      });
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
