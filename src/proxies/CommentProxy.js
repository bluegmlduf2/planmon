import Proxy from './Proxy';

class CommentProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('comment', parameters);
  }

  /**
   * 댓글 가져오기
   *
   * @param {String} postId 게시물 번호
   *
   * @returns {Promise} The result in a promise.
   */
  getComment(postId) {
    return this.find(postId);
  }

  /**
   * 댓글 등록하기
   *
   * @param {String} postId 게시물 번호
   *
   * @returns {Promise} The result in a promise.
   */
  createComment({ postId, commentContent }) {
    const parameter = { postId, commentContent };
    return this.submit('post', `${this.endpoint}/${postId}`, parameter);
  }

  /**
   * 댓글 수정하기
   *
   * @param {String} postId 게시물 번호
   *
   * @returns {Promise} The result in a promise.
   */
  updateComment({ commentId, commentContent }) {
    const parameter = { commentId, commentContent };
    return this.update(commentId, parameter);
  }

  /**
   * 댓글 삭제하기
   *
   * @param {String} postId 게시물 번호
   *
   * @returns {Promise} The result in a promise.
   */
  destroyComment({ commentId }) {
    return this.destroy(commentId);
  }
}

export default CommentProxy;
