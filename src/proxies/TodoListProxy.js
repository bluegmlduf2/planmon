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
    myTodolist, get20perpage, currentPage, getAllPages,
  }) {
    const parameter = { get20perpage, currentPage, getAllPages };
    parameter.myTodolist = myTodolist?.map((e) => e.postId);
    return this.find(JSON.stringify(parameter));
  }
}

export default TodoListProxy;
