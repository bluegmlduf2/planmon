import { initializeApp } from 'firebase/app'; // initializeApp는 export default가 아니기 때문에 {}로 불러옴
import { getAuth, onAuthStateChanged } from 'firebase/auth';
// SDK v9를 사용, SDK8는 firebase를 모든 모듈을 통채로 사용했다면 SDK9는 필요한 모듈(auth)만 import하기때문에 적은 용량의 이점이 있음

// 파이어베이스 환경설정파일
const firebaseConfig = {
  apiKey: process.env.VUE_APP_FIREBASE_APP_KEY,
  authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN,
  databaseURL: process.env.VUE_APP_FIREBASE_PROJECT_ID,
  projectId: process.env.VUE_APP_FIREBASE_STORAGE_BUCKET,
  storageBucket: process.env.VUE_APP_FIREBASE_MESSAGING_SENDER_ID,
  messagingSenderId: process.env.VUE_APP_FIREBASE_APP_ID,
  appId: process.env.VUE_APP_FIREBASE_MEASUREMENT_ID,
};

// 반환값
const returnModule = {
  onAuthStateChanged,
};

// 파이어베이스 모듈들을 내보냄
// 싱글턴 패턴
function initFireBase() {
  // 한번 초기화 된적이 있으면 firebase모듈만 내보낸다
  if (returnModule.auth) {
    // 파이어베이스 모듈반환
    return returnModule;
  }
  // 최초 로딩시 한번만 파이어베이스 초기화
  initializeApp(
    firebaseConfig,
  );

  returnModule.auth = getAuth();
  // 파이어베이스 모듈반환
  return returnModule;
}

export default initFireBase();
