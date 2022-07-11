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
  createCommentReply({ commentId, commentReplyContent }) {
    const parameter = { commentId, commentReplyContent };
    return this.submit('post', `${this.endpoint}/${commentId}`, parameter);
  }

  /**
   * 대댓글 수정하기
   *
   * @param {String} postId 게시물 번호
   *
   * @returns {Promise} The result in a promise.
   */
  updateCommentReply({ commentReplyId, commentReplyContent }) {
    const parameter = { commentReplyId, commentReplyContent };
    return this.update(commentReplyId, parameter);
  }

  /**
   * 대댓글 삭제하기
   *
   * @param {String} postId 게시물 번호
   *
   * @returns {Promise} The result in a promise.
   */
  destroyCommentReply({ commentReplyId }) {
    return this.destroy(commentReplyId);
  }
}

export default CommentReplyProxy;
