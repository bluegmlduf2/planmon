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
    const parameter = { postId };
    return this.find(JSON.stringify(parameter));
  }
}

export default PostProxy;
