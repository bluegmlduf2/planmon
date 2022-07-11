import Vue from 'vue';
import message from '@/assets/js/message';
import CommentProxy from '@/proxies/CommentProxy';

export default {
  state: {
    comments: [],
  },
  mutations: {
    // 댓글 초기화
    setComment(state, payload) {
      state.comments = payload;
    },
    // 댓글 이전 내용 지우기
    clearComment(state) {
      state.comments = [];
    },
  },
  actions: {
    // 댓글 초기화
    setInitComment({ commit }) {
      commit('setSpinner', true); // 스피너 동작
      commit('clearComment'); // 댓글의 이전 내용 지우기
      const { postId } = this.getters.post; // 게시물 ID

      // 게시물 정보 취득
      return new CommentProxy()
        .getComment(postId)
        .then((response) => {
          // 서버에서 가져온 댓글을 초기화
          commit('setComment', response.data);
        })
        .catch(() => {
          console.log('Request failed...');
        });
    },
    // 댓글 등록
    createComment({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작
      const { postId } = this.getters.post; // 게시물 ID
      const param = { postId, ...payload }; // 게시물 ID와 입력 댓글내용을 포함

      // 댓글 정보 등록
      return new CommentProxy()
        .createComment(param)
        .then(async () => {
          // 댓글을 초기화
          await this.dispatch('setInitComment');
          Vue.prototype.$toast.info(message.addComment);
        })
        .catch(() => {
          console.log('Request failed...');
        })
        .finally(() => {
          commit('setSpinner', false); // 스피너 정지
        });
    },

    // 댓글 수정
    updateComment({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작

      // 댓글 정보 수정
      return new CommentProxy()
        .updateComment(payload)
        .then(async () => {
          // 댓글을 초기화
          await this.dispatch('setInitComment');
          Vue.prototype.$toast.info(message.updateComment);
        })
        .catch(() => {
          console.log('Request failed...');
        })
        .finally(() => {
          commit('setSpinner', false); // 스피너 정지
        });
    },

    // 댓글 삭제
    destroyComment({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작
      const { postId } = this.getters.post; // 게시물 ID
      const param = { postId, ...payload }; // 게시물 ID와 입력 댓글내용을 포함

      // 댓글 정보 삭제
      return new CommentProxy()
        .destroyComment(param)
        .then(async () => {
          // 댓글을 초기화
          await this.dispatch('setInitComment');
          Vue.prototype.$toast.info(message.removeComment);
        })
        .catch(() => {
          console.log('Request failed...');
        })
        .finally(() => {
          commit('setSpinner', false); // 스피너 정지
        });
    },
  },
  getters: {
    // 댓글정보
    comments(state) {
      return state.comments;
    },
  },
};
