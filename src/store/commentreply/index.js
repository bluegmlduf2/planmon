import Vue from 'vue';
import message from '@/assets/js/message';
import CommentReplyProxy from '@/proxies/CommentReplyProxy';

export default {
  actions: {
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
};
