/**
 * 참조문서
 * https://vue-meta.nuxtjs.org
 */
import Vue from 'vue';
import Meta from 'vue-meta';

Vue.use(Meta, {
  keyName: 'metaInfo', // component에서 사용할 이름
  attribute: 'data-vue-meta', // vue-meta에서 해당 메타태그를 관리하겠다고 지정해주는 역할,index.html은 고정적인 녀석이고 이건 변화될 녀석 (디폴트)
  ssrAttribute: 'data-vue-meta-server-rendered',
  tagIDKeyName: 'vmid', // 해당태그가 동일한 다른 메타태그랑 겹치더라도 vmid가 붙은것이 우선순위를 가지고 표시하도 록함 (디폴트)
  refreshOnceOnNavigation: true,
});
