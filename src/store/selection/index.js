import SelectionProxy from '@/proxies/SelectionProxy';
import { router } from '@/plugins/vue-router';

// 선택 정보의 초기값
const selectionInit = {
  country: null,
  stayStatus: null,
  entryDate: null,
  isShowMessage: true,
  myTodolist: [{ postId: '1' }, { postId: '2' }], // 로컬스토리지 보관을 위헤 위해 postId키만 보관
  // myCompletelist: [{ postId: '3' }, { postId: '4' }], // 로컬스토리지 보관을 위헤 postId키만 보관
  // myTodolist: [], // 로컬스토리지 보관을 위헤 위해 postId키만 보관
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
    setInitSelection({ commit }) {
      const isLogined = this.getters.user;
      // 로그인상태일시
      if (isLogined) {
        new SelectionProxy()
          .getSelection()
          .then((response) => {
            // 사용자 선택사항 초기화
            commit('setSelection', response.data);
            // TODO일정 초기화 (표시용)
            // TODOLIST화면에서 2번 호출되는걸 막기 위한 처리
            if (router.currentRoute.path !== '/todolist') {
              this.dispatch('setInitTodoList');
            }
          })
          .catch(() => {
            console.log('Request failed...');
          });
      } else {
      // 미로그인시
        const selectionStorage = window.localStorage.getItem('selection');
        // 기존의 로컬스토리지가 없다면 추가한다
        if (!selectionStorage) {
          window.localStorage.setItem('selection', JSON.stringify(selectionInit));
        }
        const selection = JSON.parse(window.localStorage.getItem('selection'));
        // 사용자 선택사항 초기화
        commit('setSelection', selection);
        // TODO일정 초기화 (표시용)
        // TODOLIST화면에서 2번 호출되는걸 막기 위한 처리
        if (router.currentRoute.path !== '/todolist') {
          this.dispatch('setInitTodoList');
        }
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
