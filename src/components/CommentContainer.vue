<template>
  <div>
    <!-- 유저등록정보 -->
    <div class="d-flex justify-content-between align-items-center mb-2">
      <div class="d-flex align-items-center">
        <img
          class="profile-img"
          src="https://placeimg.com/640/480/any"
        >
        <div class="d-flex flex-column align-items-start ml-2">
          <p><b>{{ userName }}</b></p>
          <p class="font-light-color">
            {{ addedDate }}
          </p>
        </div>
      </div>
      <div>
        <div
          v-if="paramShowButtons&&!isUpdateClicked"
          class="post-update-buttons font-light-color"
        >
          <span
            class="mr-2"
            @click="openContent()"
          >
            수정
          </span>
          <span
            @click="destroyContent()"
          >
            삭제
          </span>
        </div>
      </div>
    </div>
    <div>
      <!-- 댓글내용 -->
      <div class="mt-2 mb-2 pl-2 word-break">
        <textarea
          v-if="isUpdateClicked"
          v-model="inputedContent"
          class="form-control input_textarea"
          placeholder="수정할 댓글을 입력해주세요"
          rows="3"
        />
        <span v-else>
          {{ content }}
        </span>
      </div>
      <!-- 댓글버튼 -->
      <div
        v-if="isUpdateClicked"
        class="d-flex justify-content-end mt-2"
      >
        <button
          class="btn mr-2"
          @click="isUpdateClicked=false"
        >
          닫기
        </button>
        <button
          class="btn btn-purple btn-option btn-option-initial-size"
          @click="updateContent"
        >
          수정
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Confirm from '@/components/Confirm.vue';

export default {
  /**
   * The name of the component.
   */
  name: 'CommentContainer',
  /**
   * The properties that the component accepts.
   */
  props: {
    // 댓글,대댓글의 ID
    id: {
      type: String,
      required: true,
    },
    // 호출타입 (댓글,대댓글구분)
    type: {
      type: String,
      required: true,
    },
    // 로그인 상태에 따른 수정,삭제버튼의 표시여부
    paramShowButtons: {
      default: true,
      type: Boolean,
      required: true,
    },
    // 작성자명
    userName: {
      default: '',
      type: String,
      required: true,
    },
    // 작성자의 댓글 등록일
    addedDate: {
      default: '',
      type: String,
      required: true,
    },
    // 댓글내용
    content: {
      default: '',
      type: String,
      required: true,
    },
    // 수정버튼 클릭유무
    isClicked: {
      default: false,
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      // 수정버튼 클릭유무
      isUpdateClicked: this.isClicked,
      // 수정 입력 댓글 내용
      inputedContent: this.content,
    };
  },
  methods: {
    // 댓글창을 열기
    openContent() {
      // 수정 입력 댓글 내용을 초기화및 댓글수정창 열기
      this.inputedContent = this.content;
      this.isUpdateClicked = true;
    },
    // 댓글내용 수정 버튼
    updateContent() {
      // 등록 확인 진행
      this.confirmContent('수정', 'update');
    },
    // 댓글내용 삭제 버튼
    destroyContent() {
      // 삭제 확인 진행
      this.confirmContent('삭제', 'destroy');
    },
    // 댓글내용 수정/삭제 확인
    confirmContent(buttonName, buttontype) {
      const toastId = this.$toast.info({
        component: Confirm,
        props: {
          buttonName, // 확인의 버튼명
          isShowButtons: true, // 확인, 취소버튼 2개 표시
        },
        listeners: {
          // 확인(삭제)버튼
          confirmEvent: () => {
            this.$toast.dismiss(toastId); // 확인창닫기
            const commentParam = { commentId: this.id, commentContent: this.inputedContent }; // 댓글용 파라미터
            const commentReplyparam = { commentReplyId: this.id, commentReplyContent: this.inputedContent }; // 대댓글용 파라미터

            if (buttontype === 'update') {
              // 수정
              if (this.type === 'comment') {
                // 댓글
                this.$store.dispatch('updateComment', commentParam);
              } else if (this.type === 'commentReply') {
                // 대댓글
                this.$store.dispatch('updateCommentReply', commentReplyparam);
              }
            } else if (buttontype === 'destroy') {
              // 삭제
              if (this.type === 'comment') {
                // 댓글
                this.$store.dispatch('destroyComment', commentParam);
              } else if (this.type === 'commentReply') {
                // 대댓글
                this.$store.dispatch('destroyCommentReply', commentReplyparam);
              }
            }
          },
          // 취소버튼
          cancelEvent: () => {
            this.$toast.dismiss(toastId);
          },
        },
      }, { timeout: 5000, closeOnClick: false, closeButton: false });
    },
  },
};
</script>
