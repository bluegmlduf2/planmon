<template>
  <v-layout :is-left-menu-active="true">
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <div class="condition-container">
        <!-- 모바일화면용 뒤로가기버튼 -->
        <div class="row mb-3">
          <div class="col-md-12 post-back ml-2">
            <span @click="$router.push({name: 'home.index'})">
              <i
                class="fa fa-chevron-left"
                aria-hidden="true"
              />
            </span>
          </div>
        </div>
        <!-- 게시글 제목 -->
        <div class="row">
          <div class="col-md-12 mt-1 mb-3 post-title">
            <h2>
              제목입니다^^
            </h2>
            <div
              class="list-checkbox list-add mr-1"
            >
              <input
                id="itemvalue"
                type="checkbox"
              >
              <label for="itemvalue" />
            </div>
          </div>
        </div>
        <!-- 이름과 수정삭제 버튼 -->
        <div class="row justify-content-between mb-3">
          <div class="col-md-12 post-user-info">
            <div>
              <span
                class="post-bold mr-2"
              >사용자명</span>
              <span>2022년 12월 13일</span>
            </div>
            <div class="post-update-buttons">
              <span class="mr-2">
                수정
              </span>
              <span>
                삭제
              </span>
            </div>
          </div>
        </div>
        <!-- 조건 1 -->
        <div class="post-condition mb-2">
          <h5 class="mb-2">
            작성자 기준
          </h5>
          <div class="row">
            <div class="form-group col-6">
              <label for="postStartDate">일정시작일자</label>
              <div
                id="postStartDate"
                class="post-date"
              >
                2022년 12월 15일
              </div>
            </div>
            <div class="form-group col-6">
              <label for="postEndDate">일정종료일자</label>
              <div
                id="postEndDate"
                class="post-date"
              >
                2022년 12월 31일
              </div>
            </div>
          </div>
        </div>
        <!-- 조건 2 -->
        <div class="post-condition mb-3">
          <div class="mb-2 post-startDate-cont">
            <h5>
              {{ true?'내 입국일 기준':'내 지정일 기준' }}
            </h5>
            <span>일정시작일자 변경</span>
          </div>
          <div class="row">
            <div class="form-group col-6">
              <label for="postStartDate">일정시작일자</label>
              <div
                id="postStartDate"
                class="post-date"
              >
                2022년 12월 10일
              </div>
            </div>
            <div class="form-group col-6">
              <label for="postEndDate">일정종료일자</label>
              <div
                id="postEndDate"
                class="post-date"
              >
                2022년 12월 31일
              </div>
            </div>
          </div>
        </div>
        <!-- 게시글표시 ToastUI Editor -->
        <Viewer
          id="toastUiEditor"
          :initial-value="viewerText"
          height="400px"
        />
        <div class="mt-3">
          댓글창을 넣을 예정
        </div>
      </div>
    </div>
  </v-layout>
</template>

<script>
/* ============
 * Home Index Page
 * ============
 *
 * The home index page.
 */

// Basic Use - Covers most scenarios
import VLayout from '@/layouts/Default.vue';
import '@toast-ui/editor/dist/toastui-editor-viewer.css';
import { Viewer } from '@toast-ui/vue-editor';
import post from '@/assets/js/post';

export default {
  /**
   * The name of the page.
   */
  name: 'PostIndex',
  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    Viewer,
  },
  data() {
    return {
      countries: [], // 국가
      selectedCountry: null, // 선택된 국가
      viewerText: '',
      validation: {
        title: false,
        startDate: false,
        endDate: false,
        country: false,
        content: false,
      },
    };
  },
  created() {
    this.initEntyDate(); // 입국날짜 초기화
    this.initPost(); // 게시글 초기화
  },
  methods: {
    // 입국날짜 초기화
    initEntyDate() {
      const todayDate = new Date().toISOString().slice(0, 10); // 오늘날짜를 yyyy-mm-dd 형식으로 받는다
      this.entryDate = todayDate;
    },
    // 게시글 초기화
    initPost() {
      this.viewerText = post;
    },
  },
};
</script>
