<template>
  <div class="input-group">
    <flat-pickr
      id="entryDate"
      v-model="inputDateValue"
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
      type: null, // 데이터,숫자,문자열형태등이 들어오기때문에 null로 지정
      required: true,
    },
    inputDate: {
      type: null, // 데이터,숫자,문자열형태등이 들어오기때문에 null로 지정
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
