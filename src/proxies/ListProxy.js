import Proxy from './Proxy';

class ListProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    // proxy.js의 부모의 constructor를 실행, 부모의 endpoint는 list사용
    super('list', parameters);
  }

  /**
   * 할일일정 가져오기
   *
   * @param {String} sort 정렬
   * @param {String} pageKey 페이지네이션용 키
   *
   * @returns {Promise} The result in a promise.
   */
  getTodoList() {
    return this.submit('get', `${this.endpoint}/todolist`);
  }
}

export default ListProxy;
