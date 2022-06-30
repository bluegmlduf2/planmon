/* eslint-disable no-param-reassign */
import stayStatus from '@/assets/js/stayStatus';

export default {
  install(Vue) {
    // 년월일 형식반환
    Vue.prototype.getDateFormat = (date) => {
      const dt = new Date(date);
      // 데이터가 존재할때 YYYY년MM월DD일 형식으로 반환
      if (date) {
        return `${dt.getFullYear()}년 ${dt.getMonth()}월 ${dt.getDate()}일`;
      }
      // 일정로딩시 공백으로 표시
      return '';
    };

    // 리스트의 체류상태에 따라 표시 태그 반환
    Vue.prototype.setStayStatusTag = (args) => {
      // 태그명
      let tagName = '';

      switch (args.stayStatus) {
        case stayStatus[0].value:
          // 입국전
          tagName = 'tag-green';
          break;
        case stayStatus[1].value:
          // 체류중
          tagName = 'tag-blue';
          break;
        case stayStatus[2].value:
          // 귀국후
          tagName = 'tag-red';
          break;
        default:
      }

      return tagName;
    };

    // 리스트의 체류상태에 따라 표시 태그이름 반환
    Vue.prototype.setStayStatusTagName = (args) => {
      // 태그명
      let tagName = '';

      switch (args.stayStatus) {
        case stayStatus[0].value:
          // 입국전
          tagName = `${stayStatus[0].text} 일정`;
          break;
        case stayStatus[1].value:
          // 체류중
          tagName = `${stayStatus[1].text} 일정`;
          break;
        case stayStatus[2].value:
          // 귀국후
          tagName = `${stayStatus[2].text} 일정`;
          break;
        default:
      }
      return tagName;
    };
  },
};
