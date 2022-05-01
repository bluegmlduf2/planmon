import { initializeApp } from 'firebase/app'; // initializeApp는 export default가 아니기 때문에 {}로 불러옴
import {
  getAuth,
  onAuthStateChanged,
  signOut, setPersistence,
  browserLocalPersistence,
  GoogleAuthProvider,
  signInWithPopup,
  sendSignInLinkToEmail,
  isSignInWithEmailLink,
  signInWithEmailLink,
  updateProfile,
  deleteUser,
} from 'firebase/auth';
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

// 이메일링크를 위한 설정파일
const actionCodeSettings = {
  // 링크인증후 리다이렉트가 되길 원하는 주소를 입력. 만약 이 주소가 프로젝트의 승인된 도메인에 없다면 에러가 발생
  url: process.env.VUE_APP_FIREBASE_URL,
  // This must be true.
  handleCodeInApp: true,
};

// 반환값
const returnModule = {
  onAuthStateChanged,
  signOut,
  setPersistence,
  browserLocalPersistence,
  signInWithPopup,
  GoogleAuthProvider,
  sendSignInLinkToEmail,
  actionCodeSettings,
  isSignInWithEmailLink,
  signInWithEmailLink,
  updateProfile,
  deleteUser,
};

// 파이어베이스 모듈들을 내보냄
function initFireBase() {
  // 파이어베이스 초기화
  initializeApp(
    firebaseConfig,
  );
  returnModule.auth = getAuth();
  returnModule.auth.languageCode = 'ko';

  // 로그인상태 지속여부
  setPersistence(returnModule.auth, browserLocalPersistence);

  // 파이어베이스 모듈반환
  return returnModule;
}

export default initFireBase();
