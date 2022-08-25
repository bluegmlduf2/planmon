export default {
  state: {
    spinner: false,
    loading: false,
    error: null,
  },
  mutations: {
    setSpinner(state, payload) {
      state.spinner = payload;
    },
    setLoading(state, payload) {
      state.loading = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },
    clearError(state) {
      state.error = null;
    },
  },
  actions: {
    setSpinner({ commit }, payload) {
      commit('setSpinner', payload);
    },
    clearError({ commit }) {
      commit('clearError');
    },
    setError({ commit }, payload) {
      commit('setError', payload);
    },
    setLoading(state, payload) {
      state.loading = payload;
    },
  },
  getters: {
    spinner(state) {
      return state.spinner;
    },
    loading(state) {
      return state.loading;
    },
    error(state) {
      return state.error;
    },
  },
};
