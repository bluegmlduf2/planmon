import Proxy from './Proxy';

class MyListProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    // proxy.js의 부모의 constructor를 실행, 부모의 endpoint는 mylist사용
    super('mylist', parameters);
  }

  /**
   * 내가 작성한 일정 가져오기
   *
   * @param {String} sort 정렬
   * @param {String} pageKey 페이지네이션용 키
   *
   * @returns {Promise} The result in a promise.
   */
  getMyList({ get20perpage, currentPage }) {
    const parameter = { get20perpage, currentPage };
    return this.find(JSON.stringify(parameter));
  }
}

export default MyListProxy;
