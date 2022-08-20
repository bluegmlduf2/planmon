<template>
  <v-layout :is-left-menu-active="true">
    <div
      slot="default-right-body"
      class="col-md-8 default-right pt-3 pl-4 pr-4 pb-4"
    >
      <!-- v-if는 post의 최초 로딩시 nullException을 막기 위해 사용 -->
      <div
        v-if="post"
        class="condition-container"
      >
        <!-- 게시글 제목 -->
        <div class="d-flex justify-content-between align-items-center">
          <div>
            <span
              class="tag"
              :class="setStayStatusTag(post.stayStatus)"
            >{{ setStayStatusTagName(post.stayStatus) }}</span>
            <img
              class="ml-2 mb-1"
              :src="postNation"
            >
          </div>
          <div class="d-flex align-items-center">
            <span class="mr-2 scrab-span"><i
              class="fa fa-comment-o"
              aria-hidden="true"
            /> {{ comments.length }}</span>
            <span class="mr-2 scrab-span"><i
              class="fa fa-eye"
              aria-hidden="true"
            /> {{ post.postViewCount }}</span>
            <div
              class="list-checkbox list-add mr-1"
              :class="setCheckStatus(post.isCompleted)"
            >
              <input
                :id="post.postId"
                type="checkbox"
                :checked="post.isAdded"
                :disabled="post.isCompleted"
                @click="updatePostCheckInput($event)"
              >
              <label :for="post.postId" />
            </div>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-md-12 mt-1 mb-3 post-title">
            <h2 class="word-break">
              {{ post.title }}
            </h2>
          </div>
        </div>
        <!-- 이름과 수정삭제 버튼 -->
        <div class="row justify-content-between mb-3">
          <div class="col-md-12 post-user-info">
            <div>
              <span
                class="post-bold mr-2"
              >{{ post.writerUserName }}</span>
              <span class="font-light-color">{{ getDateFormat(post.createdDate) }}</span>
            </div>
            <div class="post-update-buttons font-light-color">
              <span
                v-if="user && post.userAuth"
                class="mr-2"
                @click="$router.push({name: 'write.index', params: {post}})"
              >
                수정
              </span>
            </div>
          </div>
        </div>
        <!-- 조건 1 -->
        <div class="post-condition mb-2">
          <h5 class="mb-2">
            작성자 일정
          </h5>
          <div class="row">
            <div class="form-group col-6">
              <label for="postStartDate">일정시작일</label>
              <div
                id="postStartDate"
                class="post-date"
              >
                {{ getDateFormat(post.startDate) }}
              </div>
            </div>
            <div class="form-group col-6">
              <label for="postEndDate">일정종료일({{ getDateDiff(post.startDate,post.endDate) }})</label>
              <div
                id="postEndDate"
                class="post-date"
              >
                {{ getDateFormat(post.endDate) }}
              </div>
            </div>
          </div>
        </div>
        <!-- 조건 2 (작성자에게는 표시하지 않음)-->
        <div
          v-if="!user || !post.userAuth"
          class="post-condition mb-3"
        >
          <div class="mb-2 post-startDate-cont">
            <h5 class="ellipsis">
              {{ userName }}의 일정
            </h5>
            <!-- 슬라이드 메뉴 -->
            <!-- 일정변경버튼은 일정추가된 상태 & 완료된 일정이 아닐시 표시 -->
            <span
              v-if="post.isAdded && !post.isCompleted"
              class="font-light-color list-menu-body write-span-font"
              @click="toggleMenuActive=!toggleMenuActive"
            >일정 변경</span>
            <ul
              class="list-menu list-option-post"
              :class="[toggleMenuActive?'open':'']"
            >
              <li class="pt-2 pl-1 text-left">
                <label for="appointStartDate">일정시작일 지정</label>
                <Flatpickr
                  id="appointStartDate"
                  :input-date="myStartDate"
                  input-type="start"
                  placeholder="일정시작일을 선택해주세요"
                  @onChangeCalendar="checkMydate"
                />
              </li>
              <li class="pt-2 pl-1 text-left">
                <label for="appointEndDate">일정종료일 지정</label>
                <Flatpickr
                  id="appointEndDate"
                  :input-date="myEndDate"
                  input-type="end"
                  placeholder="일정종료일을 선택해주세요"
                  @onChangeCalendar="checkMydate"
                />
              </li>
              <li class="d-flex flex-row-reverse pt-2 pb-2">
                <button
                  class="btn btn-outline-secondary"
                  style="border-radius:10px"
                  @click="closeCalendar"
                >
                  닫기
                </button>
                <button
                  class="btn btn-purple btn-option btn-option-initial-size mr-2"
                  :disabled="validation.myStartEndDate"
                  @click="changeCalendar"
                >
                  적용
                </button>
              </li>
            </ul>
          </div>
          <div class="row">
            <div class="form-group col-6">
              <label for="postStartDate">일정시작일</label>
              <div
                v-if="myStartDate"
                id="postStartDate"
                class="post-date"
              >
                {{ getDateFormat(myStartDate) }}
              </div>
              <div
                v-else
                class="post-date"
              >
                일정을 추가해주세요
              </div>
            </div>
            <div class="form-group col-6">
              <label for="postEndDate">일정종료일
                <span v-if="myStartDate&&myEndDate">
                  ({{ getDateDiff(myStartDate,myEndDate) }})
                </span>
              </label>
              <div
                v-if="myEndDate"
                id="postEndDate"
                class="post-date"
              >
                {{ getDateFormat(myEndDate) }}
              </div>
              <div
                v-else
                class="post-date"
              >
                일정을 추가해주세요
              </div>
            </div>
          </div>
        </div>
        <!-- 게시글표시 ToastUI Editor -->
        <Viewer
          id="toastUiEditor"
          :initial-value="post.content"
          height="400px"
        />
        <!-- 댓글영역 -->
        <div class="mt-5 post-comment-write">
          <div class="mb-2">
            <h5>{{ comments.length }}건의 댓글</h5>
          </div>
          <!-- 댓글입력 -->
          <div>
            <div v-if="user">
              <textarea
                v-model="commentContent"
                class="form-control input_textarea"
                placeholder="댓글을 입력해주세요"
                rows="3"
                maxlength="1000"
              />
            </div>
            <div
              v-if="user"
              class="d-flex justify-content-end mt-2"
            >
              <button
                class="btn btn-purple btn-option font-weight-bold"
                @click="createComment"
              >
                댓글작성
              </button>
            </div>
          </div>
          <!-- 댓글표시-->
          <div
            v-for="comment in comments"
            :key="comment.commentId"
            class="post-comment-view mt-3"
          >
            <!-- 댓글정보 -->
            <CommentContainer
              :id="comment.commentId"
              type="comment"
              :param-show-buttons="comment.commentUserAuth"
              :user-name="comment.commentUserName"
              :user-image="comment.commentUserImage"
              :added-date="comment.commentAddedDate"
              :content="comment.commentContent"
              :is-clicked="comment.isCommentClicked"
            />
            <!-- 대댓글 열기닫기 버튼 -->
            <div
              class="comment-reply-show"
            >
              <span
                v-if="commentReplyCount(comment) == 0 && !comment.isOpenClicked && user"
                @click="comment.isOpenClicked=true"
              >
                <i
                  class="fa fa-plus ml-1 mr-1"
                  aria-hidden="true"
                />
                댓글남기기
              </span>
              <span
                v-else-if="commentReplyCount(comment)&& !comment.isOpenClicked"
                @click="comment.isOpenClicked=true"
              >
                <i
                  class="fa fa-plus ml-1 mr-1"
                  aria-hidden="true"
                />
                {{ commentReplyCount(comment)+'건의 댓글' }}
              </span>
              <span
                v-else-if="comment.isOpenClicked"
                @click="comment.isOpenClicked=false"
              >
                <i
                  class="fa fa-minus ml-1 mr-1"
                  aria-hidden="true"
                />
                댓글접기
              </span>
            </div>
            <!-- 대댓글영역-->
            <div
              v-for="(commentReply,idx) in comment.commentReply"
              :key="idx"
            >
              <div
                v-if="comment.isOpenClicked"
                class="comment-reply-cont"
                :class="idx==0 ?'mt-2':''"
              >
                <!-- 대댓글정보 -->
                <CommentContainer
                  :id="commentReply.commentReplyId"
                  type="commentReply"
                  :param-show-buttons="commentReply.commentReplyUserAuth"
                  :user-name="commentReply.commentReplyUserName"
                  :user-image="commentReply.commentReplyUserImage"
                  :added-date="commentReply.commentReplyAddedDate"
                  :content="commentReply.commentReplyContent"
                  :is-clicked="commentReply.isCommentReplyClicked"
                />
              </div>
            </div>
            <!-- 대댓글 입력-->
            <div
              v-if="user&& comment.isOpenClicked"
            >
              <div
                v-if="!comment.isWriteClicked"
                class="mt-3"
              >
                <span
                  class="btn btn-outline-secondary w-100"
                  @click="comment.isWriteClicked = true"
                >댓글작성</span>
              </div>
              <div
                v-else
                class="mt-3"
              >
                <hr>
                <textarea
                  class="form-control input_textarea"
                  placeholder="댓글을 입력해주세요"
                  rows="3"
                />
                <!-- 대댓글작성버튼 -->
                <div class="d-flex justify-content-end mt-2">
                  <button
                    class="btn mr-2"
                    @click="comment.isWriteClicked = false"
                  >
                    닫기
                  </button>
                  <button
                    class="btn btn-purple btn-option btn-option-initial-size"
                    @click="createCommentReply($event,comment.commentId)"
                  >
                    등록
                  </button>
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

