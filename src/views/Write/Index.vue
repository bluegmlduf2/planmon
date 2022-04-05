<template>
  <v-layout>
    <div
      slot="default-right-body"
      class="col-md-8 default-right p-4"
    >
      <!-- 글쓰는곳 ToastUI Editor -->
      <Editor
        id="toastUiEditor"
        :initial-value="editorText"
        :options="editorOptions"
        height="400px"
        initial-edit-type="wysiwyg"
      />
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
  },
  data() {
    return {
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
    };
  },

};
</script>
