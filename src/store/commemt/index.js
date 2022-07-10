import Vue from 'vue';
import message from '@/assets/js/message';
import CommentProxy from '@/proxies/CommentProxy';
import CommentReplyProxy from '@/proxies/CommentReplyProxy';

export default {
  state: {
    comments: [],
  },
  mutations: {
    // 댓글 초기화
    setComment(state, payload) {
      // 댓글 초기화시 미클릭 정보 추가
      state.comments = payload.map((e) => ({ ...e, isClicked: false, isWriteClicked: false }));
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
    // 대댓글 등록
    createCommentReply({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작

      // 대댓글 정보 등록
      return new CommentReplyProxy()
        .createCommentReply(payload)
        .then(async () => {
          // 대댓글을 초기화
          await this.dispatch('setInitComment');
          Vue.prototype.$toast.info(message.addCommentReply);
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
