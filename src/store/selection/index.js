// 선택 정보의 초기값
const selectionInit = {
  country: '',
  stayStatus: '',
  entryDate: '',
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
        if (!selectionStorage) {
          window.localStorage.setItem('selection', JSON.stringify({
            country: 'CN',
            stayStatus: '1',
            entryDate: '2022-05-20',
            todolist: [1, 2, 3],
            completelist: [1, 2],
          }));
        }
        selection = JSON.parse(window.localStorage.getItem('selection'));
      }
      commit('setSelection', selection);
    },
    // 선택한 항목을 저장
    addSelection({ commit }, payload) {
      const selection = { ...this.getters.selection, ...payload };
      commit('setSelection', selection);
    },
    clearSelection({ commit }) {
      commit('clearSelection');
    },
  },
  getters: {
    selection(state) {
      return state.selection;
    },
  },
};
