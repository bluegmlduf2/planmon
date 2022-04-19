/* ============
 * vue-toastification
 * ============
 *
 * 토스트 메세지
 *
 * https://github.com/Maronato/vue-toastification/tree/main
 */
import Vue from 'vue';
import Toast from 'vue-toastification';
// Import the CSS or use your own!
import 'vue-toastification/dist/index.css';

// You can set your default options here
const options = {
  transition: 'Vue-Toastification__fade', // 메세지 표현
  maxToasts: 10, // 최대 메세지표시수
  newestOnTop: true, // 새로운메세지를 상단에 표시
  position: 'top-center', // 위치
  timeout: 3500, // 표시시간
  closeOnClick: true, // 닫기버튼사용유무
  pauseOnFocusLoss: true, // 화면에 포커스를 놓치면 프로그레스가 멈춘다
  pauseOnHover: true, // 마우스를 올리면 프로그레스가 멈춘다
  draggable: true, // 드래그가능
  draggablePercent: 0.6, // 드래그종료퍼센트
  showCloseButtonOnHover: false, // 마우스 올리면 종료버튼을 보여준다
  hideProgressBar: false, // 프로그레스바사용유무
  closeButton: 'button',
  icon: false, // 아이콘사용유무
  rtl: true, // 프로그레스바 진행방향
};

Vue.use(Toast, options);
