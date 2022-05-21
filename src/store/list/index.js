import Vue from 'vue';
import message from '@/assets/js/message';
import TodoListProxy from '@/proxies/TodoListProxy';
import RecListProxy from '@/proxies/RecListProxy';
import { router } from '@/plugins/vue-router';

export default {
  state: {
    // todolist: [{ postId: '1', title: '타이틀1' }, { postId: '2', title: '타이틀2' }], // 표시용 리스트
    // completelist: [{ postId: '3', title: '타이틀3' }, { postId: '4', title: '타이틀4' }], // 표시용 리스트
    todolist: [], // 할일 일정 (표시용)
    reclist: [], // 추천 일정 (표시용)
    completelist: [], // 완료 일정 (표시용)
  },
  mutations: {
    setTodoList(state, payload) {
      state.todolist = payload;
    },
    setRecList(state, payload) {
      state.reclist = payload;
    },
    setCompleteList(state, payload) {
      state.completelist = payload;
    },
  },
  actions: {
    // 홈화면에서 할일일정과 추천일정을 초기화
    setInitHomeList() {
      // 할일일정화면과 추천일정화면에서 2번 호출되는걸 막기 위한 처리
      if (router.currentRoute.path === '/') {
        // 홈화면의 할일일정 초기화 (표시용)
        this.dispatch('setInitTodoList');
        // 홈화면의 추천일정 초기화 (표시용)
        this.dispatch('setInitRecList');
      }
    },
    // 할일일정 초기화
    setInitTodoList({ commit }) {
      const isLogined = this.getters.user; // 로그인 유무
      // 할일일정 추가
      // 로그인 유무에 따라 사용하는 메서드가 다르다
      if (isLogined) {
        // 로그인 시
        // 나의 할일일정 초기화 (파이어베이스 토큰으로 검색)
        // TODO 나중에 완료 목록갯수까지해서 promiseall로 구현하기
        // TODO 로그아웃후 기존 로컬스토리지 내용이 적용이 안됨
        new TodoListProxy()
          .getMyTodoList()
          .then((response) => {
            commit('setTodoList', response.data);
          })
          .catch(() => {
            console.log('Request failed...');
          });
      } else {
        // 미로그인시
        const { selection } = this.getters;
        // 로컬스토리지의 정보로 초기화
        new TodoListProxy()
          .getTodoList(selection)
          .then((response) => {
            commit('setTodoList', response.data);
          })
          .catch(() => {
            console.log('Request failed...');
          });
      }
    },
    // 추천일정 초기화
    setInitRecList({ commit }) {
      // 추천일정 추가
      const { selection } = this.getters;
      // 로컬스토리지의 정보로 초기화
      new RecListProxy()
        .getRecList(selection)
        .then((response) => {
          commit('setRecList', response.data);
        })
        .catch(() => {
          console.log('Request failed...');
        });
    },
    // 선택한 리스트를 추가, 삭제
    updateList(_, payload) {
      const checkedItem = payload;

      if (checkedItem.isAdded) {
        // 추가모드
        this.dispatch('addList', checkedItem);
      } else {
        // 삭제모드
        this.dispatch('removeList', checkedItem);
      }
    },
    // 일정 추가
    addList({ commit }, payload) {
      const { selection } = this.getters;
      const { listKind } = payload; // 클릭한 리스트 종류
      const isLogined = this.getters.user; // 로그인 유무
      const checkedItem = { postId: payload.postId }; // 입력값

      // 로그인상태일시
      if (isLogined) {
        // TODO axios 리스트별 추가 삭제 찰;
      } else {
        // 미로그인시
        if (listKind === 'rec') {
          // 추천일정 할일 일정에 추가
          // 중복된 일정이 아니라면 할일 일정에 추가
          selection.myTodolist = [...selection.myTodolist.filter((e) => e.postId !== checkedItem.postId), checkedItem];
          Vue.prototype.$toast.info(message.addList);
        } else if (listKind === 'todo' || listKind === 'all') {
          // 할일일정, 모든일정의 추천일정 선택시 완료일정에 추가
          // 중복된 일정이 아니라면 완료 일정에 추가
          selection.myCompletelist = [...selection.myCompletelist.filter((e) => e.postId !== checkedItem.postId), checkedItem];
          // 할일 일정에서 삭제
          selection.myTodolist = [...selection.myTodolist.filter((e) => e.postId !== checkedItem.postId)];
          // 할일 일정 초기화 (표시용)
          this.dispatch('setInitTodoList');
          Vue.prototype.$toast.info(message.completeList);
        }
        window.localStorage.setItem('selection', JSON.stringify(selection));
      }
      commit('setSelection', selection);
    },
    // 일정 삭제
    removeList({ commit }, payload) {
      const { selection } = this.getters;
      const { listKind } = payload; // 클릭한 리스트 종류
      const isLogined = this.getters.user; // 로그인 유무
      const checkedItem = { postId: payload.postId }; // 입력값

      // 로그인상태일시
      if (isLogined) {
        // TODO axios 리스트별 추가 삭제 찰;
      } else {
        // 미로그인시
        if (listKind === 'todo' || listKind === 'all') {
          // 할일 일정, 모든일정의 할일일정 선택시 일정삭제
          selection.myTodolist = [...selection.myTodolist.filter((e) => e.postId !== checkedItem.postId)];
          // 할일 일정 초기화 (표시용)
          this.dispatch('setInitTodoList');
        } else if (listKind === 'complete') {
          // 완료일정 선택시 일정삭제
          selection.myCompletelist = [...selection.myCompletelist.filter((e) => e.postId !== checkedItem.postId)];
        }
        window.localStorage.setItem('selection', JSON.stringify(selection));
      }
      Vue.prototype.$toast.info(message.removeList);
      commit('setSelection', selection);
    },
  },
  getters: {
    todolist(state) {
      return state.todolist;
    },
    reclist(state) {
      return state.reclist;
    },
    completelist(state) {
      return state.completelist;
    },
  },
};
