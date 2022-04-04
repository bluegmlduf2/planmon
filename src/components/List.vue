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
          class="list-menu"
          :class="[toggleMenuActive?'open':'']"
        >
          <li>최근일자순으로 정렬</li>
          <li>완료순으로 정렬</li>
          <li
            @click="deleteButtonActive=!deleteButtonActive"
          >
            <slot
              name="deleteList"
            >
              {{ deleteButtonActive?'일정 추가':'일정 삭제' }}
            </slot>
          </li>
        </ul>
      </div>
    </div>
    <div class="list-body">
      <ul class="list-body-ul">
        <li
          v-for="(item, index) in paramList"
          :key="index"
        >
          <!-- 일정삭제모드 -->
          <div class="list-item">
            <div
              v-if="deleteButtonActive"
              class="list-checkbox list-del"
            >
              <input
                :id="item.value"
                type="checkbox"
              >
              <label :for="item.value" />
            </div>
            <!-- 일정추가모드 -->
            <div
              v-else
              class="list-checkbox list-add"
            >
              <input
                :id="item.value"
                type="checkbox"
              >
              <label :for="item.value" />
            </div>
            <span class="list-content ellipsis">
              {{ item.text }}
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import SlotMixin from '@/mixins/slot';

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
  },

  data() {
    return {
      toggleMenuActive: false, // 슬라이드 토글 메뉴 활성화
      deleteButtonActive: false, // 삭제상태 활성화
    };
  },

  /**
   * The computed properties that the component can use.
   */
  computed: {
    /**
     * Computed property which will compute the classes
     * for the header of the card.
     *
     * @returns {Array} The classes for the header.
     */
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
  },

  methods: {
    // TODO 버튼클릭시 선택화면 뜬다음에 선택하면 삭제 ,그리고 체크시 해당 체크이외에 전부 취소
  },
};
</script>
