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
              v-model="selectedCountry"
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
              v-model="selectedStayStatus"
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
              :input-date="entryDate"
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
              :input-date="entryDate"
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
          :initial-value="editorText"
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
            >
              <b>글쓰기</b>
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
  data() {
    return {
      countries: [], // 국가
      stayStatus: [], // 체류상태
      selectedCountry: null, // 선택된 국가
      selectedStayStatus: null, // 선택된 체류상태 (기본 체류중)
      editorText: '',
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
    this.initEntyDate(); // 입국날짜 초기화
    this.initCountries(); // 국가 초기화
    this.initStayStatus(); // 체류상태 초기화
  },
  methods: {
    // 입국날짜 초기화
    initEntyDate() {
      // const todayDate = new Date().toISOString().slice(0, 10); // 오늘날짜를 yyyy-mm-dd 형식으로 받는다
      // this.entryDate = todayDate;
      this.entryDate = ''; // TODO 삭제예정
    },
    // 국가 초기화
    initCountries() {
      this.countries = countriesList;
    },
    // 체류상태 초기화
    initStayStatus() {
      this.stayStatus = stayStatusList;
    },
  },
};
</script>
