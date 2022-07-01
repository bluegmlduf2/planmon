import PostProxy from '@/proxies/PostProxy';

export default {
  state: {
    post: null,
  },
  mutations: {
    // 게시글 초기화
    setPost(state, payload) {
      state.post = payload;
    },
  },
  actions: {
    // 게시물 초기화
    setInitPost({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작

      // 게시물 정보 취득
      return new PostProxy()
        .getPost(payload)
        .then((response) => {
          // 서버에서 가져온 게시글을 초기화
          commit('setPost', response.data);
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
    // 게시글정보
    post(state) {
      return state.post;
    },
  },
};
