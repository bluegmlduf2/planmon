import Proxy from './Proxy';

class PostProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    // proxy.js의 부모의 constructor를 실행, 부모의 endpoint는 reclist사용
    super('post', parameters);
  }

  /**
   * 게시물 가져오기
   *
   * @param {String} postId 게시물 번호
   *
   * @returns {Promise} The result in a promise.
   */
  getPost(postId) {
    return this.find(postId);
  }

  /**
   * 게시물 상세정보 가져오기
   *
   * @param {String} postId 게시물 번호
   * @param {String} requestItem 게시물에서 취득할 정보
   *
   * @returns {Promise} The result in a promise.
   */
  getPostDetail({ postId, requestItem }) {
    return this.submit('get', `${this.endpoint}/${postId}/${requestItem}`);
  }

  /**
   * 게시물의 사용자 일정 변경
   *
   * @param {String} sort 정렬
   *
   * @returns {Promise} The result in a promise.
   */
  updatePostCalendar(param) {
    return this.submit('put', `${this.endpoint}/update-post-date`, param);
  }

  /**
   * 게시물 등록
   *
   * @param {String} sort 정렬
   *
   * @returns {Promise} The result in a promise.
   */
  createPost(param) {
    return this.create(param);
  }
}

export default PostProxy;
