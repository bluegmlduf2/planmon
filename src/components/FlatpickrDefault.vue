<template>
  <div class="input-group">
    <flat-pickr
      id="entryDate"
      v-model="entryDate"
      :config="config"
      class="form-control flat-pickr"
      :placeholder="placeholderValue"
    />
    <button
      type="button"
      class="btn bg-transparent"
      style="margin-left: -40px; z-index: 100; color:#7b8694"
      data-clear
    >
      <i class="fa fa-times" />
    </button>
  </div>
</template>

<script>
import korean from 'flatpickr/dist/l10n/ko';

export default {
  /**
   * The name of the component.
   */
  name: 'Flatpickr',

  /**
   * The properties that the component accepts.
   */
  props: {
    placeholder: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      placeholderValue: this.placeholder, // 플레이스홀더 ,prop로 받은 데이터를 다시 변환
      config: {
        wrap: true,
        altFormat: 'Y년 M J',
        altInput: true,
        dateFormat: 'Y-m-d',
        locale: korean.ko,
        disableMobile: 'true', // flatpicker모바일모드끄기
      },
    };
  },
  computed: {
    entryDate: {
      get() {
        return this.$store.getters.selection.entryDate;
      },
      set(value) {
        this.$store.dispatch('addSelection', { entryDate: value });
      },
    },
  },
};
</script>
