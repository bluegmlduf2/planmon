// 선택 정보의 초기값
const selectionInit = {
  country: null,
  stayStatus: null,
  entryDate: null,
  todolist: [],
  completelist: [],
};

export default {
  state: {
    selection: selectionInit,
  },
  mutations: {
    setSelection(state, payload) {
      state.selection = payload;
    },
    clearSelection(state) {
      state.selection = selectionInit;
    },
  },
  actions: {
    // 선택값 데이터 초기화
    setInitSelection({ commit }) {
      let selection;
      const isLogined = this.getters.user;
      // 로그인상태일시
      if (isLogined) {
        // TODO axios로 selection 가져옴
        selection = {
          country: 'JP',
          stayStatus: '2',
          entryDate: '2022-05-10',
          todolist: [1, 2, 3, 4, 5],
          completelist: [1],
        };
      } else {
      // 미로그인시
        const selectionStorage = window.localStorage.getItem('selection');
        // 기존의 로컬스토리지가 없다면 추가한다
        if (!selectionStorage) {
          window.localStorage.setItem('selection', JSON.stringify(selectionInit));
        }
        selection = JSON.parse(window.localStorage.getItem('selection'));
      }
      commit('setSelection', selection);
    },
    // 선택한 항목을 저장
    addSelection({ commit }, payload) {
      const selection = { ...this.getters.selection, ...payload }; // 선택한 항목
      let insertSelection; // 입력할 항목

      const isLogined = this.getters.user;
      // 로그인상태일시
      if (isLogined) {
        // TODO axios로 selection 가져옴
        insertSelection = selection;
      } else {
        // 미로그인시
        window.localStorage.setItem('selection', JSON.stringify(selection));
        insertSelection = selection;
      }
      commit('setSelection', insertSelection);
    },
    clearSelection({ commit }) {
      commit('clearSelection');
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
          selection.todolist = [...selection.todolist.filter((e) => e.postId !== checkedItem.postId), checkedItem];
        } else if (listKind === 'todo' || listKind === 'all') {
          // 할일일정, 모든일정의 추천일정 선택시 완료일정에 추가
          // 중복된 일정이 아니라면 완료 일정에 추가
          selection.completelist = [...selection.completelist.filter((e) => e.postId !== checkedItem.postId), checkedItem];
          // 할일 일정에서 삭제
          selection.todolist = [...selection.todolist.filter((e) => e.postId !== checkedItem.postId)];
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
          selection.todolist = [...selection.todolist.filter((e) => e.postId !== checkedItem.postId)];
        } else if (listKind === 'complete') {
          // 완료일정 선택시 일정삭제
          selection.completelist = [...selection.completelist.filter((e) => e.postId !== checkedItem.postId)];
        }
        window.localStorage.setItem('selection', JSON.stringify(selection));
      }
      commit('setSelection', selection);
    },
  },
  getters: {
    selection(state) {
      return state.selection;
    },
  },
};
