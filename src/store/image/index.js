import Vue from 'vue';
import message from '@/assets/js/message';
import ImageProxy from '@/proxies/ImageProxy';

export default {
  actions: {
    // 게시물 이미지 등록
    uploadImage({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작

      // 게시물 이미지 정보 등록
      return new ImageProxy()
        .uploadImage(payload)
        .then((response) => {
          Vue.prototype.$toast.info(message.addImage);
          // 등록한 이미지 정보 반환
          return response.data;
        })
        .catch(() => {
          console.log('Request failed...');
        })
        .finally(() => {
          commit('setSpinner', false); // 스피너 정지
        });
    },

    // 유저 이미지 등록
    uploadUserImage({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작
      // 유저 이미지 정보 등록후 URL반환
      return new ImageProxy()
        .uploadUserImage(payload)
        .then((response) => response.data)
        .catch(() => {
          console.log('Request failed...');
        })
        .finally(() => {
          commit('setSpinner', false); // 스피너 정지
        });
    },

    // 유저 이미지 삭제
    deleteUserImage({ commit }) {
      commit('setSpinner', true); // 스피너 동작

      // 유저 이미지 정보 삭제
      return new ImageProxy()
        .deleteUserImage()
        .then(() => true)
        .catch(() => {
          console.log('Request failed...');
        })
        .finally(() => {
          commit('setSpinner', false); // 스피너 정지
        });
    },
  },
};
