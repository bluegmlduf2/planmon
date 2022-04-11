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
              <span class="font-light-color">2022년 12월 13일</span>
            </div>
            <div class="post-update-buttons font-light-color">
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
            <!-- 슬라이드 메뉴 -->
            <span
              class="font-light-color list-menu-body"
              @click="toggleMenuActive=!toggleMenuActive"
            >일정시작일자 변경</span>
            <ul
              class="list-menu list-option-post"
              :class="[toggleMenuActive?'open':'']"
            >
              <li class="pt-2 pl-1 text-left">
                <label for="appointStartDate">일정시작일 지정</label>
                <Flatpickr
                  id="appointStartDate"
                  :input-date="entryDate"
                  placeholder="일정시작일을 선택해주세요"
                />
              </li>
              <li class="pt-2 pl-1 text-left">
                <label for="appointEndDate">일정종료일 지정</label>
                <Flatpickr
                  id="appointEndDate"
                  :input-date="entryDate"
                  placeholder="일정종료일을 선택해주세요"
                />
              </li>
              <li class="d-flex flex-row-reverse pt-2 pb-2">
                <button
                  class="btn btn-outline-secondary"
                  style="border-radius:10px"
                  @click="toggleMenuActive=!toggleMenuActive"
                >
                  닫기
                </button>
                <button class="btn btn-purple btn-option btn-option-initial-size mr-2">
                  적용
                </button>
              </li>
            </ul>
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
        <!-- 댓글영역 -->
        <div class="mt-5 post-comment-write">
          <div class="mb-2">
            <h5>4건의 댓글</h5>
          </div>
          <!-- 댓글입력부 -->
          <div>
            <div>
              <textarea
                class="form-control input_textarea"
                placeholder="댓글을 입력해주세요"
                rows="3"
              />
            </div>
            <div class="d-flex justify-content-end mt-2">
              <button
                class="btn btn-purple btn-option font-weight-bold"
              >
                댓글작성
              </button>
            </div>
          </div>
          <!-- 댓글표시부 -->
          <div class="post-comment-view mt-3">
            <!-- 댓글작성자정보 -->
            <UserInfo />
            <!-- 댓글표시 -->
            <div class="mt-2 mb-2 pl-2">
              <span>
                {{ 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'.repeat(5) }}
              </span>
            </div>
            <!-- 대댓글 영역 -->
            <div>
              <div class="comment-reply-show">
                <span v-if="true">
                  <i
                    class="fa fa-plus ml-1 mr-1"
                    aria-hidden="true"
                  />
                  {{ true?'1건의 댓글':'댓글남기기' }}
                </span>
                <span v-else>
                  <i
                    class="fa fa-minus ml-1 mr-1"
                    aria-hidden="true"
                  />
                  댓글접기
                </span>
              </div>
              <!-- 대댓글 표시부 -->
              <div class="comment-reply-cont">
                <!-- 댓글작성자정보 -->
                <UserInfo />
                <!-- 댓글표시 -->
                <div class="mt-2 mb-3 pl-2">
                  <span>
                    {{ 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'.repeat(5) }}
                  </span>
                </div>
                <!-- 대댓글 입력부 열기버튼-->
                <div
                  v-if="true"
                  class="mt-3"
                >
                  <span class="btn btn-outline-secondary w-100">댓글작성</span>
                </div>
                <!-- 대댓글 입력부-->
                <div
                  v-else
                  class="mt-4"
                >
                  <hr>
                  <textarea
                    class="form-control input_textarea"
                    placeholder="댓글을 입력해주세요"
                    rows="3"
                  />
                  <!-- 대댓글작성버튼 -->
                  <div class="d-flex justify-content-end mt-2">
                    <button class="btn mr-2">
                      닫기
                    </button>
                    <button class="btn btn-purple btn-option btn-option-initial-size">
                      등록
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
import UserInfo from '@/components/UserInfo.vue';
import '@toast-ui/editor/dist/toastui-editor-viewer.css';
import { Viewer } from '@toast-ui/vue-editor';
import post from '@/assets/js/post';
import Flatpickr from '@/components/Flatpickr.vue';

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
    UserInfo,
    Flatpickr,
  },
  data() {
    return {
      countries: [], // 국가
      selectedCountry: null, // 선택된 국가
      viewerText: '',
      toggleMenuActive: false, // 슬라이드 토글 메뉴 활성화
      deleteButtonActive: false, // 삭제상태 활성화
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