/* eslint-disable no-param-reassign, no-underscore-dangle */
import Vue from 'vue';
import VLayout from '@/layouts/Default.vue';
import CommentContainer from '@/components/CommentContainer.vue';
import '@toast-ui/editor/dist/toastui-editor-viewer.css';
import { Viewer } from '@toast-ui/vue-editor';
import Flatpickr from '@/components/Flatpickr.vue';
// import Login from '@/views/Login/Index.vue';
import Confirm from '@/components/Confirm.vue';
import message from '@/assets/js/message';
import globalFunc from '@/plugins/globalFunc';
import countries from '@/assets/js/countries';

// 공통함수사용
Vue.use(globalFunc);

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
    CommentContainer,
    Flatpickr,
  },
  data() {
    return {
      countries: [], // 국가
      selectedCountry: null, // 선택된 국가
      toggleMenuActive: false, // 슬라이드 토글 메뉴 활성화
      deleteButtonActive: false, // 삭제상태 활성화
      commentContent: '', // 입력중인 댓글내용
      validation: {
        // 나의 시작종료일정의 유효성유무
        myStartEndDate: false,
      },
    };
  },
  computed: {
    // 게시글 정보
    post() {
      return this.$store.getters.post;
    },
    // 댓글 정보
    comments() {
      return this.$store.getters.comments;
    },
    // 유저정보
    user() {
      return this.$store.getters.user;
    },
    // 유저이름
    userName() {
      return this.user?.name ? this.user.name : '사용자';
    },
    // 로컬스토리지 저장 알림창 (store에서 값이 변경될때마다 갱신)
    showMessage() {
      return this.$store.getters.selection.isShowMessage;
    },
    // 일정시작일
    myStartDate() {
      return this.$store.getters.post.myStartDate || '';
    },
    // 일정종료일
    myEndDate() {
      return this.$store.getters.post.myEndDate || '';
    },
    // 게시글의 국가 이미지 반환
    postNation() {
      const { country } = this.post;
      if (country === countries[0].value) {
        // eslint-disable-next-line global-require
        return require('@/assets/img/japan.png');
      } if (country === countries[1].value) {
        // eslint-disable-next-line global-require
        return require('@/assets/img/america.png');
      } if (country === countries[2].value) {
        // eslint-disable-next-line global-require
        return require('@/assets/img/china.png');
      }
      return '';
    },
  },
  watch: {
    commentContent(newVal, oldVal) {
      // 입력한 글자수가 초과하는 경우
      if (newVal.length > 1000) {
        this.$toast.warning(message.invalidInputLength('1000'));
        this.commentContent = oldVal;
      }
    },
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
    async initPost() {
      // 사용자 선택값 데이터 초기화
      await this.$store.dispatch('setInitSelection');

      const { postId } = this.$route.params; // URL로 부터 취득한 게시물 번호
      await this.$store.dispatch('setInitPost', postId);
    },
    // 추가,삭제 체크박스 선택시
    updatePostCheckInput(e) {
      // 추가, 삭제 메인 진행 함수
      const processUpdate = () => {
        const { isAdded, postId } = this.post;
        // isAdded: !isAdded 추가모드 isAdded 삭제모드
        const param = {
          postId,
          isAdded: !isAdded,
        };
        // 추가일정일시 rec 삭제일정일시 todo
        param.listKind = param.isAdded ? 'rec' : 'todo';
        // 일정에 추가후 일정화면 초기화
        this.$store.dispatch('updateList', param);
        this.$store.dispatch('setInitPost', postId);
      };

      // 확인창 표시
      const confirmToast = (buttonName, confirmMessage) => {
        const toastId = this.$toast.info({
          component: Confirm,
          props: {
            buttonName, // 확인의 버튼명
            isShowButtons: true, // 확인, 취소버튼 2개 표시
            confirmMessage, // 확인메세지 사용자 지정
          },
          listeners: {
            // 확인(삭제)버튼
            confirmEvent: () => {
              this.$toast.dismiss(toastId);
              if (confirmMessage) {
                // 추가모드에서 확인한 경우
                // 로컬스토리지 경고 메세지 표시하지 않음을 설정
                this.$store.dispatch('addSelection', { isShowMessage: false });
              } else {
                // 삭제모드에서 삭제한 경우
                processUpdate();
              }
            },
            // 취소버튼 (삭제 취소시 체크표시를 취소)
            cancelEvent: () => {
              this.$toast.dismiss(toastId);
              e.target.checked = !e.target.checked;
            },
          },
        }, { timeout: 5000, closeOnClick: false, closeButton: false });
      };

      // 현재 함수의 메인로직, 체크효과를 위해 체크후 0.4초후에 실행한다
      setTimeout(() => {
        const { isAdded } = this.post; // 게시물의 추가상태유무
        // 추가 삭제 로직 분기

        // isAdded: !isAdded 추가모드 isAdded 삭제모드
        // 일정추가
        if (!isAdded) {
          // 다시보기 메세지 표시 (메세지보기가 상태이고 미로그인시)
          if (this.showMessage && !this.user) {
            confirmToast('확인', message.localStorageListAlert);
          }
          // 추가 진행
          processUpdate();
        } else {
          // 일정 삭제
          confirmToast('삭제');
        }
      }, 400);
    },
    // 일정변경창의 적용버튼
    async changeCalendar() {
      const myStartDate = Vue.prototype.getDateFormatYYYYMMDD(document.querySelector('#appointStartDate')?._flatpickr?.selectedDates[0]); // 입력한 시작일정을 YYYY-MM-DD형식으로 저장
      const myEndDate = Vue.prototype.getDateFormatYYYYMMDD(document.querySelector('#appointEndDate')?._flatpickr?.selectedDates[0]); // 입력한 종료일정을 YYYY-MM-DD형식으로 저장
      const param = { myStartDate, myEndDate };
      await this.$store.dispatch('updatePostCalendar', param);
      this.toggleMenuActive = !this.toggleMenuActive;
    },
    // 나의 시작 종료일정에 대한 유효성 검사
    checkMydate(selectedDate) {
      // 데이터 컴포넌트에서 입력한 값
      // 파라미터정보 1.데이터형식 입력값 2.YYYY-MM-DD 입력값 3.시작종료컴포넌트타입여부
      const { selectedDates, inputType } = selectedDate;
      const myStartDate = document.querySelector('#appointStartDate')?._flatpickr?.selectedDates[0]; // 입력한 시작일정
      const myEndDate = document.querySelector('#appointEndDate')?._flatpickr?.selectedDates[0]; // 입력한 종료일정

      // 시작일정을 선택하지 않은 경우 경우
      if (!myStartDate) {
        this.$toast.warning(message.confirmEmptyStartDate);
        this.validation.myStartEndDate = true;
      } else if (!myEndDate) {
      // 종료일정을 선택하지 않은 경우 경우
        this.$toast.warning(message.confirmEmptyEndDate);
        this.validation.myStartEndDate = true;
      } else if (inputType === 'start' && selectedDates[0] > myEndDate) {
      // 일정 종료일이 일정시작일보다 큰 경우
        this.$toast.warning(message.confirmInvalidDate);
        this.validation.myStartEndDate = true;
      } else if (inputType === 'end' && myStartDate > selectedDates[0]) {
      // 일정 종료일이 일정시작일보다 큰 경우
        this.$toast.warning(message.confirmInvalidDate);
        this.validation.myStartEndDate = true;
      } else {
      // 유효성에 문제가 없으면 적용버튼을 활성화
        this.validation.myStartEndDate = false;
      }
    },
    // 일정변경창의 닫기버튼
    closeCalendar() {
      // 미적용상태 알림
      if (this.validation.myStartEndDate) {
        this.$toast.warning(message.noticeNotChangedDate);
      }
      this.toggleMenuActive = !this.toggleMenuActive;
    },
    // 체크박스의 활성상태 제어 (computed파라미터전달이 안되서 method로 작성)
    setCheckStatus(isCompleted) {
      // 모든 일정화면에서 완료일정의 추가시 체크박스 비표시
      if (isCompleted) {
        return 'visible-hidden';
      }
      return '';
    },
    // 대댓글의 갯수 (computed로 파라미터를 넘기는건 권장되지않기때문에 메서드 사용)
    commentReplyCount(comment) {
      return comment.commentReply.length;
    },
    // 댓글작성
    async createComment() {
      const param = { commentContent: this.commentContent };

      // 댓글 입력확인
      if (!this.commentContent) {
        this.$toast.warning(message.invalidEmptyInput('댓글'));
        return;
      }

      await this.$store.dispatch('createComment', param);
      this.commentContent = ''; // 입력한 댓글을 초기화
    },
    // 대댓글작성
    async createCommentReply(e, commentId) {
      // 입력한 대댓글내용
      const commentReplyContent = e.target.parentElement.parentElement.querySelector('textarea').value;

      // 대댓글 입력확인
      if (!commentReplyContent) {
        this.$toast.warning(message.invalidEmptyInput('댓글'));
        return;
      }
      // 대댓글 글자수 체크
      if (commentReplyContent.length > 1000) {
        this.$toast.warning(message.invalidInputLength('1000'));
        return;
      }

      const param = { commentId, commentReplyContent };
      await this.$store.dispatch('createCommentReply', param);
    },
  },
};
</script>
