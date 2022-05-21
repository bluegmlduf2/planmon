import Proxy from './Proxy';

class RecListProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    // proxy.js의 부모의 constructor를 실행, 부모의 endpoint는 reclist사용
    super('reclist', parameters);
  }

  /**
   * 추천 일정 가져오기
   *
   * @param {String} sort 정렬
   * @param {String} pageKey 페이지네이션용 키
   *
   * @returns {Promise} The result in a promise.
   */
  getRecList({
    country, stayStatus, entryDate, myCompletelist, myTodolist,
  }) {
    const parameter = {
      country, stayStatus, entryDate, myCompletelist, myTodolist,
    };
    return this.find(JSON.stringify(parameter));
  }
}

export default RecListProxy;
