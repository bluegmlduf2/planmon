<template>
  <flat-pickr
    id="entryDate"
    v-model="inputDateValue"
    :config="config"
    class="form-control flat-pickr"
    :placeholder="placeholderValue"
  />
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
    inputDate: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      placeholderValue: this.placeholder, // 플레이스홀더 ,prop로 받은 데이터를 다시 변환
      inputDateValue: this.inputDate, // 입력날짜 ,prop로 받은 데이터를 다시 변환
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
};
</script>
