/* ============
 * 메세지 리스트
 * ============
 */
export default {
  welcome: '플랜몬에 오신것을 환영합니다',
  logout: '다음에 또 봐요',
  invalidUser: '유효하지 않은 유저정보를 포함하므로 로그아웃합니다',
  changeUserInfo: '유저 정보를 변경했습니다',
  changeSelection: '유저 선택정보를 변경했습니다',
  sendEmail: '인증 이메일을 보냈습니다\n해당 메일의 인증 링크로 로그인해주세요',
  deleteUser: '회원탈퇴처리 되었습니다\n감사합니다',
  localStorageAlert: '현재 브라우저에 설정을 저장합니다\n웹데이터를 삭제하면 저장된 설정이 삭제될수있습니다\n안전하게 설정를 저장하기 위해선 로그인해주세요\n\n해당 메세지를 다시 표시하지 않으시려면 확인버튼을 눌러주세요',
  localStorageListAlert: '현재 브라우저에 일정을 저장합니다\n웹데이터를 삭제하면 저장된 일정이 삭제될수있습니다\n안전하게 일정을 저장하기 위해선 로그인해주세요\n\n해당 메세지를 다시 표시하지 않으시려면 확인버튼을 눌러주세요',
  addList: '일정을 추가했습니다',
  completeList: '일정을 완료했습니다',
  removeList: '일정을 삭제했습니다',
  removeTodoList: '등록된 할일일정을 취소하시겠습니까',
  writeConfirm: '일정 게시글은 수정은 가능하지만 삭제가 불가능합니다\n작성하시겠습니까',
  writeUpdateConfirm: '게시글을 수정하시겠습니까',
  reSearch: '추천일정 화면의 결과 재검색을 이용해주세요',
  confirmEmptyStartDate: '시작일정을 선택해주세요',
  confirmEmptyEndDate: '종료일정을 선택해주세요',
  confirmInvalidDate: '일정시작일에 일정종료일 이전 날짜를 선택해주세요',
  noticeNotChangedDate: '변경한 일정시작일과 종료일이 적용되지 않았습니다\n다시 한번 확인후 적용해주세요',
  changePostDate: '일정시작일과 일정종료일을 변경했습니다',
  addComment: '댓글을 추가했습니다',
  updateComment: '댓글을 수정했습니다',
  removeComment: '댓글을 삭제했습니다',
  addCommentReply: '대댓글을 추가했습니다',
  updateCommentReply: '대댓글을 수정했습니다',
  removeCommentReply: '대댓글을 삭제했습니다',
  emptyPostWrite: '게시글의 미입력 항목이 있습니다\n다시 한번 확인해주세요',
  addPost: '게시글을 등록했습니다',
  updatePost: '게시글을 수정했습니다',
  addImage: '이미지를 등록했습니다',
  emptyWriteCondition: '일정작성을 위해서는 국가와 체류상태를 선택해야합니다',
  imageUploadSize: '파일 사이즈를 확인해주세요\n파일 사이즈가 5MB이상인 경우에는 등록할수없습니다',
  error400: '요청에 문제가 있습니다\n잠시후에 다시 시도해주세요',
  error500: '예기치 못한 에러가 발생했습니다\n잠시후에 다시 시도해주세요',
  // 사용자 유효성 검사
  invalidEmptyInput: (e) => `${e} 입력을 해주세요`,
  invalidInputLength: (e) => `입력가능한 글자수 ${e}자를 초과했습니다`,
};
