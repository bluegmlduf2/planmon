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
        insertSelection = JSON.parse(window.localStorage.getItem('selection'));
      }
      commit('setSelection', insertSelection);
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
