<template>
  <div class="list-container">
    <div class="list-haeder">
      <h4>
        <slot name="header" />
      </h4>
      <span>
        <i
          class="fa fa-ellipsis-h"
          aria-hidden="true"
        />
      </span>
    </div>
    <div class="list-body">
      <ul name="body">
        <li
          v-for="(item, index) in todoList"
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
    <div class="list-footer">
      <button
        type="button"
        class="btn btn-light btn-sm"
      >
        더보기
      </button>
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
    todoList: {
      default: null,
      type: Array,
    },
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
