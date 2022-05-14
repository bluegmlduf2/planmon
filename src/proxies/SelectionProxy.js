import Proxy from './Proxy';

class SelectionProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    // proxy.js의 부모의 constructor를 실행, 부모의 endpoint는 user사용
    super('selection', parameters);
  }

  /**
   * 로그인한 유저의 선택사항 가져오기
   *
   * @param {String} sort 정렬
   *
   * @returns {Promise} The result in a promise.
   */
  getSelection() {
    return this.submit('get', `${this.endpoint}/selection`);
  }
}

export default SelectionProxy;
