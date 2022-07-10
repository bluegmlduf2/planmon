import Proxy from './Proxy';

class CommentReplyProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    super('commentreply', parameters);
  }

  /**
   * 대댓글 등록하기
   *
   * @param {String} postId 게시물 번호
   *
   * @returns {Promise} The result in a promise.
   */
  createCommentReply(param) {
    return this.create(param);
  }
}

export default CommentReplyProxy;
