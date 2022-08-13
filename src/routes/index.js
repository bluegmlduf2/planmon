/* ============
 * Routes File
 * ============
 *
 * The routes and redirects are defined in this file.
 */

export default [
  // 홈
  {
    path: '/',
    name: 'home.index',
    component: () => import('@/views/Home/Index.vue'),
  },

  // 할일 일정
  {
    path: '/todolist',
    name: 'todolist.index',
    props: true, // route.param 전달데이터를 props로도 받는다
    component: () => import('@/views/Todolist/Index.vue'),
  },

  // 추천 일정
  {
    path: '/reclist',
    name: 'reclist.index',
    props: true, // route.param 전달데이터를 props로도 받는다
    component: () => import('@/views/Reclist/Index.vue'),
  },

  // 완료 일정
  {
    path: '/completelist',
    name: 'completelist.index',
    component: () => import('@/views/Completelist/Index.vue'),
  },

  // 모든 일정
  {
    path: '/alllist',
    name: 'alllist.index',
    component: () => import('@/views/Alllist/Index.vue'),
  },

  // 내 일정
  {
    path: '/mylist',
    name: 'mylist.index',
    component: () => import('@/views/Mylist/Index.vue'),
    meta: {
      auth: true,
    },
  },

  // 글쓰기 화면
  {
    path: '/write',
    name: 'write.index',
    props: true, // route.param 전달데이터를 props로도 받는다
    component: () => import('@/views/Write/Index.vue'),
    meta: {
      auth: true,
    },
  },

  // 게시글 보기 화면
  {
    path: '/post/:postId',
    name: 'post.index',
    component: () => import('@/views/Post/Index.vue'),
  },

  // 환경설정
  {
    path: '/setting',
    name: 'setting.index',
    component: () => import('@/views/Setting/Index.vue'),
    meta: {
      auth: true,
    },
  },

  // 유저선택정보 (컴포넌트지만 예외적으로 화면으로 사용)
  {
    path: '/selection',
    name: 'selection',
    props: { isRoutedRequest: true }, // 라우트로 화면 이동시 초기화 필요유무를 위해 매개변수전달
    component: () => import('@/components/Selection.vue'),
  },

  // 에러페이지
  {
    path: '/*',
    name: 'error.index',
    component: () => import('@/views/Error/Index.vue'),
  },
];
