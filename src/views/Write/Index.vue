<template>
  <v-layout :is-left-menu-active="true">
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <div class="condition-container">
        <div class="row">
          <div class="form-group col-md-12">
            <input
              v-model="inputData.title"
              type="text"
              class="form-control none-outline"
              :class="{ 'is-invalid': validation.title }"
              placeholder="제목을 입력해주세요"
              aria-describedby="validationTitle"
              required
            >
            <div
              v-if="validation.title"
              id="validationTitle"
              class="invalid-feedback"
            >
              제목을 입력해주세요
            </div>
          </div>
        </div>
        <div class="row">
          <div class="form-group col-md-6">
            <select
              id="exampleFormControlSelect1"
              v-model="inputData.country"
              class="form-control"
              :class="{ 'is-invalid': validation.country }"
              aria-describedby="validationCountry"
              required
            >
              <option
                value="null"
                selected
                disabled
              >
                국가를 선택해주세요
              </option>
              <option
                v-for="country in countries"
                :key="country.value"
                :value="country.value"
              >
                {{ country.text }}
              </option>
            </select>
            <div
              v-if="validation.country"
              id="validationCountry"
              class="invalid-feedback"
            >
              국가를 선택해주세요
            </div>
          </div>
          <div class="form-group col-md-6">
            <select
              id="exampleFormControlSelect1"
              v-model="inputData.stayStatus"
              class="form-control"
              :class="{ 'is-invalid': validation.stayStatus }"
              aria-describedby="validationStayStatus"
              required
            >
              <option
                value="null"
                selected
                disabled
              >
                체류상태를 선택해주세요
              </option>
              <option
                v-for="e in stayStatus"
                :key="e.value"
                :value="e.value"
              >
                {{ e.text }}
              </option>
            </select>
            <div
              v-if="validation.stayStatus"
              id="validationStayStatus"
              class="invalid-feedback"
            >
              체류상태를 선택해주세요
            </div>
          </div>
        </div>
        <div class="row">
          <div class="form-group col-md-6">
            <Flatpickr
              id="entryStartDate"
              :input-date="inputData.startDate"
              input-type="start"
              placeholder="시작예정일을 선택해주세요"
              :class="{ 'is-invalid': validation.startDate }"
              aria-describedby="validationStartDate"
              @onChangeCalendar="checkMydate"
            />
            <div
              v-if="validation.startDate"
              id="validationStartDate"
              class="invalid-feedback"
            >
              시작예정일을 선택해주세요
            </div>
          </div>
          <div class="form-group col-md-6">
            <Flatpickr
              id="entryEndDate"
              :input-date="inputData.endDate"
              input-type="end"
              placeholder="종료예정일을 선택해주세요"
              :class="{ 'is-invalid': validation.endDate }"
              aria-describedby="validationEndDate"
              @onChangeCalendar="checkMydate"
            />
            <div
              v-if="validation.endDate"
              id="validationEndDate"
              class="invalid-feedback"
            >
              종료예정일을 선택해주세요
            </div>
          </div>
        </div>
        <!-- 글쓰는곳 ToastUI Editor -->
        <Editor
          id="toastUiEditor"
          ref="toastuiEditor"
          :initial-value="inputData.content"
          :options="editorOptions"
          height="400px"
          initial-edit-type="wysiwyg"
        />
        <div class="writeContButtons mt-3">
          <div
            id="writeContBack"
            @click="$router.go(-1)"
          >
            <i
              class="fa fa-chevron-left"
              aria-hidden="true"
            />
          </div>
          <div class="writeContWrite">
            <button
              id="writeContPostBtn"
              class="btn btn-purple btn-option"
              :disabled="validation.startDate||validation.endDate"
              @click="writePost"
            >
              <b>{{ post?'수정':'새글등록' }}</b>
            </button>
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
/* eslint-disable no-param-reassign, no-underscore-dangle */
import Vue from 'vue';
import VLayout from '@/layouts/Default.vue';
import '@toast-ui/editor/dist/toastui-editor.css';
import '@toast-ui/editor/dist/i18n/ko-kr';
import { Editor } from '@toast-ui/vue-editor';
import countriesList from '@/assets/js/countries';
import stayStatusList from '@/assets/js/stayStatus';
import Flatpickr from '@/components/Flatpickr.vue';
import Confirm from '@/components/Confirm.vue';
import message from '@/assets/js/message';
import globalFunc from '@/plugins/globalFunc';

Vue.use(globalFunc);

