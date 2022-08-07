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
    country, stayStatus, entryDate, myCompletelist, myTodolist, get20perpage, currentPage, searchWord,
  }) {
    const parameter = {
      country, stayStatus, entryDate, myCompletelist, myTodolist, get20perpage, currentPage, searchWord,
    };
    return this.submit('post', `${this.endpoint}`, parameter);
  }

  /**
   * 추천일정을 추가하기
   *
   * @param {String} sort 정렬
   *
   * @returns {Promise} The result in a promise.
   */
  updateRecList(postId) {
    return this.update(postId);
  }
}

export default RecListProxy;
