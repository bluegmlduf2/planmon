import Vue from 'vue';
import message from '@/assets/js/message';
import ImageProxy from '@/proxies/ImageProxy';

export default {
  actions: {
    // 이미지 등록
    uploadImage({ commit }, payload) {
      commit('setSpinner', true); // 스피너 동작

      // 이미지 정보 등록
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
  },
};
