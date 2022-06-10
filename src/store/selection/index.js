import SelectionProxy from '@/proxies/SelectionProxy';

// 선택 정보의 초기값
const selectionInit = {
  country: null,
  stayStatus: null,
  entryDate: null,
  isShowMessage: true,
  myTodolist: [], // 로컬스토리지 보관을 위헤 위해 postId키만 보관
  myCompletelist: [], // 로컬스토리지 보관을 위헤 postId키만 보관
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
    // 사용자 선택값 데이터 초기화
    // eslint-disable-next-line consistent-return
    setInitSelection({ commit }) {
      const isLogined = this.getters.user;
      // 로그인상태일시
      if (isLogined) {
        return new SelectionProxy()
          .getSelection()
          .then((response) => {
            debugger;
            const selection = response.data;
            // 각 일정의 수를 초기화후 삭제
            commit('setTodoListCount', selection.todolistCount);
            commit('setCompleteListCount', selection.completelistCount);
            delete selection.todolistCount;
            delete selection.completelistCount;
            // 사용자 선택사항 초기화
            commit('setSelection', selection);
          })
          .catch(() => {
            console.log('Request failed...');
          });
      // eslint-disable-next-line no-else-return
      } else {
      // 미로그인시
        const selectionStorage = window.localStorage.getItem('selection');
        // 기존의 로컬스토리지가 없다면 추가한다
        if (!selectionStorage) {
          window.localStorage.setItem('selection', JSON.stringify(selectionInit));
        }
        const selection = JSON.parse(window.localStorage.getItem('selection'));
        // 각 일정의 수를 초기화
        commit('setTodoListCount', selection.myTodolist.length);
        commit('setCompleteListCount', selection.myCompletelist.length);
        // 사용자 선택사항 초기화
        commit('setSelection', selection);
      }
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
  },
  getters: {
    selection(state) {
      return state.selection;
    },
  },
};
