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
          <li>
            <slot name="deleteList">
              일정 삭제
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
          <div class="list-item">
            <div class="list-checkbox">
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
};
</script>
