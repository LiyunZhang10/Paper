<template>
  <el-header>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">处理中心</el-menu-item>
      <el-menu-item index="2">订单管理</el-menu-item>
      <el-menu-item index="3">购物车</el-menu-item>
    </el-menu>
  </el-header>
</template>

<script lang="ts" setup>

</script>

<style lang="scss" scoped>
.el-menu-demo {
  background-color: #545c64;
 .el-menu-item {
    color: #fff;
  }
  .el-menu-item--active {
    background-color: #409EFF;
  }
}
</style>