export default {
  /**
   * The name of the page.
   */
  name: 'WriteIndex',
  /**
   * The components that the page can use.
   */
  components: {
    VLayout,
    Editor,
    Flatpickr,
  },
  props: {
    // 게시글화면에서 전달받은 게시글 정보
    post: {
      type: Object,
      default: null,
    },
  },
  data() {
    return {
      countries: [], // 국가
      stayStatus: [], // 체류상태
      selectedStayStatus: null, // 선택된 체류상태 (기본 체류중)
      editorOptions: {
        minHeight: '200px',
        language: 'ko-KR',
        useCommandShortcut: true,
        usageStatistics: true,
        hideModeSwitch: true, // wysiwyg 선택 목록 비표시
        toolbarItems: [
          ['heading', 'bold', 'strike'],
          ['ul', 'ol', 'task'],
          ['image', 'link'],
        ],
        placeholder: '당신의 일정을 공유해주세요..',
      },
      // 입력된 게시글 정보 (수정모드일시 수정입력값을 초기화)
      inputData: {
        title: this.post?.title ?? '',
        content: this.post?.content ?? '',
        country: this.post?.country ?? 'JP',
        stayStatus: this.post?.stayStatus ?? '0',
        startDate: this.post?.startDate ?? '',
        endDate: this.post?.endDate ?? '',
      },
      validation: {
        title: false,
        startDate: false,
        endDate: false,
        country: false,
        stayStatus: false,
        content: false,
      },
    };
  },
  watch: {
    inputData: {
      handler(e) {
        // 제목입력여부확인
        if (!e.title) {
          this.validation.title = true;
        } else {
          this.validation.title = false;
        }
      },
      deep: true,
    },
  },
  created() {
    this.initCountries(); // 국가 초기화
    this.initStayStatus(); // 체류상태 초기화
  },
  methods: {
    // 국가 초기화
    initCountries() {
      this.countries = countriesList;
    },
    // 체류상태 초기화
    initStayStatus() {
      this.stayStatus = stayStatusList;
    },
    // 글쓰기
    writePost() {
      // 입력내용
      const contentMarkdown = this.$refs.toastuiEditor.invoke('getMarkdown'); // 데이터 유효성 테스트용 (HTML태그불포함)
      const contentHTML = this.$refs.toastuiEditor.invoke('getHTML'); // 실제로 DB에 전달할 내용 데이터 (HTML태그포함)
      const myStartDate = document.querySelector('#entryStartDate')?._flatpickr?.selectedDates[0]; // 입력한 시작일정
      const myEndDate = document.querySelector('#entryEndDate')?._flatpickr?.selectedDates[0]; // 입력한 종료일정
      // 입력데이터 객체
      const inputData = { ...this.inputData, content: contentHTML };

      // 미입력항목확인
      const isDisabled = !contentMarkdown || !inputData.title || !myStartDate || !myEndDate;
      if (isDisabled) {
        this.$toast.warning(message.emptyPostWrite);
        return;
      }

      // 확인창
      const toastId = this.$toast.info({
        component: Confirm,
        props: {
          buttonName: this.post ? '수정' : '작성',
          confirmMessage: this.post ? message.writeUpdateConfirm : message.writeConfirm, // 확인메세지 사용자 지정
          isShowButtons: true, // 확인, 취소버튼 2개 표시
        },
        listeners: {
          // 확인(삭제)버튼
          confirmEvent: () => {
            this.$toast.dismiss(toastId); // 확인창닫기
            const commentParam = { inputData }; // 댓글용 파라미터
            // 글수정
            if (this.post) {
              // 수정을 위해 게시글id를 추가
              commentParam.inputData.postId = this.post.postId;
              this.$store.dispatch('updatePost', commentParam); // 게시물 수정
            } else {
            // 글등록
              this.$store.dispatch('createPost', commentParam); // 게시물 등록
            }
          },
          // 취소버튼
          cancelEvent: () => {
            this.$toast.dismiss(toastId);
          },
        },
      }, { timeout: 6000, closeOnClick: false, closeButton: false });
    },
    // 시작 종료일정에 대한 유효성 검사
    checkMydate(selectedDate) {
      // 데이터 컴포넌트에서 입력한 값
      // 파라미터정보 1.데이터형식 입력값 2.YYYY-MM-DD 입력값 3.시작종료컴포넌트타입여부
      const { selectedDates, inputType } = selectedDate;
      const myStartDate = document.querySelector('#entryStartDate')?._flatpickr?.selectedDates[0]; // 입력한 시작일정
      const myEndDate = document.querySelector('#entryEndDate')?._flatpickr?.selectedDates[0]; // 입력한 종료일정

      this.inputData.startDate = Vue.prototype.getDateFormatYYYYMMDD(myStartDate);
      this.inputData.endDate = Vue.prototype.getDateFormatYYYYMMDD(myEndDate);

      // 시작일정을 선택하지 않은 경우 경우
      if (!myStartDate) {
        this.$toast.warning(message.confirmEmptyStartDate);
        this.validation.startDate = true;
      } else if (!myEndDate) {
      // 종료일정을 선택하지 않은 경우 경우
        this.$toast.warning(message.confirmEmptyEndDate);
        this.validation.endDate = true;
      } else if (inputType === 'start' && selectedDates[0] > myEndDate) {
      // 일정 종료일이 일정시작일보다 큰 경우
        this.$toast.warning(message.confirmInvalidDate);
        this.validation.startDate = true;
      } else if (inputType === 'end' && myStartDate > selectedDates[0]) {
      // 일정 종료일이 일정시작일보다 큰 경우
        this.$toast.warning(message.confirmInvalidDate);
        this.validation.endDate = true;
      } else {
      // 유효성에 문제가 없으면 적용버튼을 활성화
        this.validation.startDate = false;
        this.validation.endDate = false;
      }
    },
  },
};
</script>
