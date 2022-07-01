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
    // 게시글 이전 내용 지우기
    clearPost(state) {
      state.post = null;
    },
  },
  actions: {
    // 게시물 초기화
    setInitPost({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작
      commit('clearPost'); // 게시글의 이전 내용 지우기

      // 게시물 정보 취득
      return new PostProxy()
        .getPost(payload)
        .then((response) => {
          // 서버로부터 받은 값
          const responseData = response.data;
          // 유저 로그인 정보
          const isLogined = this.getters.user;

          // 미로그인 상태일시 유저의 로컬스토리지에서 해당 일정의 시작일 종료일이 있는지 검색
          if (!isLogined) {
            // 로컬스토리지의 나의 할일일정과 완료일정을 취득후, 해당 일정의 예정 시작일 예정 종료일을 취득
            const { myTodolist, myCompletelist } = this.getters.selection;
            const myList = [...myTodolist, ...myCompletelist].find((e) => e.postId === payload);

            // 추천 시작,종료일자
            const recommendedEndDate = new Date().setDate(new Date().getDate() + responseData.afterEntryDate); // 추천 게시글의 일정종료일과 비교해서 추천일정 선택
            responseData.myStartDate = myList?.myStartDate ?? new Date(); // 시작일자가 존재하지 않을 경우 추천 시작일자 입력
            responseData.myEndDate = myList?.myEndDate ?? recommendedEndDate; // 종료일자가 존재하지 않을 경우 추천 종료일자 입력
          }

          // 서버에서 가져온 게시글을 초기화
          commit('setPost', responseData);
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
