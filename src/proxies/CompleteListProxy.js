import Proxy from './Proxy';

class CompleteListProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    // proxy.js의 부모의 constructor를 실행, 부모의 endpoint는 completelist사용
    super('completelist', parameters);
  }

  /**
   * 완료 일정 가져오기
   *
   * @param {String} sort 정렬
   * @param {String} pageKey 페이지네이션용 키
   *
   * @returns {Promise} The result in a promise.
   */
  getCompleteList({ myCompletelist }) {
    const parameter = myCompletelist.map((e) => e.postId);
    return this.find(JSON.stringify(parameter));
  }
}

export default CompleteListProxy;
