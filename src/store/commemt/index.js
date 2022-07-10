export default {
  state: {
    comments: null,
  },
  mutations: {
    // 댓글 초기화
    setComment(state, payload) {
      // 댓글 초기화시 미클릭 정보 추가
      state.comments = payload.map((e) => ({ ...e, isClicked: false, isWriteClicked: false }));
    },
    // 댓글 이전 내용 지우기
    clearComment(state) {
      state.comments = null;
    },
  },
  actions: {
    // 댓글 초기화
    setInitComment() {
    },
  },
  getters: {
    // 댓글정보
    comments(state) {
      return state.comments;
    },
  },
};
