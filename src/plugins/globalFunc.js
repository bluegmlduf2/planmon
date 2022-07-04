/* eslint-disable no-param-reassign */
import stayStatus from '@/assets/js/stayStatus';

export default {
  install(Vue) {
    // 년월일 형식반환
    Vue.prototype.getDateFormat = (date) => {
      const dt = new Date(date);
      // 데이터가 존재할때 YYYY년MM월DD일 형식으로 반환
      if (date) {
        return `${dt.getFullYear()}년 ${dt.getMonth() + 1}월 ${dt.getDate()}일`;
      }
      // 일정로딩시 공백으로 표시
      return '';
    };

    // YYYY-MM-DD형식을 반환
    // 로컬스토리지에 데이터형식을 적은용량으로 저장하기 위해 해당 포맷 사용
    Vue.prototype.getDateFormatYYYYMMDD = (date) => {
      const d = new Date(date);
      let month = `${d.getMonth() + 1}`;
      let day = `${d.getDate()}`;
      const year = d.getFullYear();

      if (month.length < 2) { month = `0${month}`; }
      if (day.length < 2) { day = `0${day}`; }

      return [year, month, day].join('-');
    };

    // 파라미터의 date에 일수를 더해서 반환
    Vue.prototype.addDays = (date, addedDay) => new Date(date.getTime() + addedDay * 24 * 60 * 60 * 1000);

    // 두 날짜 사이의 일수 구하기
    Vue.prototype.getDateDiff = (d1, d2) => {
      const diffDate = new Date(d2).getTime() - new Date(d1).getTime(); // 종료일 - 시작일
      const sign = Math.sign(diffDate) >= 0 ? '+' : '-'; // 음수양수에 따라 +-를 추가
      const diffDay = Math.ceil(Math.abs(diffDate / (1000 * 60 * 60 * 24))); // 밀리세컨 * 초 * 분 * 시 = 일

      return `${sign}${diffDay}일`;
    };

    // 리스트의 체류상태에 따라 표시 태그 반환
    Vue.prototype.setStayStatusTag = (args) => {
      // 태그명
      let tagName = '';

      switch (args) {
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

      switch (args) {
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
