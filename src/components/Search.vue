<template>
  <div>
    <h4 class="list-search">
      검색
    </h4>
    <div class="input-groupt">
      <button class="btn">
        <i
          aria-hidden="true"
          class="fa fa-search"
        />
      </button>
      <slot name="searchBtn" />
    </div>
  </div>
</template>

<script>
export default {
  /**
   * The name of the component.
   */
  name: 'Search',
};
</script>
