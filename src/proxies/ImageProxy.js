import Proxy from './Proxy';

class ImageProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    // proxy.js의 부모의 constructor를 실행, 부모의 endpoint는 image사용
    super('image', parameters);
  }

  /**
   * 게시물 이미지 업로드
   *
   * @returns {Promise} The result in a promise.
   */
  uploadImage(param) {
    return this.uploadTempImage(param);
  }

  /**
   * 유저 이미지 업로드
   *
   * @returns {Promise} The result in a promise.
   */
  uploadUserImage(param) {
    return this.uploadTempImage(param, true);
  }

  /**
   * 유저 이미지 삭제
   *
   * @returns {Promise} The result in a promise.
   */
  deleteUserImage() {
    return this.submit('delete', `${this.endpoint}/userimage`);
  }
}

export default ImageProxy;
