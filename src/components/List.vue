<template>
  <div class="list-container">
    <slot name="search" />
    <div class="list-haeder">
      <h4>
        <slot name="header" />
      </h4>
      <div class="list-menu-body">
        <i
          class="fa fa-ellipsis-h"
          aria-hidden="true"
          @click="toggleMenuActive=!toggleMenuActive"
        />
        <ul
          class="list-menu list-option-home"
          :class="openSlideMenu"
        >
          <li>등록일자순 정렬</li>
          <li>완료순으로 정렬</li>
          <li
            v-if="paramShowButtons"
            @click="changeCheckInput"
          >
            {{ isAdded?'일정 삭제':'일정 추가' }}
          </li>
        </ul>
      </div>
    </div>
    <div class="list-body list-blind">
      <ul class="list-body-ul">
        <li
          v-for="(item, index) in paramList"
          :key="index"
        >
          <!-- 일정 -->
          <div class="list-item">
            <div
              class="list-checkbox"
              :class="setCheckStatus(item)"
            >
              <input
                :id="item.value"
                type="checkbox"
                @click="updateCheckInput($event,item)"
              >
              <label :for="item.value" />
            </div>
            <span
              class="list-content ellipsis"
              @click="$router.push({name: 'post.index'})"
            >
              {{ item.text }}
            </span>
            <span
              class="tag tag-list tag-blue"
            >
              체류중 일정
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import SlotMixin from '@/mixins/slot';
import Confirm from '@/components/Confirm.vue';

export default {
  /**
   * The name of the component.
   */
  name: 'List',
  /**
   * The mixins that the component can use.
   */
  mixins: [
    SlotMixin,
  ],
  /**
   * The properties that the component accepts.
   */
  props: {
    contextualStyle: {
      default: 'primary',
      type: String,
      required: false,
    },
    paramList: {
      default: null,
      type: Array,
    },
    paramShowButtons: {
      default: false,
      type: Boolean,
      required: true,
    },
    paramIsAdd: {
      default: true,
      type: Boolean,
      required: true,
    },
  },

  data() {
    return {
      toggleMenuActive: false, // 슬라이드 토글 메뉴 활성화
      isAdded: this.paramIsAdd, // 삭제상태 활성화
    };
  },
  /**
   * The computed properties that the component can use.
   */
  computed: {
    classNamesHeader() {
      const classNames = ['card-header'];

      if (this.contextualStyle) {
        classNames.push(`bg-${this.contextualStyle}`);
        classNames.push('text-white');
      } else {
        classNames.push('bg-default');
      }

      return classNames;
    },
    // 슬라이드 메뉴 선택시 상태에 맞는 높이의 클래스적용
    openSlideMenu() {
      if (this.toggleMenuActive) {
        if (this.paramShowButtons) {
          return 'open menu3';
        }
        return 'open menu2';
      }
      return '';
    },
  },

  methods: {
    // 체크모드 변경
    changeCheckInput() {
      this.isAdded = !this.isAdded; // 모드변경
      this.toggleMenuActive = false; // 슬라이드 닫기
    },
    // 추가,삭제 체크박스 선택시
    updateCheckInput(e, args) {
      // 추가, 삭제 진행함수
      const processUpdate = () => {
        // isAdded: true 추가모드 false 삭제모드
        const param = {
          isAdded: this.isAdded,
          postId: args.value,
          hidden: !!args.hidden,
        };
        this.$emit('updateCheckInput', param);
      };

      // 삭제 진행시 확인 창을 표시
      if (!this.isAdded) {
        const toastId = this.$toast.info({
          component: Confirm,
          props: {
            buttonName: '삭제',
            isShowButtons: true,
          },
          listeners: {
            // 삭제 확인시 삭제진행
            confirmEvent: () => {
              this.$toast.dismiss(toastId);
              processUpdate();
            },
            // 삭제 취소시 체크표시를 취소함
            cancelEvent: () => {
              this.$toast.dismiss(toastId);
              e.target.checked = false;
            },
          },
        }, { timeout: 7000, closeOnClick: false, closeButton: false });
      } else {
        // 추가 진행시 그냥 진행
        processUpdate();
      }
    },
    // 체크박스 등록삭제상태 표시 (computed파라미터전달이 안되서 method로 작성)
    setCheckStatus(args) {
      // 모든 일정화면에서 완료일정의 추가시 체크박스 비표시
      if (!!args.hidden && this.isAdded) {
        return 'visible-hidden';
      }
      // 추가,삭제모드의 체크 표시
      if (this.isAdded) {
        return 'list-add';
      }
      return 'list-del';
    },
  },
};
</script>
