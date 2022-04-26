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

  // 다가오는 일정
  {
    path: '/todolist',
    name: 'todolist.index',
    component: () => import('@/views/Todolist/Index.vue'),
  },

  // 추천 일정
  {
    path: '/reclist',
    name: 'reclist.index',
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
    path: '/post',
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

  {
    path: '/*',
    redirect: '/home',
  },
];
