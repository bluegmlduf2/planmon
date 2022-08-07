import Proxy from './Proxy';

class TodoListProxy extends Proxy {
  /**
   * The constructor for the ArtistProxy.
   *
   * @param {Object} parameters The query parameters.
   */
  constructor(parameters = {}) {
    // proxy.js의 부모의 constructor를 실행, 부모의 endpoint는 todolist사용
    super('todolist', parameters);
  }

  /**
   * 할일 일정 가져오기
   *
   * @param {String} sort 정렬
   * @param {String} pageKey 페이지네이션용 키
   *
   * @returns {Promise} The result in a promise.
   */
  getTodoList({
    myTodolist, get20perpage, currentPage, getAllPages, searchWord,
  }) {
    const parameter = {
      get20perpage, currentPage, getAllPages, searchWord,
    };
    parameter.myTodolist = myTodolist?.map((e) => e.postId);
    return this.submit('post', `${this.endpoint}`, parameter);
  }

  /**
   * 할일일정을 추가하기
   *
   * @param {String} sort 정렬
   *
   * @returns {Promise} The result in a promise.
   */
  updateTodoList(postId) {
    return this.update(postId);
  }

  /**
   * 할일일정을 삭제하기
   *
   * @param {String} sort 정렬
   *
   * @returns {Promise} The result in a promise.
   */
  destroyTodoList(postId) {
    return this.destroy(postId);
  }
}

export default TodoListProxy;
