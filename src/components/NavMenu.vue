<template>
  <ul
    :class="{'navbar-nav mr-auto pl-4':isForMobileNav}"
  >
    <li
      :class="{'nav-item':isForMobileNav}"
      @click="$emit('closeMenuActive')"
    >
      <router-link
        :class="{'nav-link':isForMobileNav}"
        :to="{ name: 'home.index'}"
      >
        Home
      </router-link>
    </li>
    <li
      :class="{'nav-item':isForMobileNav}"
    >
      <a
        v-if="userIsAuthenticated"
        :class="{'nav-link':isForMobileNav}"
        href="#"
        @click="onLogout"
      >
        로그아웃
      </a>
      <a
        v-else
        :class="{'nav-link':isForMobileNav}"

        href="#"
        @click="$emit('openLoginActive')"
      >
        로그인
      </a>
    </li>
    <li
      v-if="userIsAuthenticated"
      :class="{'nav-item':isForMobileNav}"
    >
      <router-link
        :class="{'nav-link':isForMobileNav}"
        :to="{ name: 'setting.index' }"
      >
        유저 설정
      </router-link>
    </li>
    <li
      v-if="userIsAuthenticated"
      :class="{'nav-item':isForMobileNav}"
    >
      <router-link
        :to="{ name: 'write.index' }"
        :class="{'nav-link':isForMobileNav}"
      >
        글쓰기
      </router-link>
    </li>
    <li
      v-if="isForMobileNav"
      class="nav-item"
    >
      <router-link
        :to="{ name: 'selection' }"
        class="nav-link"
      >
        나의 일정 설정
      </router-link>
    </li>
    <li v-if="userIsAuthenticated&&!isForMobileNav">
      <router-link :to="{ name: 'mylist.index' }">
        내가 작성한 일정
      </router-link>
    </li>
    <li
      v-else-if="isForMobileNav"
      class="nav-item dropdown"
    >
      <a
        class="nav-link dropdown-toggle"
        data-toggle="dropdown"
        aria-expanded="false"
      >
        나의 일정
      </a>
      <div class="dropdown-menu bg-dark">
        <router-link
          :to="{ name: 'todolist.index' }"
          class="dropdown-item"
          href="#"
        >
          다가오는 일정
        </router-link>
        <router-link
          :to="{ name: 'completelist.index' }"
          class="dropdown-item"
          href="#"
        >
          완료된 일정
        </router-link>
        <router-link
          :to="{ name: 'alllist.index' }"
          class="dropdown-item"
          href="#"
        >
          모든 일정
        </router-link>
        <router-link
          v-if="userIsAuthenticated"
          :to="{ name: 'mylist.index' }"
          class="dropdown-item"
          href="#"
        >
          내가 작성한 일정
        </router-link>
      </div>
    </li>
  </ul>
</template>

<script>
import message from '@/assets/js/message';

export default {
  /**
   * The name of the component.
   */
  name: 'NavMenu',
  /**
   * The properties that the component accepts.
   */
  props: {
    // 모바일용 NAV와 데스크탑용 NAV유무
    // true:모바일용,false:데스크톱
    isForMobileNav: {
      default: false,
      type: Boolean,
      required: true,
    },
    // 유저로그인상태
    userIsAuthenticated: {
      default: false,
      type: Boolean,
      required: true,
    },
    // 메뉴 토글 상태
    // true:열림,false:닫힘
    isMenuActive: {
      default: false,
      type: Boolean,
      required: true,
    },
  },

  methods: {
    // 로그아웃
    onLogout() {
      this.$emit('closeMenuActive');// nav메뉴 닫기
      this.$store.dispatch('logout'); // 유저 정보삭제
      this.$toast.info(message.logout);
    },
  },
};
</script>
