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

  // 에러페이지
  {
    path: '/*',
    name: 'error.index',
    component: () => import('@/views/Error/Index.vue'),
  },
];
