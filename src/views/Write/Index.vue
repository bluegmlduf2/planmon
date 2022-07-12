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
              placeholder="시작예정일을 선택해주세요"
              :class="{ 'is-invalid': validation.startDate }"
              aria-describedby="validationStartDate"
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
              placeholder="종료예정일을 선택해주세요"
              :class="{ 'is-invalid': validation.endDate }"
              aria-describedby="validationEndDate"
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
import VLayout from '@/layouts/Default.vue';
import '@toast-ui/editor/dist/toastui-editor.css';
import '@toast-ui/editor/dist/i18n/ko-kr';
import { Editor } from '@toast-ui/vue-editor';
import countriesList from '@/assets/js/countries';
import stayStatusList from '@/assets/js/stayStatus';
import Flatpickr from '@/components/Flatpickr.vue';
import Confirm from '@/components/Confirm.vue';
import message from '@/assets/js/message';

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
      this.$toast.info({
        component: Confirm,
        props: {
          buttonName: '작성',
          confirmMessage: message.writeConfirm, // 확인메세지 사용자 지정
        },
        listeners: {
          confirmEvent: () => this.testMethod(),
        },
      }, { timeout: 7000 });
    },
    testMethod() {
      console.log(this.countries);
    },
  },
};
</script>
