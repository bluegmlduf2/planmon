import Vue from 'vue';
import message from '@/assets/js/message';
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
    // 나의 일정 시작일 초기화
    setMyStartDate(state, payload) {
      state.post.myStartDate = payload;
    },
    // 나의 일정 종료일 초기화
    setMyEndDate(state, payload) {
      state.post.myEndDate = payload;
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
            const myCompleteList = [...myCompletelist].find((e) => e.postId === payload);

            responseData.myStartDate = myList?.myStartDate; // 추천 시작일자
            responseData.myEndDate = myList?.myEndDate; // 추천 종료일자
            responseData.isAdded = !!myList; // 추가한 게시물의 유무
            responseData.isCompleted = !!myCompleteList; // 완료한 게시물의 유무
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
    // 게시물의 일정변경
    updatePostCalendar({ commit }, payload) {
      const { postId } = this.getters.post; // 게시물 ID
      const isLogined = this.getters.user; // 로그인 유무
      const param = { postId, ...payload }; //

      // 로그인 상태일시
      if (isLogined) {
        // 추천일정 추가
        new PostProxy()
          .updatePostCalendar(param)
          .then((response) => {
            // 변경한 일정시작일과 일자종료일을 등록
            commit('setMyStartDate', response.data.myStartDate);
            commit('setMyEndDate', response.data.myEndDate);

            Vue.prototype.$toast.info(message.changePostDate);
          })
          .catch(() => {
            console.log('Request failed...');
          });
      }
      // else {

      // }
    },
  },
  getters: {
    // 게시글정보
    post(state) {
      return state.post;
    },
  },
};
